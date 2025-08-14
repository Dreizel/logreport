from datetime import datetime
from logreport.exceptions import InvalidDateError


def parse_date(date_str: str | None) -> str | None:
    if not date_str:
        return None
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        raise InvalidDateError()
