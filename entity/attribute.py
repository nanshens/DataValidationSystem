from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from . import db
from .base import Base


class Attribute(Base):
    type: Mapped[str]
    entity = relationship("Entity")
    entity_id: Mapped[str] = mapped_column(ForeignKey("entity.id"))