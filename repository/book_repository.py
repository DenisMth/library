from sqlalchemy.orm import Session
from sqlalchemy import select
from Models.book import Books

def create_book(session: Session, title: str, author_id: int, status: str, category_id: int):
    book = Books(title=title, author_id=author_id, status=status, category_id=category_id)

    session.add(book)
    session.commit()
    session.refresh(book)

    return book