from collections.abc import Iterable
from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class LogRecord:
    """"""

    url: str
    status: int
    timestamp: str
    response_time: float
    request_method: str
    http_user_agent: str | None


class Report(Protocol):
    """"""

    name: str

    def run(self, records: Iterable[LogRecord]) -> list[dict]: ...
