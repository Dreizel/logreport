class LogReportError(Exception):
    pass

class InvalidReportError(LogReportError):
    pass

class InvalidDateError(LogReportError):
    pass

class LogParseError(LogReportError):
    pass
