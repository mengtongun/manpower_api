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
Warning: In case got error cannot get env please restart terminal

### Seed Dump Data for Testing
```
python seed.py
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

## How to Run Frontend with Backend (MacOS and Linux Only):

### Clone Frontend Project
```
cd https://github.com/mengtongun/manpower_app.git
```
### Setup and Install Dependencies
```
cd manpower_app

flutter pub get
```
### Build Flutter Web
```
fluter build web
```

### Replace Static Web File in Backend)
```
cd ..
rm -rf web && cp manpower_app/build/web web
```
### Run in Local
```
uvicorn manpower_api.main:app --port=8000
```

### Project Structure
```
manpower_api
├── manpower_api
│   ├── auth
│   │   ├── router.py
│   │   ├── schemas.py  # pydantic models
│   │   ├── models.py  # db models
│   │   ├── config.py  # local configs
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   ├── security.py
│   │   ├── service.py
│   └── employee
│   │   ├── router.py
│   │   ├── schemas.py
│   │   ├── models.py
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   ├── service.py
│   ├── config.py  # global configs
│   ├── models.py  # global models
│   ├── exceptions.py  # global exceptions
│   ├── database.py  # db connection related stuff
│   └── main.py
├── web # static build file from flutter web 
│   └── index.html
│   └── ...
├── requirements.txt
├── README.md
├── .env
├── .gitignore
```
Details at

https://fastapi.tiangolo.com/tutorial/

and

https://fastapi.tiangolo.com/tutorial/sql-databases/
