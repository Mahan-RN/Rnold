from typing import TypedDict

import pytest
from sqlalchemy.orm import Session

from src.exceptions.topic_exceptions import TopicConflictError, TopicNotFoundError
from src.services import topic_services


class TopicData(TypedDict):
    name: str
    description: str
    sort_order: int


class TestTopicServices:
    def setup_method(self) -> None:
        self.topic_1_dict: TopicData = {
            "name": "Recursion",
            "description": "Just trust the natural recursion",
            "sort_order": 100,
        }
        self.topic_2_dict: TopicData = {
            "name": "Control flow",
            "description": "some string",
            "sort_order": 200,
        }

    def test_get_one_no_match(self, db_session: Session) -> None:
        with pytest.raises(TopicNotFoundError):
            topic_services.get_one(1, db_session)

    def test_insert_one(self, db_session: Session) -> None:
        result = topic_services.insert_one(**self.topic_1_dict, session=db_session)
        assert result.id == 1
        assert result.name == self.topic_1_dict["name"]
        assert result.description == self.topic_1_dict["description"]
        assert result.sort_order == self.topic_1_dict["sort_order"]

    def test_update_one_no_match(self, db_session: Session) -> None:
        with pytest.raises(TopicNotFoundError):
            topic_services.update_one(id=1, session=db_session)

    def test_update_one_duplicate_name(self, db_session: Session) -> None:
        topic_services.insert_one(**self.topic_1_dict, session=db_session)
        self.topic_2_dict["name"] = self.topic_1_dict["name"]
        with pytest.raises(TopicConflictError):
            topic_services.insert_one(**self.topic_2_dict, session=db_session)

    def test_update_one_match_name(self, db_session: Session) -> None:
        insert_result = topic_services.insert_one(
            **self.topic_1_dict, session=db_session
        )
        assert insert_result.name == self.topic_1_dict["name"]
        update_result = topic_services.update_one(
            id=insert_result.id, name="new name", session=db_session
        )
        assert update_result.name == "new name"
        assert update_result.id == 1
        assert update_result.description == self.topic_1_dict["description"]
        assert update_result.sort_order == self.topic_1_dict["sort_order"]

    def test_update_one_match_description(self, db_session: Session) -> None:
        insert_result = topic_services.insert_one(
            **self.topic_1_dict, session=db_session
        )
        assert insert_result.name == self.topic_1_dict["name"]
        update_result = topic_services.update_one(
            id=insert_result.id, description="new description", session=db_session
        )
        assert update_result.description == "new description"
        assert update_result.id == 1
        assert update_result.name == self.topic_1_dict["name"]
        assert update_result.sort_order == self.topic_1_dict["sort_order"]

    def test_update_one_match_sort_order(self, db_session: Session) -> None:
        insert_result = topic_services.insert_one(
            **self.topic_1_dict, session=db_session
        )
        assert insert_result.name == self.topic_1_dict["name"]
        update_result = topic_services.update_one(
            id=insert_result.id, sort_order=500, session=db_session
        )
        assert update_result.sort_order == 500
        assert update_result.id == 1
        assert update_result.name == self.topic_1_dict["name"]
        assert update_result.description == self.topic_1_dict["description"]

    def test_update_one_match_all(self, db_session: Session) -> None:
        insert_result = topic_services.insert_one(
            **self.topic_1_dict, session=db_session
        )
        assert insert_result.name == self.topic_1_dict["name"]
        update_result = topic_services.update_one(
            id=insert_result.id,
            name="new name",
            description="new description",
            sort_order=500,
            session=db_session,
        )
        assert update_result.id == 1
        assert update_result.name == "new name"
        assert update_result.description == "new description"
        assert update_result.sort_order == 500

    def test_delete_one_no_match(self, db_session: Session) -> None:
        topic_services.insert_one(**self.topic_1_dict, session=db_session)
        with pytest.raises(TopicNotFoundError):
            topic_services.delete_one(2, db_session)
        get_result = topic_services.get_one(1, db_session)
        assert get_result is not None

    def test_delete_one_match(self, db_session: Session) -> None:
        topic_services.insert_one(**self.topic_1_dict, session=db_session)
        topic_services.delete_one(1, db_session)
        with pytest.raises(TopicNotFoundError):
            topic_services.get_one(1, db_session)
