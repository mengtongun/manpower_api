import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DB_USERNAME=os.environ['DB_USERNAME']
DB_PASSWORD=os.environ['DB_PASSWORD']
DB_SERVER=os.environ['DB_SERVER']
DB_NAME=os.environ['DB_NAME']
DB_TABLE_PREFIX=os.environ['DB_TABLE_PREFIX']

DATABASE_URL = f"mssql+pyodbc://{DB_USERNAME}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}?driver=ODBC Driver 17 for SQL Server"

engine = create_engine(
    DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 

