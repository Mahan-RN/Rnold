import secrets
from typing import TypedDict, cast
from urllib.parse import urlencode
import httpx
from src.config import GitAuthSettings

GITHUB_AUTHORIZE_URL = "https://github.com/login/oauth/authorize"
GITHUB_TOKEN_URL = "https://github.com/login/oauth/access_token"
GITHUB_USER_URL = "https://api.github.com/user"
GITHUB_EMAILS_URL = "https://api.github.com/user/emails"

SCOPES = "read:user user:email"


class GithubOAuthError(Exception):
    pass


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
    return secrets.token_urlsafe(32)


def build_authorize_url(state: str) -> str:
    params = {
        "client_id": GitAuthSettings.github_client_id,
        "redirect_uri": GitAuthSettings.github_redirect_uri,
        "scope": SCOPES,
        "state": state,
    }
    return f"{GITHUB_AUTHORIZE_URL}?{urlencode(params)}"


def exchange_code_for_token(code: str) -> str:
    with httpx.Client(timeout=10.0) as client:
        response = client.post(
            GITHUB_TOKEN_URL,
            data={
                "client_id": GitAuthSettings.github_client_id,
                "client_secret": GitAuthSettings.github_client_secret,
                "code": code,
                "redirect_uri": GitAuthSettings.github_redirect_uri,
            },
            headers={"Accept": "application/json"},
        )
    response.raise_for_status()
    payload = cast(GithubTokenResponse, response.json())

    if "error" in payload:
        raise GithubOAuthError(payload.get("error_description", payload["error"]))

    return payload["access_token"]


def fetch_github_profile(access_token: str) -> GithubProfile:
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
