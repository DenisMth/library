from db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

class Books(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(String(255))

    author_id: Mapped[int] = mapped_column(
        ForeignKey("authors.id"),
        unique = True,
        nullable = False
    )

    status: Mapped[str] = mapped_column(String(100))

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"),
        unique = True,
        nullable = False
    )