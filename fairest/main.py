from fairest.core.modelling import get_model
from fairest.core.reporting import run_reporting
from fairest.models import Response, Request, ResponseCode


def fairest(request: Request) -> Response:
    response = Response(request=request)
    document = get_model(request)
    if document:
        run_reporting(document, request, response)
    else:
        response.response_code = ResponseCode.BAD_REQUEST
    return response
