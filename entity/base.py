import uuid
from sqlalchemy.orm import Mapped, mapped_column
from entity import db


def generate_uuid():
  return str(uuid.uuid4())

class Base(db.Model):
    __abstract__ = True
    id: Mapped[str] = mapped_column(primary_key=True, default=generate_uuid)
    active: Mapped[bool] = mapped_column(default=True)
    code: Mapped[str] = mapped_column()
    name: Mapped[str]


    def to_dict(self):
        return {"id": self.id, "active": self.active, "code": self.code, "name": self.name}