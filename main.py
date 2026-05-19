from db.database import Base, engine
from sqlalchemy.orm import sessionmaker
from Models.author import Authors
from Models.user import Users
from Models.category import Categories
from Models.book import Books
from Models.rented_book import RentedBooks

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)

with SessionLocal() as session:
    pass