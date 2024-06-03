import io

import pandas as pd
from sqlalchemy.orm import Session

from manpower_api.database import engine
from manpower_api.employees.exceptions import EmployeeNotExisted
from manpower_api.employees.models import Employee
from manpower_api.employees.schemas import UpdateEmployeeRequest


def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(Employee)
        .order_by(Employee.id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def export_employees(db: Session, stream: io.StringIO):
    sql = db.query(Employee).order_by(Employee.id).statement
    df = pd.read_sql(sql, con=engine)
    df.to_csv(stream, index=False)


def update_employees(db: Session, manpower_id: str, data: UpdateEmployeeRequest):
    employee_db = db.query(Employee).filter(
        Employee.manpowerId == manpower_id).first()
    if not employee_db:
        raise EmployeeNotExisted
    to_update = data.model_dump(exclude_unset=True)
    for key, value in to_update.items():
        setattr(employee_db, key, value)
    to_update['id'] = employee_db.id
    db.commit()
    return employee_db
