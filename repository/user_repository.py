from sqlalchemy.orm import Session
from sqlalchemy import select
from Models.user import Users
import bcrypt

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

def create_user(session: Session, first_name: str, last_name: str, username: str, password, role: str, email: str):
    user = Users(
        first_name=first_name,
        last_name=last_name,
        username=username,
        password=hash_password(password),
        role=role,
        email=email)

    session.add(user)
    session.commit()
    session.refresh(user)

    return user

