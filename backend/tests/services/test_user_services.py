from src.schemas.user import PostUser
from sqlalchemy.orm import Session
from src.exceptions.user_exceptions import UserNotFoundError, LastAdminDeletionError
from src.services import user_services
from src.models.user import Role
import pytest


class TestUserServices:
    def setup_method(self):
        self.post_user1 = PostUser(
            github_id=123, github_email="user1@email.com", username="user1"
        )
        self.post_user2 = PostUser(
            github_id=456, github_email="user1@email.com", username="user2"
        )
        self.post_admin1 = PostUser(
            github_id=789,
            github_email="admin1@email.com",
            username="admin1",
            role=Role.ADMIN,
        )
        self.post_admin2 = PostUser(
            github_id=111,
            github_email="admin2@email.com",
            username="admin2",
            role=Role.ADMIN,
        )

    def test_get_one_no_match(self, db_session: Session):
        with pytest.raises(UserNotFoundError):
            user_services.get_one(123, db_session)

    def test_insert_one_user(self, db_session: Session):
        user_services.insert_one(self.post_user1, db_session)
        user_result = user_services.get_one(self.post_user1.github_id, db_session)
        assert user_result is not None
        assert user_result.role == Role.USER

    def test_insert_one_admin(self, db_session: Session):
        user_services.insert_one(self.post_admin1, db_session)
        admin_result = user_services.get_one(self.post_admin1.github_id, db_session)
        assert admin_result is not None
        assert admin_result.role == Role.ADMIN

    def test_update_one_no_match(self, db_session: Session):
        with pytest.raises(UserNotFoundError):
            user_services.update_one(5000, db_session, None, "new_user")

    def test_updated_one_match_username(self, db_session: Session):
        user_services.insert_one(self.post_user1, db_session)
        result = user_services.update_one(
            self.post_user1.github_id, db_session, None, "new_username"
        )
        assert result.username == "new_username"

    def test_update_one_match_role(self, db_session: Session):
        user_services.insert_one(self.post_user1, db_session)
        before = user_services.get_one(self.post_user1.github_id, db_session)
        assert before.role == Role.USER
        after = user_services.update_one(
            self.post_user1.github_id, db_session, Role.ADMIN, None
        )
        assert after.role == Role.ADMIN

    def test_delete_one_no_match(self, db_session: Session):
        with pytest.raises(UserNotFoundError):
            user_services.delete_one(111, db_session)

    def test_delete_match_user(self, db_session: Session):
        user_services.insert_one(self.post_user1, db_session)
        result = user_services.get_one(self.post_user1.github_id, db_session)
        assert result is not None
        user_services.delete_one(self.post_user1.github_id, db_session)
        with pytest.raises(UserNotFoundError):
            user_services.get_one(self.post_user1.github_id, db_session)

    def test_delete_match_admin_no_error(self, db_session: Session):
        user_services.insert_one(self.post_admin1, db_session)
        user_services.insert_one(self.post_admin2, db_session)
        result = user_services.get_one(self.post_admin2.github_id, db_session)
        assert result is not None
        user_services.delete_one(self.post_admin2.github_id, db_session)
        with pytest.raises(UserNotFoundError):
            user_services.get_one(self.post_admin2.github_id, db_session)

    def test_delete_match_admin_error(self, db_session: Session):
        user_services.insert_one(self.post_admin1, db_session)
        user_services.insert_one(self.post_user1, db_session)
        result = user_services.get_one(self.post_admin1.github_id, db_session)
        assert result is not None
        with pytest.raises(LastAdminDeletionError):
            user_services.delete_one(self.post_admin1.github_id, db_session)
