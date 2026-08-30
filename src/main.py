from fastapi import FastAPI
from src.routers import users_router


app = FastAPI()

app.include_router(users_router)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hllo World"}


# def main() -> None:
#     print("Hello from rnold!")


# if __name__ == "__main__":
#     main()
