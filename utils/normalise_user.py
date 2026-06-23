def normalise_user(user: dict) -> dict:
    return {
        "name": user["name"].strip(),
        "email": user["email"].strip().lower(),
        "password": user["password"]  # ideally hashed in real apps
    }