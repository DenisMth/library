from sqlalchemy.orm import Session
from sqlalchemy import select
from Models.user import Users
import bcrypt
from pydantic import BaseModel, EmailStr
from fastapi import HTTPException

class User(BaseModel):
    first_name: str
    last_name: str
    username: str
    password: str
    role: str
    email: EmailStr

def hash_password(password: str):

    hashed = bcrypt.hashpw(
        password.encode('utf-8'),
        bcrypt.gensalt()
    )
    return hashed

def verify_password(password: str, hashed: str):
    return bcrypt.checkpw(
        password.encode(),
        hashed.encode()
    )

def create_user(session: Session, user_data: User):
    user = Users(
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        username=user_data.username,
        password=hash_password(user_data.password),
        role=user_data.role,
        email=user_data.email)

    try:

        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=str(e))



def get_user_by_id(session: Session, id: int):
    stmt = select(Users).where(Users.id == id)
    user = session.execute(stmt).scalar_one_or_none()
    return user

def update_user_last_name(session: Session, user_id, last_name):
    stmt = select(Users).where(Users.id == user_id)
    user = session.execute(stmt).scalar_one_or_none()

    if user is None:
        return False

    user.last_name = last_name
    session.commit()
    session.refresh(user)

    return user

def update_user_first_name(session: Session, user_id, first_name):
    stmt = select(Users).where(Users.id == user_id)
    user = session.execute(stmt).scalar_one_or_none()

    if user is None:
        return False

    user.last_name = first_name
    session.commit()
    session.refresh(user)

    return user

def delete_user_by_id(session, user_id):
    stmt = select(Users).where(Users.id == user_id)
    user = session.execute(stmt).scalar_one_or_none()

    if user is None:
        return False

    session.delete(user)
    session.commit()

    return True

