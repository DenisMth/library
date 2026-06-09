from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from repository.author_repository import get_author_by_id

router = APIRouter(
    prefix="/authors",
    tags=["authors"],
)

@router.get("/{author_id}")
def read_author(author_id: int, session: Session = Depends(get_db)):

    author = get_author_by_id(session, author_id)

    return {
        "id": author.id,
        "Last name": author.last_name,
        "First name": author.first_name
    }