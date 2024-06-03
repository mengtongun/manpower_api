from datetime import date
from typing import Optional

from pydantic import BaseModel


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


class UpdateEmployeeRequest(BaseModel):
    designation: Optional[str] = None
    project: Optional[str] = None
    team: Optional[str] = None
    supervisor: Optional[str] = None
    joinDate: Optional[str] = None
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
