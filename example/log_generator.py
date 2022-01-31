import time
import logging
from datetime import datetime

_log = logging.getLogger(__name__)


def generate_logs():

    while True:
        print(f"text print {datetime.utcnow()}")

        _log.info(
            f"plain text record: utcnow: {datetime.utcnow()}"
        )
        _log.info({
            "one": "one value",
            "two": "two value",
            "three": "three value",
            "utcnow": datetime.utcnow(),
        })

        time.sleep(1)
