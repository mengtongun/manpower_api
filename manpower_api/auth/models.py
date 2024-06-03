from sqlalchemy import Boolean, Column, Integer, String

from manpower_api.database import DB_TABLE_PREFIX, Base


class User(Base):
    __tablename__ = f"{DB_TABLE_PREFIX}.users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    username = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)
