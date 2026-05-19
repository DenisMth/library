from sqlalchemy.orm import Session
from sqlalchemy import select
from Models.author import Authors

def create_author(session: Session, first_name: str, last_name: str):
    author = Authors(first_name=first_name, last_name=last_name)

    session.add(author)
    session.commit()
    session.refresh(author)

    return author