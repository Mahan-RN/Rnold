from src.routers.auth import router as auth_router
from src.routers.curriculum import router as curriculum_router
from src.routers.evaluation_cases import router as evaluation_cases_router
from src.routers.problems import router as problems_router
from src.routers.submissions import router as submissions_router
from src.routers.topics import router as topics_router
from src.routers.users import router as users_router

__all__ = [
    "auth_router",
    "curriculum_router",
    "evaluation_cases_router",
    "problems_router",
    "submissions_router",
    "topics_router",
    "users_router",
]
