from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from common.enums import ValidationRuleType
from . import db
from .base import Base


class ValidationRule(Base):
    type: Mapped[ValidationRuleType]
    attribute = relationship("Attribute")
    attribute_id: Mapped[str] = mapped_column(ForeignKey("attribute.id"))