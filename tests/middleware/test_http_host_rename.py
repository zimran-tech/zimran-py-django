import pytest

from zimran.django.middleware import HttpHostRenameMiddleware


@pytest.mark.parametrize('http_host, expected_http_host', [
    ('localhost:8000', 'localhost:8000'),
    ('stocks_app:8000', 'stocks-app:8000'),
])
def test_rename_http_host(http_host: str, expected_http_host: str) -> None:
    assert HttpHostRenameMiddleware._rename_http_host(http_host) == expected_http_host
