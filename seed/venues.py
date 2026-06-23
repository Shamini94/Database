import json
from pathlib import Path


DATA_DIR = Path(__file__).parent / "data"


def drop_venues_table(cursor):
    cursor.execute("DROP TABLE IF EXISTS venues;")


def create_venues_table(cursor):
    cursor.execute("""
        CREATE TABLE venues (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            address TEXT,
            capacity INT
        );
    """)
def load_venues():
    with open(DATA_DIR / "venues.json", "r", encoding="utf-8") as file:
        return json.load(file)


def insert_venues(cursor, venues):
    values = [
        (
            venue["name"],
            venue["address"],
            venue["capacity"]
        )
        for venue in venues
    ]

    cursor.executemany(
        """
        INSERT INTO venues (name, address, capacity)
        VALUES (%s, %s, %s);
        """,
        values
    )
def seed(connection):
    cursor = connection.cursor()

    drop_venues_table(cursor)
    create_venues_table(cursor)

    venues = load_venues()
    insert_venues(cursor, venues)

    connection.commit()