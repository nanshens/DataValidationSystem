from sqlalchemy import ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from common.enums import ValidationRuleType
from . import db
from .base import Base


class ValidationRule(Base):
    type: Mapped[ValidationRuleType]
    attribute = relationship("Attribute")
    attribute_id: Mapped[str] = mapped_column(ForeignKey("attribute.id"))
    length: Mapped[int] = mapped_column()
    relate_entity: Mapped[str] = mapped_column()
    relate_attribute: Mapped[str] = mapped_column()
    collection: Mapped[list] = mapped_column(JSON)

    def to_dict(self):
        dicts = super().to_dict()
        dicts['type'] = self.type
        dicts['attribute_id'] = self.attribute_id
        dicts['length'] = self.length
        dicts['relate_entity'] = self.relate_entity
        dicts['relate_attribute'] = self.relate_attribute
        dicts['collection'] = self.collection
        return dicts