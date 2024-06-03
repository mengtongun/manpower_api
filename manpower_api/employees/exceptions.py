from manpower_api.auth.constants import ErrorCode
from manpower_api.exceptions import BadRequest


class EmployeeNotExisted(BadRequest):
    DETAIL = ErrorCode.EMPLOYEE_NOT_EXISTED
