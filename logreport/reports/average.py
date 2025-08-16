from typing import Iterable
from collections import defaultdict
from logreport.domain import LogRecord

class AverageReport:
    name = 'average'

    def run(self, records: Iterable[LogRecord]) -> list[dict]:
        """
        Groups records by URL and calculates:
        Total number of requests (total)
        Average response time (avg_response_time)
        """
        groups = defaultdict(list)

        for record in records:
            groups[record.url].append(record.response_time)

        result = []

        for url, times in groups.items():
            total = len(times)
            avg = round(sum(times) / total, 3)
            result.append({
                'handler': url,
                'total': total,
                'avg_response_time': avg
            })

        result.sort(key=lambda row: row["total"], reverse=True)

        return result