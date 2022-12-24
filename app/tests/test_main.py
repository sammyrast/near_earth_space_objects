import pytest 
from fastapi.testclient import TestClient
from app.main import app


def test_ping(test_app):
    response = test_app.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client  

