import logging
from io import StringIO

from fairest.models import Response, Report


def init_logger(level=logging.DEBUG) -> logging.StreamHandler:
    ch = logging.StreamHandler(StringIO())
    fairest_logger.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    fairest_logger.addHandler(ch)
    return ch


def close_logger(log_stream: logging.StreamHandler, response: Response):
    log_stream.flush()
    response.debug_log = log_stream.stream.getvalue()
    if response.source_request.options.get('development', False):
        response.add_report(DebugReport(response.debug_log))
    log_stream.close()


class DebugReport(Report):
    def __init__(self, log: str):
        message = "Output of Debug Log \n" + log
        super().__init__(title="Debug Log", message=message, rule_id="Core.DebugReport")


fairest_logger = logging.getLogger('fairest')
