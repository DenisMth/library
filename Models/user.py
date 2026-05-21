from db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    
    username: Mapped[str] = mapped_column(String(100))
    password: Mapped[str] = mapped_column(String(255))

    role: Mapped[str] = mapped_column(String(100))

    email: Mapped[str] = mapped_column(
        String(200),
        unique=True,
    )

    def repr(self):
        return f"{self.first_name} {self.last_name} {self.username} {self.role} {self.email}"

    
    