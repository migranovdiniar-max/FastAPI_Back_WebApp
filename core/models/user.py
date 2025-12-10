from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .post import Post


class User(Base):
    name: Mapped[str] = mapped_column(String(32), unique=True)
    posts = Mapped[list['Post']] = mapped_column(back_populates='users')