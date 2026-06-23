from utils.normalise_user import normalise_user

def test_trims_name():
    user = {"name": " Alice ", "email": "a@b.com", "password": "123"}
    assert normalise_user(user)["name"] == "Alice"

def test_lowercases_email():
    user = {"name": "Alice", "email": "ALICE@EXAMPLE.COM", "password": "123"}
    assert normalise_user(user)["email"] == "alice@example.com"