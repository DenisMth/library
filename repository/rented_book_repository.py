from asyncio.windows_events import NULL

from sqlalchemy.orm import Session
from sqlalchemy import select
from Models.rented_book import RentedBooks

def create_rented_book(session: Session, user_id: int, book_id: int, start_date, end_date):
    rented_book = RentedBooks(user_id=user_id, book_id=book_id, start_date=start_date, end_date=end_date)

    session.add(rented_book)
    session.commit()
    session.refresh(rented_book)

    return rented_book

def get_rented_book_by_id(session: Session, rented_book_id: int):
    stmt = select(RentedBooks).where(RentedBooks.book_id == rented_book_id)
    rented_book = session.execute(stmt).scalar_one_or_none()
    return rented_book

def delete_book_by_id(session: Session, rented_book_id: int):
    stmt = select(RentedBooks).where(RentedBooks.book_id == rented_book_id)
    rented_book = session.execute(stmt).scalar_one_or_none()

    if rented_book is None:
        return False

    session.delete(rented_book)
    session.commit()
    return True