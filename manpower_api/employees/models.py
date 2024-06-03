from sqlalchemy import DATE, NVARCHAR, Column, Integer

from manpower_api.database import DB_TABLE_PREFIX, Base


class Employee(Base):
    __tablename__ = f"{DB_TABLE_PREFIX}.manpowers"

    id = Column(Integer, primary_key=True, index=True)
    nric4Digit = Column(NVARCHAR(4), nullable=False, unique=True)
    name = Column(NVARCHAR(255), comment="Employee's name.")
    manpowerId = Column(NVARCHAR(255), comment="Employee's ID")
    designation = Column(NVARCHAR(255), comment="Employee's job title.")
    project = Column(
        NVARCHAR(255), comment="Current project assigned to the employee.")
    team = Column(
        NVARCHAR(255), comment="Team within the organization the employee belongs to.")
    supervisor = Column(
        NVARCHAR(255), comment="Supervisor's name responsible for the employee.")
    joinDate = Column(
        DATE, comment="The date the employee joined the company.")
    resignDate = Column(
        DATE, comment="The date the employee left the company, if applicable.")
