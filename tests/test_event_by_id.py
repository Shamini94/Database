import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()

def test_get_event_by_id_200(client):
    res = client.get("/api/events/2")

    assert res.status_code == 200
    data = res.get_json()

    assert "event" in data
    assert data["event"]["id"] == 2

def test_get_event_by_id_404(client):
    res = client.get("/api/events/99999")

    assert res.status_code == 404

def test_get_event_by_id_400(client):
    res = client.get("/api/events/not-a-number")

     assert res.status_code == 400