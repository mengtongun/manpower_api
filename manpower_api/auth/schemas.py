from typing import Optional

from pydantic import BaseModel
from datetime import date


class Employee(BaseModel):
    id: int
    nric4Digit: str
    name: str
    manpowerId: str
    designation: str
    project: str
    team: str
    supervisor: str
    joinDate: date
    resignDate: Optional[date] = None


class EmployeeResponse(BaseModel):
    nric4Digit: str
    name: str
    manpowerId: str
    designation: str
    project: str
    team: str
    supervisor: str
    joinDate: date
    resignDate: Optional[date] = None


class UserResponse(BaseModel):
    username: str
    email: str
    is_active: bool


class UserBase(BaseModel):
    username: str
    email: str


class RegisterUserRequest(UserBase):
    password: str


class LoginRequest(BaseModel):
    username: str
    password: str
