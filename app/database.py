from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

db_hostname = settings.database_hostname
db_username = settings.database_username
db_name = settings.database_name
db_pass = settings.database_password
db_port = settings.database_port


SQLALCHEMY_DATABASE_URL = f"postgresql://{db_username}:{db_pass}@{db_hostname}:{db_port}/{db_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
