def normalise_rsvp(rsvp: dict) -> dict:
    return {
        "attendee_id": int(rsvp["attendee_id"]),
        "event_id": int(rsvp["event_id"])
    }