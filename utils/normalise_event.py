def normalise_event(event: dict) -> dict:
    return {
        "title": event["title"].strip(),
        "description": event["description"].strip() if event["description"] else None,
        "starts_at": event["starts_at"],
        "ends_at": event["ends_at"],
        "organiser_id": int(event["organiser_id"]),
        "venue_id": int(event["venue_id"])
    }