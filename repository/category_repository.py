from sqlalchemy.orm import Session
from sqlalchemy import select
from Models.category import Categories

def create_category(session: Session, name: str):
    category = Categories(name=name)

    session.add(category)
    session.commit()
    session.refresh(category)

    return category

def get_category_by_id(session: Session, category_id: int):
    stmt = select(Categories).where(Categories.id == category_id)
    category = session.execute(stmt).scalar_one_or_none()
    return category

def delete_category_by_id(session: Session, category_id: int):
    stmt = select(Categories).where(Categories.id == category_id)
    category = session.execute(stmt).scalar_one_or_none()

    if category is None:
        return False

    session.delete(category)
    session.commit()
    return True