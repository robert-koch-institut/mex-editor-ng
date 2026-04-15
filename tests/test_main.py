from typing import TYPE_CHECKING, Literal

import pytest
from starlette.routing import Mount, Route

from mex.editor.main import create_fastapi

if TYPE_CHECKING:  # pragma: no cover
    from fastapi.testclient import TestClient


@pytest.mark.parametrize(
    ("mode", "startup", "expect_api", "expect_static"),
    [
        (None, "both", True, True),
        (None, "api", True, False),
        (None, "frontend", False, True),
        ("dev", "both", True, True),
        ("dev", "api", True, False),
    ],
    ids=["both", "api-only", "frontend-only", "dev-both", "dev-api"],
)
def test_create_fastapi(
    mode: Literal["dev"] | None,
    startup: Literal["api", "frontend", "both"],
    expect_api: bool,  # noqa: FBT001
    expect_static: bool,  # noqa: FBT001
) -> None:
    app = create_fastapi(mode, startup)
    route_paths = [r.path for r in app.routes if isinstance(r, Route)]
    mount_paths = [r.path for r in app.routes if isinstance(r, Mount)]
    assert ("/api/v0/sample-data" in route_paths) == expect_api
    assert ("" in mount_paths) == expect_static


@pytest.mark.parametrize(
    ("path", "accept", "expected_status", "expected_body"),
    [
        ("/favicon.ico", "*/*", 200, None),
        ("/nonexistent", "text/html", 200, "MEx Editor"),
        ("/missing.js", "application/javascript", 404, None),
    ],
    ids=["existing-file", "spa-fallback", "missing-asset-404"],
)
def test_spa_static_files(
    client_with_frontend: TestClient,
    path: str,
    accept: str,
    expected_status: int,
    expected_body: str | None,
) -> None:
    response = client_with_frontend.get(path, headers={"accept": accept})
    assert response.status_code == expected_status
    if expected_body:
        assert expected_body in response.text
