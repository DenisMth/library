from sqlalchemy.orm import Session
from sqlalchemy import select
from Models.category import Categories

def create_category(session: Session, name: str):
    category = Categories(name=name)

    session.add(category)
    session.commit()
    session.refresh(category)

    return category