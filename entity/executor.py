from sqlalchemy import ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from common.utils import Utils
from . import db
from .base import Base
from datetime import datetime

class Executor(Base):
    execute_time: Mapped[datetime] = mapped_column(nullable=True)
    validator = relationship("Validator")
    validator_id: Mapped[str] = mapped_column(ForeignKey("validator.id"))
    match_entities: Mapped[list] = mapped_column(JSON, nullable=True)
    config: Mapped[list] = mapped_column(JSON, nullable=True)

    @staticmethod
    def create_from_dto(data):
        executor = Executor(id=Utils.del_prefix(data['id']), active=data['active'], code=data['code'],name=data['name'],
                            validator_id=data['validator_id'], match_entities=data['match_entities'], config=data['config'])
        return executor

    def to_dict(self):
        dicts = super().to_dict()
        dicts['validator_id'] = self.validator_id
        dicts['match_entities'] = self.match_entities
        dicts['config'] = self.config
        return dicts