from fairest.main import fairest
from fairest.models import Request, ResponseCode


def test_main():
    request = Request(body='')
    assert fairest(request).response_code == ResponseCode.BAD_REQUEST
    request = Request(body='This is a test string')
    assert fairest(request).response_code == ResponseCode.OK
