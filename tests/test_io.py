import os
import pytest
from logreport.io_ import load_records
from logreport.domain import LogRecord
from logreport.exceptions import LogParseError

TEST_LOG = os.path.join(os.path.dirname(__file__), "data", "example1.log")

def test_load_records_success():
    records = list(load_records([TEST_LOG], date_filter=None))
    assert len(records) == 100
    assert isinstance(records[0], LogRecord)


def test_load_records_with_date_filter():
    records = list(load_records([TEST_LOG], "2025-06-22"))
    assert all(r.timestamp.startswith("2025-06-22") for r in records)


def test_load_records_invalid_log_raises_error(tmp_path):
    bad_log = tmp_path / "bad.log"
    bad_log.write_text('{"url": "/home", "status": 200')

    with pytest.raises(LogParseError):
        list(load_records([str(bad_log)], date_filter=None))

