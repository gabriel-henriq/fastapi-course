
# FastAPI Project

I create this project leaded by [Saanjev](https://www.youtube.com/channel/UC2sYgV-NV6S5_-pqLGChoNQ), teacher at [freeCodeCamp](https://freecodecamp.org/) in the
 Python API Development Course.
## Acknowledgements

 - [Python API Development - Comprehensive Course for Beginners](https://www.freecodecamp.org/news/creating-apis-with-python-free-19-hour-course/)
 

## Features

- CRUD using Restful Architecture;
- Unitary Tests using Pytest;
- Alembic Migration Tool for database maintainability;
- FastAPI micro-framework for creating fast api's;
- Postman for testing routes and documenting;
- Pydantic for data models and typing;
- SQLAlchemy for creating a native way to manipulate databases with Python;
- JWT for routes that need be authenticated;
- CORS for domains controls;
- Docker;
- Deploy using heroku;
- CI/CD using GitHub Actions.



## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DATABASE_HOSTNAME = String`

`DATABASE_PORT = Integer`

`DATABASE_NAME = String`

`DATABASE_PASSWORD = String`

`DATABASE_USERNAME = String`

`SECRET_KEY = String`

`ALGORITHM = String`

`ACCESS_TOKEN_EXPIRE_MINUTES = Integer`



## Installation Locally (Full Guide)

Clone this project with:

```bash
  git clone https://github.com/gabriel-henriq/fastapi-course.git
```

CD the folder project:

```bash
  cd fastapi-course
```

Then install a python virtual environment with:

```bash
  virtualenv env
```

Activate your virtual environment

```bash
source env/bin/activate.bash
```

Install all dependencies with:

```bash
pip install -r requirements.txt
```

After all the code above, you will need an postgres database already configured to run 
with your environment variables, finally run the last commands to create your database schemas.

```bash
alembic upgrade head
```

To turn on your server you can use:


```bash
uvicorn app.main:app
```

or

```bash
uvicorn app.main:app --reload
```
## API Reference

You can use [this public postman](https://www.postman.com/spacecraft-geoscientist-97585229/workspace/my-workspace/collection/16203062-62a34f39-42ac-4eca-9d73-202de27915eb).

Don't forget to setup the enviroment in right top to **FastAPI: Course**

#### Create User

```http
  POST /users/
```
Create a user
| Parameter | Type     | Description  |
| :-------- | :------- | :----------- |
| `email`   | `string` | **Required**.|
| `password`| `string` | **Required**.|

#### Get User

```http
  GET /users/${id}
```
Get a specfic user fetching by **id**
| Parameter | Type     | Description    |
| :-------- | :------- | :------------- |
| `id`      | `integer`| **Required**.  |

```http
  POST /posts/
```
Create a post for authenticated users

| Parameter     | Type     | Description    |
| :--------     | :------- | :------------- |
| `title`       | `string` | **Required**   |
| `content`     | `string` | **Required**   |
| `published`   | `boolean`| **Optional**   |

```http
  PUT /posts/${id}
```
Updating posts for authenticated users that provides **title**, **content** 
and **Optional published** using body with json format, example:

```json 
{
  "title": "New Title",
  "content": "New Content",
  "published": False
}
```

| Parameter | Type        |  Description   |
| :-------- | :-------    | :------------- |
| `id`      | `integer`   | **Required**   |


```http
  DELETE /posts/${id}
```
Delete a post for authenticated users that provides an **id** in url parameter

| Parameter | Type      | Description   |
| :-------  | :------   | :----------   |
|  `id`     | `integer` |  **Required** |

```http
  GET /posts/
```

Get all posts from all users

| Parameter | Type      | Description   |
| :-------  | :------   | :----------   |
|  `None`   | `None`    |  **None**     |