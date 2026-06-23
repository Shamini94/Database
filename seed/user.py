import json
from db.connection import get_connection
from services.user_transformer import normalize_user

def load_users(path="data/users.json"):
    with open(path, "r") as f:
        return json.load(f)

def seed_users():
    conn = get_connection()
    cur = conn.cursor()

    users = load_users()

    cleaned = [
        normalize_user(user)
        for user in users
    ]

    query = """
        INSERT INTO users (first_name, last_name, email)
        VALUES (%s, %s, %s)
    """
cur.executemany(
        query,
        [(u["first_name"], u["last_name"], u["email"]) for u in cleaned]
    )

conn.commit()
cur.close()
conn.close()

if __name__ == "__main__":
    seed_users()
    