from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def register_models():
    from .validator import Validator
    from .validation_rule import ValidationRule
    from .repair_rule import RepairRule
    from .history import History
    from .entity import Entity
    from .attribute import Attribute
