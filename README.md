# Manpower API

## Purpose

### Technical Test for Developer From PylonAI

## Requirements

#### Python Version >= 3.12

Recommend to create a virtual python environment

#### Install OBDC Driver Version 17

https://learn.microsoft.com/en-us/sql/connect/odbc/microsoft-odbc-driver-for-sql-server?view=sql-server-ver16

#### Install Dependencies

```
python install -r requirement.txt
```

#### Update Environment Variable

Copy .env.example

```
cp .env.example .env
```

and update

```
DB_USERNAME=sa
DB_PASSWORD=pw
DB_SERVER=localhost
DB_NAME=test
DB_TABLE_PREFIX=test
```

### How to run:

To launch uvicorn:

```
uvicorn manpower_api.main:app --reload --port=8000
```

### Access Flutter Web Built

```
http://localhost:8000
```

### API Documentation Swagger

Then load the fancy interactive docs page at

```
http://localhost:8000/docs
```

Details at

https://fastapi.tiangolo.com/tutorial/

and

https://fastapi.tiangolo.com/tutorial/sql-databases/
