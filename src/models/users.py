from sqlalchemy.orm import Mapped, mapped_column
from src.db.db import Base
from src.schemas.users import UserSchema


class UsersModel(Base):
    __tablename__ = 'users'

    id : Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    points: Mapped[int] = mapped_column(default=0)

    def to_read_model(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            username=self.username,
            email=self.email,
            password=self.password,
            points=self.points
        )