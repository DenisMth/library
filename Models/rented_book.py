from db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, TIMESTAMP, ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

class RentedBooks(Base):
    __tablename__ = "rented_books"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique = True,
        nullable = False
    )

    book_id: Mapped[int] = mapped_column(
        ForeignKey("books.id"),
        unique = True,
        nullable = False
    )

    start_date: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP)
    end_date: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP)
    return_date: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP)
