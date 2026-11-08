import pytest

from sqlalchemy.orm import Session
from src.models import Role
from src.repository import user_repository
from src.exceptions.repository_exceptions import NotFoundError
from datetime import datetime


class TestUserRepository:
    def setup_method(self):
        self.user1 = {
            "github_id": 123_456,
            "github_email": "conan_barbarian@gmail.com",
            "username": "Conan",
        }
        self.user2 = {
            "github_id": 69_696_767,
            "github_email": "ed.brubaker@yahoo.com",
            "username": "Ed Brubaker",
        }
        self.admin1 = {
            "github_id": 111_111,
            "github_email": "meanAdmin@email.ca",
            "username": "admin1",
            "role": Role.ADMIN,
        }

    def test_get_one_no_match(self, db_session: Session):
        with pytest.raises(NotFoundError):
            user_repository.get_one(1, db_session)

    def test_get_all_empty(self, db_session: Session):
        users = user_repository.get_all(db_session)
        assert len(users) == 0

    def test_insert_one_user(self, db_session: Session):
        user_repository.insert_one(**self.user1, session=db_session)
        users = user_repository.get_all(db_session)
        assert len(users) == 1
        user = users[0]
        assert user.github_id == self.user1["github_id"]
        assert user.github_email == self.user1["github_email"]
        assert user.username == self.user1["username"]
        assert user.role == Role.USER
        assert len(user.submissions) == 0
        assert isinstance(user.created_at, datetime)
        assert isinstance(user.last_login, datetime)

    def test_insert_one_admin(self, db_session: Session):
        user_repository.insert_one(**self.admin1, session=db_session)
        users = user_repository.get_all(db_session)
        assert len(users) == 1
        user = users[0]
        assert user.github_id == self.admin1["github_id"]
        assert user.github_email == self.admin1["github_email"]
        assert user.username == self.admin1["username"]
        assert user.role == Role.ADMIN
        assert len(user.submissions) == 0
        assert isinstance(user.created_at, datetime)
        assert isinstance(user.last_login, datetime)

    def test_insert_one_multiple(self, db_session: Session):
        user_repository.insert_one(**self.user1, session=db_session)
        user_repository.insert_one(**self.user2, session=db_session)
        user_repository.insert_one(**self.admin1, session=db_session)
        users = user_repository.get_all(db_session)
        assert len(users) == 3

    def test_update_one_no_match(self, db_session: Session):
        with pytest.raises(NotFoundError):
            user_repository.update_one(1, db_session)

    def test_update_one_match_role(self, db_session: Session):
        user = user_repository.insert_one(**self.user1, session=db_session)
        assert user.username == "Conan"
        assert user.role == Role.USER
        user = user_repository.update_one(
            github_id=self.user1["github_id"], session=db_session, role=Role.ADMIN
        )
        assert user.role == Role.ADMIN

    def test_update_one_match_username(self, db_session: Session):
        user = user_repository.insert_one(**self.user1, session=db_session)
        assert user.username == "Conan"
        assert user.github_email == "conan_barbarian@gmail.com"
        user = user_repository.update_one(
            self.user1["github_id"], db_session, username="ConanBarbarian"
        )
        assert user.github_email == "conan_barbarian@gmail.com"
        assert user.username == "ConanBarbarian"

    def test_update_one_match_role_username(self, db_session: Session):
        user = user_repository.insert_one(**self.user1, session=db_session)
        assert user.username == "Conan"
        assert user.role == Role.USER
        user = user_repository.update_one(
            github_id=self.user1["github_id"],
            session=db_session,
            username="ConanBarbarian",
            role=Role.ADMIN,
        )
        assert user.role == Role.ADMIN
        assert user.username == "ConanBarbarian"

    def test_delete_one_no_match(self, db_session: Session):
        with pytest.raises(NotFoundError):
            user_repository.delete_one(123456, db_session)

    def test_delete_one_match(self, db_session: Session):
        user_repository.insert_one(**self.user1, session=db_session)
        assert len(user_repository.get_all(db_session)) == 1
        user_repository.delete_one(self.user1["github_id"], db_session)
        assert len(user_repository.get_all(db_session)) == 0
