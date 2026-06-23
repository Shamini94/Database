from utils.normalise_rsvp import normalise_rsvp

def test_converts_ids_to_int():
    rsvp = {"attendee_id": "2", "event_id": "5"}

    result = normalise_rsvp(rsvp)

    assert isinstance(result["attendee_id"], int)
    assert isinstance(result["event_id"], int)


def test_values_correct():
    rsvp = {"attendee_id": "3", "event_id": "7"}

    result = normalise_rsvp(rsvp)

    assert result == {"attendee_id": 3, "event_id": 7}