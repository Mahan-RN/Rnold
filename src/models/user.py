from src.database import Base
from datetime import datetime
from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from enum import Enum, auto


class Role(Enum):
    USER = auto()
    ADMIN = auto()


class User(Base):
    __tablename__ = "users"

    github_id: Mapped[int] = mapped_column(primary_key=True)
    github_email: Mapped[str]
    username: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    last_login: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    role: Mapped[int] = mapped_column(default=Role.USER)

    def __repr__(self) -> str:
        return f"""
            User(
            github_id: {self.github_id},
            github_email: '{self.github_email}',
            username: '{self.username}',
            created_at: '{self.created_at}',
            last_login: '{self.last_login}',
            role: {self.role}
            )
            """
