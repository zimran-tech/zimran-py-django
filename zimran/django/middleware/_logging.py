import sys
import time
import uuid

from django.conf import settings as app_settings
from django.core.exceptions import ImproperlyConfigured
from loguru import logger

try:
    logger.remove(0)
    logger.add(
        sys.stdout,
        level='DEBUG' if app_settings.DEBUG else 'INFO',
        serialize=True,
        colorize=True,
        format='{message}',
    )
except ImproperlyConfigured as error:
    print(error)


class LoguruMiddleware:
    def __init__(self, get_response: callable):
        self._get_response = get_response

    def __call__(self, request):
        request_id = str(uuid.uuid4())
        with logger.contextualize(request_id=request_id):
            request.start_time = time.time()
            response = self._get_response(request)
            elapsed = time.time() - request.start_time

            logger.bind(
                url=request.get_full_path(),
                method=request.method,
                status_code=response.status_code,
                response_size=len(response.content),
                elapsed=elapsed,
            ).info('incoming {method} request to {path}', method=request.method, path=request.path)

            response['X-Request-ID'] = request_id

            return response
