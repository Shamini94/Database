from utils.normalise_event import normalise_event

def test_trims_title():
    event = {
        "title": "  Meetup ",
        "description": None,
        "starts_at": "2026-01-01T10:00:00",
        "ends_at": "2026-01-01T12:00:00",
        "organiser_id": "1",
        "venue_id": "2"
    }

    assert normalise_event(event)["title"] == "Meetup"


def test_handles_null_description():
    event = {
        "title": "Event",
        "description": None,
        "starts_at": "2026-01-01T10:00:00",
        "ends_at": "2026-01-01T12:00:00",
        "organiser_id": 1,
        "venue_id": 2
    }

    assert normalise_event(event)["description"] is None