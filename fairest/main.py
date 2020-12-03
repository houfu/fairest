from typing import Union

from fairest.core.logging import init_logger, fairest_logger, close_logger
from fairest.core.modelling import get_model
from fairest.core.reporting import run_reporting
from fairest.core.settings import Settings
from fairest.models import Response, ResponseCode


def fairest(body: Union[str, bytes], **kwargs) -> Response:
    settings = Settings(**kwargs)
    log_stream = init_logger()
    fairest_logger.info('Begin main.')
    request = settings.create_request(body, **kwargs)
    fairest_logger.debug(
        f'Request submitted: size: {len(body)}, '
        f'Debug: {settings.development}'
        f'options: {settings if request.options else "Default"}')
    response = Response(request=request)
    fairest_logger.info('Begin document model construction.')
    document = get_model(request)
    if document:
        fairest_logger.info('Document model construction finished.')
        fairest_logger.debug(
            f'Document model details: Document Type: {document.document_type}; '
            f'Number of sections: {len(document)}')
        fairest_logger.info('Starting reporting functions.')
        run_reporting(document, request, response)
    else:
        fairest_logger.error('Fairest failed to find a rule that could form a document model.')
        response.response_code = ResponseCode.BAD_REQUEST
    fairest_logger.info('End fairest processing.')
    fairest_logger.info(
        f'Response Code: {response.response_code}; Number of reports collected: {len(response.reports)}')
    close_logger(log_stream, response)
    return response
