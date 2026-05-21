from sqlalchemy.orm import Session
from sqlalchemy import select
from Models.book import Books

def create_book(session: Session, title: str, author_id: int, status: str, category_id: int):
    book = Books(title=title, author_id=author_id, status=status, category_id=category_id)

    session.add(book)
    session.commit()
    session.refresh(book)

    return book

def get_book_by_id(session, book_id):
    stmt = select(Books).where(Books.id == book_id)
    book = session.execute(stmt).scalar_one_or_none()

    return book

def delete_book_by_id(session, book_id):
    stmt = select(Books).where(Books.id == book_id)
    book = session.execute(stmt).scalar_one_or_none()

    if book is None:
        return False

    session.delete(book)
    session.commit()

    return True