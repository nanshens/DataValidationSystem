from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from . import db
from .base import Base
from datetime import datetime

class Executor(Base):
    execute_time: Mapped[datetime] = mapped_column(default=db.func.current_timestamp())
    validator = relationship("Validator")
    validator_id: Mapped[str] = mapped_column(ForeignKey("validator.id"))


    def to_dict(self):
        dicts = super().to_dict()
        dicts['validator_id'] = self.validator_id
        dicts['execute_time'] = self.execute_time
        return dicts