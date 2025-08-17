import os

from logreport.io_ import load_records
from logreport.reports import AverageReport

TEST_LOG_1 = os.path.join(os.path.dirname(__file__), "data", "example1.log")
TEST_LOG_2 = os.path.join(os.path.dirname(__file__), "data", "example2.log")


def test_empty_list():
    report = AverageReport()
    result = report.run([])
    assert result == []


def test_average_report_one_url():
    report = AverageReport()
    result = report.run(load_records([TEST_LOG_1], date_filter=None))
    assert result[0:2] == [
        {"handler": "/api/homeworks/...", "total": 71, "avg_response_time": 0.158},
        {"handler": "/api/context/...", "total": 21, "avg_response_time": 0.043},
    ]


def test_average_report_multiple_urls():
    report = AverageReport()
    result = report.run(load_records([TEST_LOG_1, TEST_LOG_2], date_filter="2025-06-22"))
    print(result[0:2])
    assert result[0:2] == [
        {"handler": "/api/homeworks/...", "total": 3521, "avg_response_time": 0.095},
        {"handler": "/api/context/...", "total": 2564, "avg_response_time": 0.023},
    ]
