# Manpower API

## Purpose

### Technical Test for Developer From PylonAI

## Requirements

### Recommended (Docker)

- **Docker** ≥ 20.10
- **Docker Compose** ≥ 2.0 (comes bundled with recent Docker Desktop versions)

Running in containers means you _do not_ need to install Python, database drivers or system packages locally.

### If you prefer to run natively

- **Python** ≥ 3.12 — create a virtual environment.
- **Microsoft ODBC Driver 18** for SQL Server — [installation guide](https://learn.microsoft.com/en-us/sql/connect/odbc/microsoft-odbc-driver-for-sql-server?view=sql-server-ver16).
- Install Python dependencies: `pip install -r requirements.txt`.

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

### Manual run (without Docker – optional)

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
git clone https://github.com/mengtongun/manpower_app.git
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

## Features

- **Authentication:** Basic HTTP authentication with secure password hashing (bcrypt).
- **Employee Management:**
  - List employees with pagination: `GET /v1/api/employees`
  - Update employee details: `PATCH /v1/api/employees/{manpower_id}`
  - Export employees as CSV: `GET /v1/api/employees/csv`
- **Health Check:** `GET /health` verifies application ↔ database connectivity.
- **Interactive API Docs:** Swagger UI available at `http://localhost:8000/docs`.
- **Static Front-End:** Compiled Flutter web application served from the root path `/`.

## Technology Stack

| Layer            | Technology                    |
| ---------------- | ----------------------------- |
| Language         | Python ≥ 3.12                 |
| Web Framework    | FastAPI                       |
| ASGI Server      | Uvicorn                       |
| ORM              | SQLAlchemy                    |
| Database Driver  | pyodbc (Microsoft SQL Server) |
| Authentication   | bcrypt + HTTP Basic Auth      |
| Data Utilities   | pandas (CSV export)           |
| Containerisation | Docker & Docker Compose       |
| Front-End        | Flutter Web (static files)    |

## Local Development

### Option 1 – Docker (recommended)

```bash
cp .env.example .env   # customise credentials if needed
make init-db
make seed
make build
make up
```

The API will now be reachable at `http://localhost:8000`.

#### Makefile shortcuts

| Command        | Description                                                                                     |
| -------------- | ----------------------------------------------------------------------------------------------- |
| `make build`   | Build (or rebuild) the Docker images. Run this after updating the Dockerfile or dependencies.   |
| `make up`      | Start all containers in detached mode.                                                          |
| `make down`    | Stop and remove containers, networks and **volumes** (drops DB data).                           |
| `make init-db` | Create the database schema inside the SQL Server container. Run once after the first `make up`. |
| `make seed`    | Execute `seed.py` inside the API container to populate sample data.                             |
| `make logs`    | Follow logs from all running containers (`Ctrl+C` to stop).                                     |
| `make ps`      | Show current container status.                                                                  |

> 🔄 **Quick rebuild cycle**: when you change backend code or dependencies run `make build && make up` to recreate the `manpower_api` image and restart the stack.

> 🧹 **Start from scratch**: `make down` removes containers **and** the persisted `mssql_data` volume, giving you a clean slate.

### Option 2 – Manual (native Python)

Create a virtual environment, install dependencies and run the server:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn manpower_api.main:app --reload --port 8000
```

## Environment Variables

| Name              | Description                          | Default     |
| ----------------- | ------------------------------------ | ----------- |
| `DB_USERNAME`     | Database username                    | `sa`        |
| `DB_PASSWORD`     | Database password                    | `pw`        |
| `DB_SERVER`       | Hostname / IP of SQL Server          | `localhost` |
| `DB_NAME`         | Database name                        | `test`      |
| `DB_TABLE_PREFIX` | Prefix prepended to every table name | `test`      |

## Seed Sample Data

Populate the database with sample records for quick testing:

```bash
python seed.py
```

---
