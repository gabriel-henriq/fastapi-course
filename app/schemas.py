from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, conint


class BasePost(BaseModel):
    title: str
    content: str
    published: bool = True


class BaseUser(BaseModel):
    email: EmailStr
    password: str


class CreatePost(BasePost):
    pass


class CreateUser(BaseUser):
    email: EmailStr
    password: str


class UpdateUser(BaseModel):
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class Post(BasePost):
    id: int
    created_at: datetime
    owner: UserOut

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str]


class Vote(BaseModel):
    post_id: int
    dir: conint(ge=0, le=1)
