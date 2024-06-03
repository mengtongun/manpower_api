
from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session

from manpower_api.auth.services import verify_basic_auth
from manpower_api.database import get_db

security = HTTPBasic()


def basic_auth(
        credentials: Annotated[HTTPBasicCredentials, Depends(security)], db: Session = Depends(get_db)
):
    return verify_basic_auth(db, credentials.username, credentials.password)
