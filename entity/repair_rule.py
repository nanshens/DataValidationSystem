from sqlalchemy import ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from common.enums import RepairRuleType
from entity.base import Base


class RepairRule(Base):
    type: Mapped[RepairRuleType]
    attribute = relationship("Attribute")
    attribute_id: Mapped[str] = mapped_column(ForeignKey("attribute.id"))
    replace_strs: Mapped[list] = mapped_column(JSON)
    replace_result: Mapped[str] = mapped_column()
    substring_format: Mapped[str] = mapped_column()

    def to_dict(self):
        dicts = super().to_dict()
        dicts['type'] = self.type
        dicts['attribute_id'] = self.attribute_id
        dicts['replace_strs'] = self.replace_strs
        dicts['replace_result'] = self.replace_result
        dicts['substring_format'] = self.substring_format
        return dicts