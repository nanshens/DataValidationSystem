import uuid

from sqlalchemy import JSON
from sqlalchemy.orm import Mapped, mapped_column
from . import db
from .base import Base

# todo: entity:id active code name
# todo: Attribute:id active code name type
# todo: RepairRule:id active code name type replace_strs replace_result substring_format is_regexp_replace
# todo: ValidationRule:id active code name type length relate_entity relate_attribute collection
# todo: 添加正则表达式 在validationrule 和repairrule中
class Validator(Base):
    config: Mapped[list] = mapped_column(JSON, nullable=True)



    def get_entity(self, id):
        r = [ r for r in self.config if r['id'] == id]
        return r[0] if len(r) == 1 else None

    def add_entity(self, code, name, ):
        entity = {
            "id": uuid.uuid4(),
            "code": code,
            "name": name,
            "active": True
        }
        return entity


    def to_dict(self, with_config=False):
        dicts = super().to_dict()
        if with_config:
            dicts['config'] = self.config
        return dicts