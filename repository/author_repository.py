from sqlalchemy.orm import Session
from sqlalchemy import select
from Models.author import Authors

def create_author(session: Session, first_name: str, last_name: str):
    author = Authors(first_name=first_name, last_name=last_name)

    try :
        session.add(author)
        session.commit()
        session.refresh(author)
    except:
        session.rollback()

    return author

def get_author_by_id(session: Session, author_id: int):
    stmt = select(Authors).where(Authors.id == author_id)
    author = session.execute(stmt).scalar_one_or_none()
    return author

def delete_author_by_id(session: Session, author_id: int):
    stmt = select(Authors).where(Authors.id == author_id)
    author = session.execute(stmt).scalar_one_or_none()

    if author is None:
        return False

    session.delete(author)
    session.commit()

    return True