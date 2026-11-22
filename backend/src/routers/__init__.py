from src.routers.auth import router as auth_router
from src.routers.curriculum import router as curriculum_router
from src.routers.problems import router as problems_router
from src.routers.submissions import router as submissions_router
from src.routers.test_cases import router as test_cases_router
from src.routers.topics import router as topics_router
from src.routers.users import router as users_router

__all__ = [
    "auth_router",
    "curriculum_router",
    "problems_router",
    "submissions_router",
    "test_cases_router",
    "topics_router",
    "users_router",
]
