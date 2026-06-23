from db.connection import get_connection  # adjust to your project
from seed.users import seed_users
from seed.venues import seed_venues
from seed.events import seed_events
from seed.rsvps import seed_rsvps

def seed():
    """Reset and seed the database."""
    connection = None

    try:
        connection = get_connection()

        seed_users(connection)
        seed_venues(connection)
        seed_events(connection)
        seed_rsvps(connection) 
        
        print("Database seeded successfully")

    except Exception as e:
        if connection:
            connection.rollback()
        print(f"Seeding failed: {e}")
        raise

    finally:
        if connection:
            connection.close()


if __name__ == "__main__":
    seed()