from sqlalchemy.orm import Session

from manpower_api.auth.exceptions import (EmailTaken, InvalidCredentials,
                                          NotAuthenticated, UsernameTaken)
from manpower_api.auth.models import User
from manpower_api.auth.schemas import LoginRequest, RegisterUserRequest
from manpower_api.auth.security import check_password, hash_password


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email.lower()).first()


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username.lower()).first()


def login(db: Session, user: LoginRequest):
    db_user = get_user_by_username(db, user.username)
    if not db_user:
        raise InvalidCredentials()
    is_correct_password = check_password(
        user.password, db_user.hashed_password)
    if not (is_correct_password):
        raise InvalidCredentials()
    return db_user


def create_user(db: Session, user: RegisterUserRequest):
    # Validate User Payload
    if (get_user_by_email(db, user.email)):
        raise EmailTaken()
    if (get_user_by_username(db,  user.username)):
        raise UsernameTaken()
    hashed_password = hash_password(user.password)
    db_user = User(
        email=user.email,
        username=user.username,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def verify_basic_auth(db: Session, username: str, password: str):
    if not username or not password:
        raise NotAuthenticated()
    db_user = get_user_by_username(db,  username)
    if not db_user:
        raise NotAuthenticated()
    is_correct_password = check_password(
        password, db_user.hashed_password)
    if not (is_correct_password):
        raise NotAuthenticated()
    return db_user
