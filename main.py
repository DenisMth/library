# from db.database import Base, engine
# from sqlalchemy.orm import sessionmaker
# from repository.user_repository import create_user, get_user_by_id
#
# SessionLocal = sessionmaker(bind=engine)
#
# with SessionLocal() as session:
#     user = create_user(session, "Denis", "MATHIEU", "DenisMth", "test1234", "admin", "denis@mail.com")
#     print(user)
#
#     new_user = create_user(session, "John", "DOE", "JohnDoe", "test1234567", "user", "john@doe.com")
#
#     other_user = get_user_by_id(session, 1)
#     print(f"{other_user.last_name} {other_user.first_name}")

from fastapi import FastAPI
from typing import Optional
from repository.user_repository import create_user, get_user_by_id
from repository.author_repository import create_author, get_author_by_id
from routers import users, authors

from db.database import Base, engine
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(bind=engine)

app = FastAPI()


app.include_router(users.router)
app.include_router(authors.router)