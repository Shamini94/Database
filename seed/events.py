import json
from pathlib import Path
from utils.normalise_event import normalise_event


def drop_events_table(cursor):
    cursor.execute("DROP TABLE IF EXISTS events;")


def create_events_table(cursor):
    cursor.execute("""
        CREATE TABLE events (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            description TEXT,
            starts_at TIMESTAMP NOT NULL,
            ends_at TIMESTAMP NOT NULL,
            organiser_id INTEGER NOT NULL REFERENCES users(id),
            venue_id INTEGER NOT NULL REFERENCES venues(id)
        );
    """)
def load_events_from_file():
    file_path = Path(__file__).resolve().parent.parent / "data" / "events.json"
    with open(file_path, "r") as f:
        return json.load(f)


def insert_events(cursor, events):
    values = [
        (
            e["title"],
            e["description"],
            e["starts_at"],
            e["ends_at"],
            e["organiser_id"],
            e["venue_id"]
        )
        for e in events
    ]

    cursor.executemany(
        """
        INSERT INTO events (
            title,
            description,
            starts_at,
            ends_at,
            organiser_id,
            venue_id
        ) VALUES (%s, %s, %s, %s, %s, %s)
        """,
        values
    )
def seed_events(connection):
    cursor = connection.cursor()

    drop_events_table(cursor)
    create_events_table(cursor)

    raw_events = load_events_from_file()
    events = [normalise_event(e) for e in raw_events]

    insert_events(cursor, events)

    connection.commit()
    cursor.close()