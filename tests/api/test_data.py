from typing import TYPE_CHECKING

from mex.editor.api.data import _sample_data

if TYPE_CHECKING:  # pragma: no cover
    from fastapi.testclient import TestClient


def test_sample_data(client: TestClient) -> None:
    response = client.get("/api/v0/sample-data")
    assert response.status_code == 200
    assert response.json() == _sample_data
