from db.database import Base, engine
from sqlalchemy.orm import sessionmaker
from Models.author import Authors
from Models.user import Users
from Models.category import Categories
from Models.book import Books
from Models.rented_book import RentedBooks
from repository.user_repository import create_user

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)

with SessionLocal() as session:
    user = create_user(session, "MATHIEU", "Denis", "DenisMth", "test1234", "admin", "denis@mail.com")
    print(user)