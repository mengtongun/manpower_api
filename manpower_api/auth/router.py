from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from manpower_api.auth.schemas import (LoginRequest, RegisterUserRequest,
                                       UserResponse)
from manpower_api.auth.services import create_user, login
from manpower_api.database import get_db

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def register_user(
    data: RegisterUserRequest,
    db: Session = Depends(get_db),
):
    return create_user(db, data)


@router.post("/login", response_model=UserResponse)
async def login_user(
    data: LoginRequest,
    db: Session = Depends(get_db),

):
    return login(db, data)
