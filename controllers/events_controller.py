from models.events_model import select_all_events, select_event_by_id

def get_events():
    rows = select_all_events()

    events = [
        {
            "id": r[0],
            "title": r[1],
            "starts_at": r[2].isoformat() if hasattr(r[2], "isoformat") else r[2],
            "ends_at": r[3].isoformat() if hasattr(r[3], "isoformat") else r[3],
            "location": r[4]
        }
        for r in rows
    ]

    return {"events": events}

def get_event_by_id(event_id):
    row = select_event_by_id(event_id)

    if row is None:
        return None

    return {
        "id": row[0],
        "title": row[1],
        "description": row[2],
        "starts_at": row[3].isoformat() if hasattr(row[3], "isoformat") else row[3],
        "ends_at": row[4].isoformat() if hasattr(row[4], "isoformat") else row[4],
        "location": row[5],
        "address": row[6],
        "capacity": row[7],
        "created_at": row[8].isoformat() if hasattr(row[8], "isoformat") else row[8],
    }