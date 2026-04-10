from typing import TYPE_CHECKING, Literal

import pytest
from starlette.routing import Mount, Route

from mex.editor.main import create_fastapi

if TYPE_CHECKING:  # pragma: no cover
    from fastapi.testclient import TestClient


def test_main_app(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "</html>" in response.text
    assert "<app-root></app-root>" in response.text


@pytest.mark.parametrize(
    ("startup", "expect_api", "expect_static"),
    [
        ("both", True, True),
        ("api", True, False),
        ("frontend", False, True),
    ],
    ids=["both", "api-only", "frontend-only"],
)
def test_create_fastapi(
    startup: Literal["api", "frontend", "both"],
    expect_api: bool,  # noqa: FBT001
    expect_static: bool,  # noqa: FBT001
) -> None:
    app = create_fastapi(startup)
    route_paths = [r.path for r in app.routes if isinstance(r, Route)]
    mount_paths = [r.path for r in app.routes if isinstance(r, Mount)]
    assert ("/api/v0/sample-data" in route_paths) == expect_api
    assert ("" in mount_paths) == expect_static
