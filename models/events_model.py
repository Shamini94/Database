from db.connection import get_connection


def select_all_events():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            title,
            starts_at,
            ends_at,
            CONCAT(
                v.name, ', ',
                COALESCE(v.address, 'Online')
            ) AS location
        FROM events e
        JOIN venues v ON e.venue_id = v.id
        ORDER BY starts_at ASC;
    """)
    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return rows

def select_event_by_id(event_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            e.id,
            e.title,
            e.description,
            e.starts_at,
            e.ends_at,
            CONCAT(v.name) AS location,
            v.address,
            v.capacity,
            e.starts_at AS created_at
        FROM events e
        JOIN venues v ON e.venue_id = v.id
        WHERE e.id = %s;
    """, (event_id,))

    row = cursor.fetchone()

    cursor.close()
    connection.close()

    return row