import logging
import os

from sqlalchemy import create_engine, text
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import declarative_base, sessionmaker

DB_USERNAME = os.environ['DB_USERNAME']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_SERVER = os.environ['DB_SERVER']
DB_PORT = os.environ.get('DB_PORT', '1433')  # Default port for SQL Server
DB_NAME = os.environ['DB_NAME']
DB_TABLE_PREFIX = os.environ['DB_TABLE_PREFIX']

logger = logging.getLogger(__name__)


# Create the main database connection
connect_url = URL.create(
    'mssql+pyodbc',
    username=DB_USERNAME,
    password=DB_PASSWORD,
    host=DB_SERVER,
    port=DB_PORT,
    database=DB_NAME,
    query=dict(driver='ODBC Driver 18 for SQL Server', TrustServerCertificate='yes'))


engine = create_engine(
    connect_url,
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
