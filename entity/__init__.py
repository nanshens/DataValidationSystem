from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def register_models():
    from .validator import Validator
    from .history import History
    from .dict_value import DictValue
    from .executor import Executor
