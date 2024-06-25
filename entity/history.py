from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from . import db
from .base import Base


class History(Base):
    create_time: Mapped[datetime] = mapped_column(default=db.func.current_timestamp())
    validator = relationship("Validator")
    validator_id: Mapped[str] = mapped_column(ForeignKey("validator.id"))

    def to_dict(self):
        dicts = super().to_dict()
        dicts['create_time'] = self.create_time
        dicts['validator_id'] = self.validator_id
        return dicts