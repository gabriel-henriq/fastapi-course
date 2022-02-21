from itsdangerous import json
import pytest
from fastapi import status

from app import schemas


def test_get_all_posts(client, test_posts):
    response = client.get('/posts/')

    assert len(response.json()) == len(test_posts)
    assert response.status_code == status.HTTP_200_OK


def test_get_one_post(client, test_posts):
    response = client.get(f'/posts/{test_posts[0].id}')

    assert response.status_code == status.HTTP_200_OK


def test_get_param_post(client, test_posts):
    response = client.get('/posts/?search=first')

    assert response.status_code == status.HTTP_200_OK


def test_not_exist_post(client, test_posts):
    response = client.get('/posts/10')

    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_unprocessable_post(client, test_posts):
    response = client.get('/posts/asd')

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.parametrize("title, content, published", [
    ("First Title", "First Content", True),
    ("Second Title", "Second Content", False),
])
def test_create_post(test_user, authorized_client, title, content, published):
    response = authorized_client.post(
        "/posts/", json={"title": title, "content": content, "published": published})
    assert response.status_code == status.HTTP_201_CREATED


def test_create_post_default_published_true(authorized_client):
    response = authorized_client.post(
        '/posts/', json={"title": "Title", "content": "Content"})

    created_post = schemas.Post(**response.json())

    assert created_post.content == "Content"
    assert created_post.title == "Title"
    assert created_post.published == True
    assert response.status_code == status.HTTP_201_CREATED


def test_unauthorized_create_post(client):
    response = client.post(
        '/posts/', json={"title": "Unauthorrized Title", "content": "Unauthorized Content"})

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.parametrize("id_indice", [
    (0),
    (1),
    (2)
])
def test_unauthorized_delete_post(client, test_posts, id_indice):
    response = client.delete(f"/posts/{test_posts[id_indice].id}")

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.parametrize("id_indice", [
    (0),
    (1),
    (2)
])
def test_authorized_delete_post(authorized_client, test_posts, id_indice):
    response = authorized_client.delete(f"/posts/{test_posts[id_indice].id}")

    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_delete_post_non_exist(authorized_client, test_posts):
    response = authorized_client.delete("/posts/9999")

    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.parametrize("id_indice, title, content", [
    (0, "Updating Title", "Updating Content"),
    (1, "Updating another title", "Updating another content"),
    (2, "updating last post title", "updating last post content")
])
def test_unauthorized_update_post(client, test_user, test_posts, title, content, id_indice):
    response = client.put(
        f"/posts/{test_posts[id_indice].id}", json={"title": title, "content": content})

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.parametrize("id_indice, title, content", [
    (0, "Updating Title", "Updating Content"),
    (1, "Updating another title", "Updating another content"),
    (2, "updating last post title", "updating last post content")
])
def test_authorized_update_post(authorized_client, test_user, test_posts, title, content, id_indice):
    response = authorized_client.put(
        f"/posts/{test_posts[id_indice].id}", json={"title": title, "content": content})

    assert response.status_code == status.HTTP_202_ACCEPTED
