from manpower_api.database import SessionLocal
from manpower_api.employees.models import Employee

db = SessionLocal()

employee_data_list = [
    {
        "nric4Digit": "1234",
        "name": "John Doe",
        "manpowerId": "EMP1001",
        "designation": "Software Engineer",
        "project": "Project X",
        "team": "Development",
        "supervisor": "Jane Smith",
        "joinDate": "2023-01-01",
        "resignDate": None,
    },
    # Add more employee data dictionaries here...
    {
        "nric4Digit": "5678",
        "name": "Alice Lee",
        "manpowerId": "EMP1002",
        "designation": "Marketing Manager",
        "project": "Campaign Y",
        "team": "Marketing",
        "supervisor": "David Kim",
        "joinDate": "2022-06-15",
        "resignDate": "2024-02-29",
    },
    {
        "nric4Digit": "9012",
        "name": "Michael Brown",
        "manpowerId": "EMP1003",
        "designation": "Data Analyst",
        "project": "Data Insights Initiative",
        "team": "Analytics",
        "supervisor": "Charles Williams",
        "joinDate": "2021-12-07",
        "resignDate": None,
    },
    {
        "nric4Digit": "3456",
        "name": "Sarah Jones",
        "manpowerId": "EMP1004",
        "designation": "Human Resources Specialist",
        "project": "Employee Onboarding Program",
        "team": "HR",
        "supervisor": "Emily Gar",
        "joinDate": "2020-05-18",
        "resignDate": None,
    },
    {
        "nric4Digit": "7890",
        "name": "David Miller",
        "manpowerId": "EMP1005",
        "designation": "Sales Manager",
        "project": "Regional Sales Expansion",
        "team": "Sales",
        "supervisor": "Robert Johnson",
        "joinDate": "2023-07-12",
        "resignDate": None,
    },
    {
        "nric4Digit": "1357",
        "name": "Lisa Chang",
        "manpowerId": "EMP1006",
        "designation": "Graphic Designer",
        "project": "Company Branding Refresh",
        "team": "Marketing",
        "supervisor": "Alice Lee",
        "joinDate": "2022-09-21",
        "resignDate": None,
    },
    {
        "nric4Digit": "2468",
        "name": "Daniel Lee",
        "manpowerId": "EMP1007",
        "designation": "Software Developer",
        "project": "Project X (continued from previous data)",
        "team": "Development",
        "supervisor": "John Doe",
        "joinDate": "2023-04-05",
        "resignDate": None,
    },
    {
        "nric4Digit": "8901",
        "name": "Emily Garcia",
        "manpowerId": "EMP1008",
        "designation": "HR Manager",
        "project": "Project Hiring",
        "team": "HR",
        "supervisor": "Jack Paul",
        "joinDate": "2018-02-14",
        "resignDate": None,
    },
    {
        "nric4Digit": "0234",
        "name": "Christopher Williams",
        "manpowerId": "EMP1009",
        "designation": "Accountant",
        "project": "Project Account",
        "team": "Finance",
        "supervisor": "Emily Garcia",
        "joinDate": "2019-11-01",
        "resignDate": None,
    },
    {
        "nric4Digit": "5679",
        "name": "Jessica Robinson",
        "manpowerId": "EMP1010",
        "designation": "Customer Service Representative",
        "project": "Customer 5 Star",
        "team": "Customer Support",
        "supervisor": "David Miller",
        "joinDate": "2024-03-19",
        "resignDate": None,
    },
]

# Insert sample employee data
for employee_data in employee_data_list:
    new_employee = Employee(**employee_data)
    db.add(new_employee)

db.commit()

# Close the session
db.close()


print("Done seed dump data!")
