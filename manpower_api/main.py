import time

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.sql import text

from manpower_api.auth.router import router as auth_router
from manpower_api.database import Base, engine
from manpower_api.employees.router import router as employees_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Manpower API",
    description="For technical test with PylonAI",
    version="1.0.0",
    swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})


# Allow Client Domains
origins = ["http://localhost:8001"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "PATCH", "POST"],
    allow_headers=["Authorization", "Accept", "User-Agent", "Content-Type"],
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/health", tags=["Health"])
async def health() -> dict[str, str]:
    try:
        engine.connect().execute(text("SELECT 1")).first()
        return {"db": "up"}
    except Exception as e:
        print(e)
        return {"db": "down"}

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(employees_router, prefix="/v1/api", tags=["Employees"])

app.mount("/", StaticFiles(directory="web", html=True), name="web")
