from sqlalchemy import JSON
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class DictValue(Base):
    value: Mapped[list] = mapped_column(JSON)

    def to_dict(self):
        dicts = super().to_dict()
        return dicts