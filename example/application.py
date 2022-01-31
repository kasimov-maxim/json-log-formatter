import logging
import sys

from json_formatter import JSONFormatter

from log_generator import generate_logs

_log_handler = logging.StreamHandler()
_log_handler.setFormatter(JSONFormatter())

logging.basicConfig(
    level=logging.DEBUG,
    handlers=(_log_handler, )
)
_log = logging.getLogger(__name__)


def main() -> int:

    _log.info("Start generate logs")
    try:
        generate_logs()
    except KeyboardInterrupt:
        _log.info("Received exit, exiting")

    return 0


if __name__ == '__main__':  # pragma: nocover
    sys.exit(main())
