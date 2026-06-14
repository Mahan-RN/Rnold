from datetime import datetime as dt


class User:
    def __init__(
        self, git_email: str, git_id: int, git_username: str, created_at: dt
    ) -> None:
        self.git_id: int = git_id
        self.git_email: str = git_email
        self.git_username: str = git_username
        self.created_at: dt = created_at
        self.last_seen: dt = created_at

    @property
    def git_id(self) -> int:
        return self._git_id

    @git_id.setter
    def git_id(self, git_id: int) -> None:
        self._git_id = git_id

    @property
    def git_email(self) -> str:
        return self._git_email

    @git_email.setter
    def git_email(self, git_email: str) -> None:
        self._git_email = git_email

    @property
    def git_username(self) -> str:
        return self._git_username

    @git_username.setter
    def git_username(self, git_username: str) -> None:
        self._git_username = git_username

    @property
    def created_at(self) -> dt:
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: dt) -> None:
        self._created_at = created_at

    @property
    def last_seen(self) -> dt:
        return self._last_seen

    @last_seen.setter
    def last_seen(self, last_seen: dt) -> None:
        self._last_seen = last_seen
