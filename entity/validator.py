from sqlalchemy import JSON
from sqlalchemy.orm import Mapped, mapped_column
from . import db
from .base import Base

# todo: entity:id active code name
# todo: Attribute:id active code name type
# todo: RepairRule:id active code name type replace_strs replace_result substring_format
# todo: ValidationRule:id active code name type length relate_entity relate_attribute collection

class Validator(Base):
    config: Mapped[list] = mapped_column(JSON, nullable=True)


    def to_dict(self, with_config=False):
        dicts = super().to_dict()
        if with_config:
            dicts['config'] = self.config
        return dicts