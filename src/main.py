from fastapi import FastAPI
from src.routers import users_router
from contextlib import asynccontextmanager
from src.database import Base, engine
from collections.abc import AsyncIterator
import src.models  # noqa: F401


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    # Create tables
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(users_router)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hllo World"}


# def main() -> None:
#     print("Hello from rnold!")


# if __name__ == "__main__":
#     main()
