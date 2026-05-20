from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_home():

    response = client.get("/")

    assert response.status_code == 200


def test_execute():

    response = client.post(
        "/execute",
        json={
            "goal": "Build AI ecommerce system"
        }
    )

    assert response.status_code == 200