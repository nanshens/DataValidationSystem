from sqlalchemy.orm import Mapped, mapped_column
from . import db
from .base import Base


class Validator(Base):
    pass

    def to_dict(self):
        dicts = super().to_dict()
        return dicts