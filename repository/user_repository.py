from sqlalchemy.orm import Session
from sqlalchemy import select
from Models.user import Users

def create_user(session, Session, first_name: str, last_name: str, username: str, password: str, role: str, email: str):
    user = Users(first_name=first_name, last_name=last_name, username=username, password=password, role=role, email=email)

    session.add(user)
    session.commit()
    session.refresh(user)

    return user