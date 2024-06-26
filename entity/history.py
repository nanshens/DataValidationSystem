from datetime import datetime
from sqlalchemy import ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from . import db
from .base import Base


class History(Base):
    create_time: Mapped[datetime] = mapped_column(default=db.func.current_timestamp())
    execute_time: Mapped[datetime] = mapped_column(default=db.func.current_timestamp())
    validator = relationship("Validator")
    validator_id: Mapped[str] = mapped_column(ForeignKey("validator.id"))
    upload_file: Mapped[str] = mapped_column(nullable=True)
    download_file: Mapped[str] = mapped_column(nullable=True)
    repair_file: Mapped[str] = mapped_column(nullable=True)
    executor: Mapped[list] = mapped_column(JSON, nullable=True)
    config: Mapped[list] = mapped_column(JSON, nullable=True)
    result: Mapped[list] = mapped_column(JSON, nullable=True)

    def to_dict(self):
        dicts = super().to_dict()
        dicts['create_time'] = self.create_time
        dicts['validator_id'] = self.validator_id
        return dicts