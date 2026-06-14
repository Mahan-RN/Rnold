import pytest
from src.models.user import User
from datetime import datetime


class TestUser:

    @pytest.fixture(autouse=True)
    def before_each(self) -> None:
        dt: datetime = datetime(2026, 6, 13, 10, 53, 0)
        self.user1: User = User(
            git_email="myemail@gmail.com",
            git_id=12345678,
            git_username="generic_user",
            created_at=dt,
        )

    def test_constructor(self) -> None:
        assert self.user1.git_email == "myemail@gmail.com"
        assert self.user1.git_id == 12345678
        assert self.user1.git_username == "generic_user"
        assert self.user1.created_at.year == 2026
        assert self.user1.created_at.month == 6
        assert self.user1.created_at.day == 13
        assert self.user1.created_at.hour == 10
        assert self.user1.created_at.second == 0
