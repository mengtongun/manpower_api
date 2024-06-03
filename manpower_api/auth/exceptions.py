
from manpower_api.auth.constants import ErrorCode
from manpower_api.exceptions import BadRequest, NotAuthenticated


class AuthRequired(NotAuthenticated):
    DETAIL = ErrorCode.AUTHENTICATION_REQUIRED


class InvalidCredentials(BadRequest):
    DETAIL = ErrorCode.INVALID_CREDENTIALS


class EmailTaken(BadRequest):
    DETAIL = ErrorCode.EMAIL_TAKEN


class UsernameTaken(BadRequest):
    DETAIL = ErrorCode.USERNAME_TAKEN
