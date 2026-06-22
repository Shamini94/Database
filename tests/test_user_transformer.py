from services.user_transformer import normalize_user

def test_normalize_user_trims_whitespace():
    raw = {
        "first_name": "  John ",
        "last_name": " Doe ",
        "email": " JOHN@EMAIL.COM "
    }

    result = normalize_user(raw)

    assert result["first_name"] == "John"
    assert result["last_name"] == "Doe"
    assert result["email"] == "john@email.com"