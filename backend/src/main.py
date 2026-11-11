from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

import src.models  # pyright: ignore[reportUnusedImport] # noqa: F401
from src.config import app_settings, git_auth_settings
from src.database import Base, SessionLocal, engine
from src.routers import (
    auth_router,
    curriculum_router,
    problems_router,
    submissions_router,
    test_cases_router,
    topics_router,
    users_router,
)
from src.services.problem_parser import load_problem_data


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    # Create tables
    Base.metadata.create_all(bind=engine)
    if app_settings.load_problems_on_startup:
        with SessionLocal() as db_session:
            load_problem_data(db_session, app_settings.problems_dir)
    yield


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    SessionMiddleware,
    secret_key=git_auth_settings.session_secret_key.get_secret_value(),
    same_site="lax",
    max_age=30 * 60,
    # Set to True in production
    https_only=False,
)

app.include_router(users_router, prefix="/api")
app.include_router(auth_router, prefix="/api")
app.include_router(curriculum_router, prefix="/api")
app.include_router(problems_router, prefix="/api")
app.include_router(submissions_router, prefix="/api")
app.include_router(topics_router, prefix="/api")
app.include_router(test_cases_router, prefix="/api")


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hllo World"}
