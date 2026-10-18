import secrets
from datetime import datetime, timezone
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.user import User
from src.services import github_oauth
from src.services.github_oauth import GithubOAuthError, GithubProfile
from src.dependency import logout

router = APIRouter(prefix="/auth/github", tags=["auth"])

DbSession = Annotated[Session, Depends(get_db)]


@router.get("/login")
def github_login(request: Request) -> RedirectResponse:
    state = github_oauth.generate_state()
    request.session["oauth_state"] = state
    return RedirectResponse(github_oauth.build_authorize_url(state))


@router.get("/callback")
def github_callback(
    request: Request,
    code: str,
    state: str,
    db: DbSession,
) -> RedirectResponse:
    expected_state = request.session.pop("oauth_state", None)
    if expected_state is None or not secrets.compare_digest(expected_state, state):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "invalid oauth state")

    try:
        access_token = github_oauth.exchange_code_for_token(code)
        profile = github_oauth.fetch_github_profile(access_token)
    except GithubOAuthError as exc:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(exc)) from exc

    user = _get_or_create_user(db, profile)
    request.session["github_id"] = user.github_id

    return RedirectResponse("/api/", status_code=status.HTTP_303_SEE_OTHER)


@router.post("/logout")
def github_logout(request: Request) -> Response:
    logout(request)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def _get_or_create_user(db: DbSession, profile: GithubProfile) -> User:
    user: User | None = db.get(User, profile["github_id"])

    if user is None:
        user = User(
            github_id=profile["github_id"],
            github_email=profile["email"],
            username=profile["username"],
        )
        db.add(user)
    else:
        user.github_email = profile["email"]
        user.username = profile["username"]
        user.last_login = datetime.now(timezone.utc)

    db.commit()
    db.refresh(user)
    return user
