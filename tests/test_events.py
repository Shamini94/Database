import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_get_events_status_200(client):
    res = client.get("/api/events")

    assert res.status_code == 200


def test_get_events_returns_events_key(client):
    res = client.get("/api/events")
    data = res.get_json()

    assert "events" in data
    assert isinstance(data["events"], list)


def test_events_are_ordered_by_starts_at(client):
    res = client.get("/api/events")
    events = res.get_json()["events"]

    dates = [e["starts_at"] for e in events]

    assert dates == sorted(dates)
