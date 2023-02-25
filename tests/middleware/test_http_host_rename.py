from dataclasses import dataclass

import pytest

from zimran.django.middleware import HttpHostRenameMiddleware


@dataclass
class Request:
    META: dict


@pytest.mark.parametrize(
    'http_host, expected_http_host',
    [
        ('localhost:8000', 'localhost:8000'),
        ('stack_app:8000', 'stack-app:8000'),
    ],
)
def test_rename_http_host(http_host: str, expected_http_host: str) -> None:
    request = Request(META={'HTTP_HOST': http_host})
    HttpHostRenameMiddleware.rename_http_host(request)
    assert request.META['HTTP_HOST'] == expected_http_host
