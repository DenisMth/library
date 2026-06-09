from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status
from pydantic import BaseModel, EmailStr

from db.database import get_db
from repository.user_repository import get_user_by_id, create_user

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

class UserResponse(BaseModel):
    id: int
    last_name: str
    first_name: str
    email: str

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    password: str
    role: str


@router.post("/create", status_code=status.HTTP_201_CREATED)
def add_user(user: UserCreate, session: Session = Depends(get_db)):

    created_user = create_user(session, user)

    return {
        "id": created_user.id,
        "Last name": created_user.last_name,
        "First name": created_user.first_name,
        "E-mail": created_user.email,
    }

@router.get("/{user_id}")
def read_user(user_id: int, session: Session = Depends(get_db)):

    user = get_user_by_id(session, user_id)

    return {
        "id": user.id,
        "Last name": user.last_name,
        "First name": user.first_name,
        "E-mail": user.email,
    }