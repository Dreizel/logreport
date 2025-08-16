import json
from collections.abc import Iterator

from logreport.domain import LogRecord
from logreport.exceptions import LogParseError


def load_records(paths: list[str], date_filter: str | None) -> Iterator[LogRecord]:
    for path in paths:
        with open(path) as file:
            for lineno, line in enumerate(file, start=1):
                try:
                    log_data = json.loads(line)
                    if "@timestamp" in log_data:
                        log_data["timestamp"] = log_data.pop("@timestamp")
                    log_record = LogRecord(**log_data)
                except Exception as e:
                    raise LogParseError(f"{path}:{lineno}: {e}") from e
                if date_filter and not log_record.timestamp.startswith(date_filter):
                    continue

                yield log_record
