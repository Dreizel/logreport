import pytest
from logreport.utils import parse_date
from logreport.exceptions import InvalidDateError


def test_parse_date_valid():
    assert parse_date("2025-08-16") == "2025-08-16"


def test_parse_date_invalid_format():
    with pytest.raises(InvalidDateError):
        parse_date("16-08-2025")


def test_parse_date_invalid_value():
    with pytest.raises(InvalidDateError):
        parse_date("2025-99-99")
