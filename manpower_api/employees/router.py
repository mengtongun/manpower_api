import io
from typing import List

from fastapi import APIRouter, Depends, status
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from manpower_api.auth.basic import basic_auth
from manpower_api.database import get_db
from manpower_api.employees.schemas import (EmployeeResponse,
                                            UpdateEmployeeRequest)
from manpower_api.employees.services import (export_employees, get_employees,
                                             update_employees)

router = APIRouter()


@router.get("/employees", response_model=List[EmployeeResponse])
def list_employees(skip: int = 0, limit: int = 100, _=Depends(basic_auth), db: Session = Depends(get_db)):
    """
    Retrieves all employee data from the SampleManpowerList table.
    """
    items = get_employees(db, skip=skip, limit=limit)
    return items


@router.patch("/employees/{manpower_id}", response_model=EmployeeResponse)
def edit_employee(manpower_id: str, data: UpdateEmployeeRequest, _=Depends(basic_auth), db: Session = Depends(get_db)):
    """
    Updates specific details of an employee.
    """
    items = update_employees(db, manpower_id, data)
    return items


@router.get("/employees/csv")
def download_employees_csv(_=Depends(basic_auth), db: Session = Depends(get_db)):
    """
    Downloads all employee data in CSV format.
    """
    stream = io.StringIO()
    export_employees(db, stream)
    response = StreamingResponse(iter([stream.getvalue()]),
                                 media_type="text/csv"
                                 )
    response.headers["Content-Disposition"] = "attachment; filename=export.csv"
    return response
