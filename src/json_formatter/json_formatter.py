import logging
import json
import traceback
from datetime import date, datetime, time
from inspect import istraceback
from typing import Any, Dict


_STANDARD_ATTRIBUTES = (
    "name",
    "levelname",
    "exc_info",
    "exc_text",
    "stack_info",
)


def _log_attributes(record: logging.LogRecord) -> Dict[str, Any]:
    return {
        f"@log:{name}": record.__dict__[name]
        for name in _STANDARD_ATTRIBUTES if record.__dict__[name]
    }


_JSONEncoder = json.JSONEncoder()


def _default(obj):
    if isinstance(obj, (date, datetime, time)):
        return obj.isoformat()

    elif istraceback(obj):
        return ''.join(traceback.format_tb(obj)).strip()

    elif type(obj) == Exception \
            or isinstance(obj, Exception) \
            or type(obj) == type:
        return str(obj)

    try:
        return _JSONEncoder.default(obj)

    except TypeError:
        try:
            return str(obj)
        except Exception:
            return "json-unformattable"


class JSONFormatter(logging.Formatter):

    def format(self, record):

        message = _log_attributes(record)
        if isinstance(record.msg, dict):
            message.update(record.msg)
        else:
            message["@log:message"] = record.msg

        record.msg = json.dumps(message, default=_default)
        return super().format(record)


__all__ = [JSONFormatter, ]
