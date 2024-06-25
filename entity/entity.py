from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from . import db
from .base import Base


class Entity(Base):
    validator = relationship("Validator")
    validator_id: Mapped[str] = mapped_column(ForeignKey("validator.id"))


    def to_dict(self):
        dicts = super().to_dict()
        dicts['validator_id'] = self.validator_id
        return dicts