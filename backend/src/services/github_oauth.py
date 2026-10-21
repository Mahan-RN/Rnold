from datetime import datetime, timezone
import secrets
from typing import TypedDict, cast
from urllib.parse import urlencode

import httpx
from sqlalchemy.orm import Session
from src.models.user import User
from src.repository import user_repository
from src.config import git_auth_settings
from src.exceptions.github_oauth_exceptions import GithubOAuthError

GITHUB_AUTHORIZE_URL = "https://github.com/login/oauth/authorize"
GITHUB_TOKEN_URL = "https://github.com/login/oauth/access_token"
GITHUB_USER_URL = "https://api.github.com/user"
GITHUB_EMAILS_URL = "https://api.github.com/user/emails"

SCOPES = "read:user user:email"


class GithubTokenResponse(TypedDict, total=False):
    access_token: str
    error: str
    error_description: str


class GithubUserResponse(TypedDict):
    id: int
    login: str
    email: str | None


class GithubEmailEntry(TypedDict):
    email: str
    primary: bool
    verified: bool


class GithubProfile(TypedDict):
    github_id: int
    username: str
    email: str


def generate_state() -> str:
    """Generates `state` query parameter for Github authorization request to help
       prevent cross-site request forgery attacks

    Returns:
        str: 32-bit random string encoded in base64 format
    """
    return secrets.token_urlsafe(32)


def build_authorize_url(state: str) -> str:
    """Builds the authorization URL required to request a user's Github
       identity.

    Args:
        state (str): unguessable random string to be used for the state query parameter

    Returns:
        str: Github authorization URL, with all the required query parameters
    """
    query_params = {
        "client_id": git_auth_settings.github_client_id,
        "redirect_uri": git_auth_settings.github_redirect_uri,
        "scope": SCOPES,
        "state": state,
    }
    return f"{GITHUB_AUTHORIZE_URL}?{urlencode(query_params)}"


def exchange_code_for_token(code: str) -> str:
    """Exchanges code provided by Github authorization server to the callback
       endpoint for an access token

    Args:
        code (str): code provided by Github authorization server

    Raises:
        GithubOAuthError: thrown if the exchange fails

    Returns:
        str: user's Github profile access token
    """
    with httpx.Client(timeout=10.0) as client:
        response = client.post(
            GITHUB_TOKEN_URL,
            data={
                "client_id": git_auth_settings.github_client_id,
                "client_secret": git_auth_settings.github_client_secret.get_secret_value(),
                "code": code,
                "redirect_uri": git_auth_settings.github_redirect_uri,
            },
            headers={"Accept": "application/json"},
        )
    response.raise_for_status()
    payload = cast(GithubTokenResponse, response.json())

    if "error" in payload:
        raise GithubOAuthError(payload.get("error_description", payload["error"]))

    return payload["access_token"]


def fetch_github_profile(access_token: str) -> GithubProfile:
    """Uses user's Github profile access token to retrieve user's profile data

    Args:
        access_token (str): user's Github profile access token

    Returns:
        GithubProfile: user's Github ID, primary email, & username as a dictionary
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.github+json",
    }
    with httpx.Client(timeout=10.0) as client:
        user_response = client.get(GITHUB_USER_URL, headers=headers)
        user_response.raise_for_status()
        user_payload = cast(GithubUserResponse, user_response.json())

        email = user_payload["email"]
        if email is None:
            emails_response = client.get(GITHUB_EMAILS_URL, headers=headers)
            emails_response.raise_for_status()
            entries = cast(list[GithubEmailEntry], emails_response.json())
            email = _select_primary_email(entries)

    return GithubProfile(
        github_id=user_payload["id"],
        username=user_payload["login"],
        email=email,
    )


def _select_primary_email(entries: list[GithubEmailEntry]) -> str:
    for entry in entries:
        if entry["primary"] and entry["verified"]:
            return entry["email"]
    raise GithubOAuthError("no verified primary email on this GitHub account")


def get_or_create_user(profile: GithubProfile, session: Session) -> User:
    user: User | None = user_repository.get_one(profile["github_id"], session)
    if user is None:
        user = user_repository.insert_one(
            github_id=profile["github_id"],
            github_email=profile["email"],
            username=profile["username"],
            session=session,
        )
    else:
        user.last_login = datetime.now(timezone.utc)

    return user
