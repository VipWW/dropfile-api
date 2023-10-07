from enum import Enum

from marshmallow import Schema, fields


class _MessageType(Enum):
    MSG = 1
    STATUS = 2
    INFO = 3
    ERROR = 4


class _MessageSchema(Schema):
    message = fields.String(required=True)
    message_type = fields.Enum(_MessageType, default=_MessageType.MSG)


class Message(dict):
    def __new__(cls, *args, **kwargs):
        return dict.__new__(cls)

    def __init__(self, message: str, message_type: _MessageType = _MessageType.MSG):
        super().__init__()
        self.message = message
        self.message_type = message_type

        # dump using schema for validation
        obj = _MessageSchema().dump(self)

        _message: str = obj.get("message")
        _message_type: str = obj.get("message_type")

        self[_message_type.lower()] = _message


class StatusMessage(Message):
    def __init__(self, message: str):
        super().__init__(message, _MessageType.STATUS)


class InfoMessage(Message):
    def __init__(self, message: str):
        super().__init__(message, _MessageType.INFO)


class ErrorMessage(Message):
    def __init__(self, message: str):
        super().__init__(message, _MessageType.ERROR)
