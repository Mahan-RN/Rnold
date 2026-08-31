from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Topic(Base):
    __tablename__ = "topics"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str]
    sort_order: Mapped[int | None] = mapped_column(unique=True)

    def __repr__(self) -> str:
        return f"""
        Topic(
        id: {self.id},
        name: '{self.name}',
        description: '{self.description}',
        sort_order: {self.sort_order}
        )"""
