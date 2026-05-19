from sqlalchemy.orm import Session
from sqlalchemy import select
from Models.rented_book import RentedBooks

def create_rented_book(session: Session, user_id: int, book_id: int, start_date, end_date, return_date):
    rented_book = RentedBooks(user_id, book_id, start_date, end_date, return_date)

    session.add(rented_book)
    session.commit()
    session.refresh(rented_book)

    return rented_book