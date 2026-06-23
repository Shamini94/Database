import json
from pathlib import Path
from utils.normalise_rsvp import normalise_rsvp


def drop_rsvps_table(cursor):
    cursor.execute("DROP TABLE IF EXISTS rsvps;")


def create_rsvps_table(cursor):
    cursor.execute("""
        CREATE TABLE rsvps (
            attendee_id INTEGER NOT NULL REFERENCES users(id),
            event_id INTEGER NOT NULL REFERENCES events(id),
            PRIMARY KEY (attendee_id, event_id)
        );
    """)


def load_rsvps_from_file():
    file_path = Path(__file__).resolve().parent.parent / "data" / "rsvps.json"
    with open(file_path, "r") as f:
        return json.load(f)


def insert_rsvps(cursor, rsvps):
    values = [(r["attendee_id"], r["event_id"]) for r in rsvps]

    cursor.executemany(
        """
        INSERT INTO rsvps (attendee_id, event_id)
        VALUES (%s, %s)
        """,
        values
    )

def seed_rsvps(connection):
    cursor = connection.cursor()

    drop_rsvps_table(cursor)
    create_rsvps_table(cursor)

    raw_rsvps = load_rsvps_from_file()
    rsvps = [normalise_rsvp(r) for r in raw_rsvps]

    insert_rsvps(cursor, rsvps)

    connection.commit()
    cursor.close()