from typing import TypedDict

import pytest
from sqlalchemy.orm import Session

from src.exceptions.user_exceptions import (
    LastAdminDeletionError,
    UserConflictError,
    UserNotFoundError,
)
from src.models.user import Role
from src.services import user_services
from tests.factory_types import UserMaker


class UserData(TypedDict):
    github_id: int
    github_email: str
    username: str
    role: Role


class TestUserServices:
    def setup_method(self) -> None:
        self.user1: UserData = {
            "github_id": 123,
            "github_email": "user1@email.com",
            "username": "user1",
            "role": Role.USER,
        }

        self.user2: UserData = {
            "github_id": 456,
            "github_email": "user2@email.com",
            "username": "user2",
            "role": Role.USER,
        }

        self.admin1: UserData = {
            "github_id": 789,
            "github_email": "admin1@email.com",
            "username": "admin1",
            "role": Role.ADMIN,
        }

        self.admin2: UserData = {
            "github_id": 111,
            "github_email": "admin2@email.com",
            "username": "admin2",
            "role": Role.ADMIN,
        }

    def test_get_one_no_match(self, db_session: Session) -> None:
        with pytest.raises(UserNotFoundError):
            user_services.get_one(123, db_session)

    def test_get_one_match(self, make_user: UserMaker, db_session: Session) -> None:
        make_user()
        make_user(github_id=-2, username="user 2")
        result = user_services.get_one(-1, db_session)
        assert result.github_id == -1
        assert result.username == "user 1"

    def test_get_all_empty(self, db_session: Session) -> None:
        users = user_services.get_all(db_session)
        assert len(users) == 0

    def test_get_all(self, make_user: UserMaker, db_session: Session) -> None:
        make_user()
        make_user(github_id=-2, username="user 2")
        result = user_services.get_all(db_session)
        assert len(result) == 2
        assert result[0].github_id == -1
        assert result[1].github_id == -2

    def test_insert_one_user(self, db_session: Session) -> None:
        user_services.insert_one(**self.user1, session=db_session)

        user_result = user_services.get_one(self.user1["github_id"], db_session)

        assert user_result is not None
        assert user_result.role == Role.USER

    def test_insert_one_admin(self, db_session: Session) -> None:
        user_services.insert_one(**self.admin1, session=db_session)

        admin_result = user_services.get_one(self.admin1["github_id"], db_session)

        assert admin_result is not None
        assert admin_result.role == Role.ADMIN

    def test_insert_one_multiple(self, db_session: Session) -> None:
        user_services.insert_one(**self.user1, session=db_session)
        user_services.insert_one(**self.user2, session=db_session)
        user_services.insert_one(**self.admin1, session=db_session)
        users = user_services.get_all(db_session)
        assert len(users) == 3

    def test_insert_one_duplicate_github_id(self, db_session: Session) -> None:
        user_services.insert_one(**self.user1, session=db_session)
        self.user2["github_id"] = self.user1["github_id"]
        with pytest.raises(UserConflictError):
            user_services.insert_one(**self.user2, session=db_session)

    def test_update_one_no_match(self, db_session: Session) -> None:
        with pytest.raises(UserNotFoundError):
            user_services.update_one(5000, db_session, None, "new_user")

    def test_updated_one_match_username(self, db_session: Session) -> None:
        user_services.insert_one(**self.user1, session=db_session)

        result = user_services.update_one(
            self.user1["github_id"], db_session, None, "new_username"
        )

        assert result.username == "new_username"

    def test_update_one_match_role(self, db_session: Session) -> None:
        user_services.insert_one(**self.user1, session=db_session)

        before = user_services.get_one(self.user1["github_id"], db_session)

        assert before.role == Role.USER

        after = user_services.update_one(
            self.user1["github_id"], db_session, Role.ADMIN, None
        )

        assert after.role == Role.ADMIN

    def test_delete_one_no_match(self, db_session: Session) -> None:
        with pytest.raises(UserNotFoundError):
            user_services.delete_one(111, db_session)

    def test_delete_match_user(self, db_session: Session) -> None:
        user_services.insert_one(**self.user1, session=db_session)

        result = user_services.get_one(self.user1["github_id"], db_session)

        assert result is not None

        user_services.delete_one(self.user1["github_id"], db_session)

        with pytest.raises(UserNotFoundError):
            user_services.get_one(self.user1["github_id"], db_session)

    def test_delete_match_admin_no_error(self, db_session: Session) -> None:
        user_services.insert_one(**self.admin1, session=db_session)
        user_services.insert_one(**self.admin2, session=db_session)

        result = user_services.get_one(self.admin2["github_id"], db_session)

        assert result is not None

        user_services.delete_one(self.admin2["github_id"], db_session)

        with pytest.raises(UserNotFoundError):
            user_services.get_one(self.admin2["github_id"], db_session)

    def test_delete_match_admin_error(self, db_session: Session) -> None:
        user_services.insert_one(**self.admin1, session=db_session)
        user_services.insert_one(**self.user1, session=db_session)

        result = user_services.get_one(self.admin1["github_id"], db_session)

        assert result is not None

        with pytest.raises(LastAdminDeletionError):
            user_services.delete_one(self.admin1["github_id"], db_session)
