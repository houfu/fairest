from fairest.main import fairest
from fairest.models import Request, ResponseCode


def test_main():
    request = Request(body='')
    assert fairest(request).response_code == ResponseCode.BAD_REQUEST
    request = Request(body='This is a test string')
    assert fairest(request).response_code == ResponseCode.OK
    request = Request(body=b"ABCD")
    assert fairest(request).response_code == ResponseCode.BAD_REQUEST


def test_logging():
    request = Request(body='')
    assert fairest(request).debug_log
    request = Request(body="This is a test string.", disable={'DocumentStatisticsRule': True}, debug_log_report=True)
    response = fairest(request)
    assert len(response.reports) == 1
