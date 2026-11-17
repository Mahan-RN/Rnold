from pathlib import Path

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class GitAuthSettings(BaseSettings):
    github_client_id: str
    github_client_secret: SecretStr
    github_redirect_uri: str
    session_secret_key: SecretStr

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


git_auth_settings = GitAuthSettings()  # pyright: ignore[reportCallIssue]


class AppSettings(BaseSettings):
    topics_dir: Path
    problems_dir: Path
    load_topics_on_startup: bool = True
    load_problems_on_startup: bool = True

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


app_settings = AppSettings()  # pyright: ignore[reportCallIssue]


class Settings(BaseSettings):
    database_url: str = Field(repr=False)

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )
