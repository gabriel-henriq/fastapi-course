from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List
from .. import models, schemas, utils
from ..database import get_db
from ..oauth2 import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/", response_model=List[schemas.UserOut])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()

    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="There's not exist any user.")
    return users


@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int,
             db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Could not found user with id {id}")

    return user


@router.post("/", status_code=status.HTTP_201_CREATED,
             response_model=schemas.UserOut)
def create_user(user: schemas.CreateUser,
                db: Session = Depends(get_db)):

    user.password = utils.hash(user.password)
    new_user = models.User(**user.dict())

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        print(new_user)
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"This email already exists.")

    return new_user


@router.put("/", status_code=status.HTTP_202_ACCEPTED,
            response_model=schemas.UserOut)
def update_user(user: schemas.UpdateUser,
                id: int,
                db: Session = Depends(get_db),
                current_user: int = Depends(get_current_user)):

    user_query = db.query(models.User).filter(models.User.id == id)
