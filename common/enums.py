from enum import Enum


class AttributeType(Enum):
    Int = "int"
    Double = "double"
    String = "string"
    Boolean = "boolean"
    Date = "date"
    Time = "time"
    DateTime = "datetime"
    TIMESTAMP = "timestamp"
    Json = "json"

    @classmethod
    def all(self):
        return [enum.name for enum in AttributeType]


class ValidationRuleType(Enum):
    Length = "length"
    Unique = "unique"
    Relate = "relate"
    Collection = "collection"
    NotNull = "not_null"
    Regexp = "regexp"

    @classmethod
    def all(self):
        return [enum.name for enum in ValidationRuleType]


class RepairRuleType(Enum):
    Replace = "replace"
    Substring = "substring"

    @classmethod
    def all(self):
        return [enum.name for enum in RepairRuleType]

class ResponseCode(Enum):
    Success = 200
    Fail = 400