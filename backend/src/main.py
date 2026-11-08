from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

import src.models  # noqa: F401
from src.config import git_auth_settings
from src.database import Base, engine
from src.routers import (
    auth_router,
    curriculum_router,
    problems_router,
    submissions_router,
    test_cases_router,
    topics_router,
    users_router,
)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    # Create tables
    Base.metadata.create_all(bind=engine)
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
