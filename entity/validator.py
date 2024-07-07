import uuid
from sqlalchemy import JSON
from sqlalchemy.orm import Mapped, mapped_column
from common.utils import Utils
from . import db
from .base import Base

# todo: entity:id active code name attributes
# todo: attribute:id active code name type
# todo: RepairRule:id active code name type replace_strs replace_result substring_format is_regexp_replace
# todo: ValidationRule:id active code name type length relate_entity relate_attribute collection
# todo: 添加正则表达式 在validationrule 和repairrule中
class Validator(Base):
    entities: Mapped[list] = mapped_column(JSON, nullable=True)
    config: Mapped[list] = mapped_column(JSON, nullable=True)

    @staticmethod
    def create_from_dto(data):
        validator = Validator(id=Utils.del_prefix(data['id']), active=data['active'], code=data['code'],
                              name=data['name'] , entities=data['entities'])
        for entity in validator.entities:
            entity["id"] = Utils.del_prefix(str(entity["id"]))
            for attr in entity['attributes']:
                attr["id"] = Utils.del_prefix(str(attr["id"]))
                for repair in attr['repairRules']:
                    repair["id"] = Utils.del_prefix(str(repair["id"]))
                for validation in attr['validationRules']:
                    validation["id"] = Utils.del_prefix(str(validation["id"]))
        return validator


    def to_dict(self, with_entities=False):
        dicts = super().to_dict()
        if with_entities:
            dicts['entities'] = self.entities
        return dicts