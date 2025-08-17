from argparse import ArgumentParser

from tabulate import tabulate

from logreport.exceptions import InvalidReportError, LogReportError
from logreport.io_ import load_records
from logreport.reports import AVAILABLE_REPORTS
from logreport.utils import parse_date


def my_parse_args():
    parser = ArgumentParser(description="LOG reports script")
    parser.add_argument("--files", required=True, type=str, nargs="+", help="Paths to log file")
    parser.add_argument(
        "--report", required=True, type=str, choices=["average"], help="Read type: average"
    )
    parser.add_argument("--date", type=str, help="Filters the report by date")

    return parser.parse_args()


def main():
    args = my_parse_args()
    try:
        date = parse_date(args.date)
        records = load_records(args.files, date)
        report = AVAILABLE_REPORTS.get(args.report)

        if report is None:
            raise InvalidReportError(f"Unknown report: {args.report}")

        rows = report.run(records)
        print(tabulate(rows, headers="keys"))
        return 0

    except LogReportError as e:
        print(f"Error: {e}")
        return 2
