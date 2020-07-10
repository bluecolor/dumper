from app import settings
from .base import BaseStore
from . import registery


_questions = [
    {
        "type": "text",
        "name": "path",
        "message": "Path to folder:",
        "default": settings.CSV_PATH,
    },
    {
        "type": "text",
        "name": "field_delimiter",
        "message": "Field delimiter:",
        "default": settings.CSV_FIELD_DELIMITER,
    },
    {
        "type": "text",
        "name": "record_delimiter",
        "message": "Record delimiter:",
        "default": settings.CSV_RECORD_DELIMITER,
    },
]


class Csv(BaseStore):
    questions = BaseStore.questions + _questions

    @classmethod
    def name(cls):
        return "CSV"

    @classmethod
    def enabled(cls):
        return True

    @classmethod
    def type(cls):
        return "csv"


registery.register(Csv)