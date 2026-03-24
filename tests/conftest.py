from typing import TYPE_CHECKING

import pytest
from fastapi.testclient import TestClient

from mex.editor.main import create_fastapi

if TYPE_CHECKING:  # pragma: no cover
    from collections.abc import Generator

pytest_plugins = ("mex.common.testing.plugin",)


@pytest.fixture(scope="session")
def client() -> Generator[TestClient]:
    """Return a fastAPI test client initialized with our app."""
    app = create_fastapi()
    with TestClient(app, raise_server_exceptions=False) as test_client:
        yield test_client
