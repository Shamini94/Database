def normalize_user(user: dict) -> dict:
    return {
        "first_name": user["first_name"].strip(),
        "last_name": user["last_name"].strip(),
        "email": user["email"].strip().lower(),
    }