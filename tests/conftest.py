from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import models
from app.main import app
from app.config import settings
from app.database import get_db
from app.database import Base
from app.oauth2 import create_access_token

db_hostname = settings.database_hostname
db_username = settings.database_username
db_name = settings.database_name
db_pass = settings.database_password
db_port = settings.database_port
SQLALCHEMY_DATABASE_URL = f"postgresql://{db_username}:{db_pass}@{db_hostname}:{db_port}/{db_name}_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


@pytest.fixture
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


@pytest.fixture
def test_user(client):
    user_data = {"email": "g@gmail.com", "password": "123"}
    response = client.post("/users/", json=user_data)
    new_user = response.json()
    new_user["password"] = user_data["password"]
    return new_user


@pytest.fixture
def token(test_user):
    return create_access_token({"user_id": test_user['id']})


@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }

    return client


@pytest.fixture
def test_posts(test_user, session):
    posts_data = [
        {
            "title": "first title",
            "content": "first content",
            "owner_id": test_user["id"]
        },
        {
            "title": "second title",
            "content": "second content",
            "owner_id": test_user["id"]
        },
        {
            "title": "third title",
            "content": "third content",
            "owner_id": test_user["id"]
        }
    ]

    def create_post_model(post):
        return models.Post(**post)

    post_map = map(create_post_model, posts_data)
    posts = list(post_map)
    session.add_all(posts)
    session.commit()
    posts = session.query(models.Post).all()

    return posts
