from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from common.enums import RepairRuleType
from entity.base import Base


class RepairRule(Base):
    type: Mapped[RepairRuleType]
    attribute = relationship("Attribute")
    attribute_id: Mapped[str] = mapped_column(ForeignKey("attribute.id"))