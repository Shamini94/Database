def normalise_venue(venue: dict) -> dict:
    return {
        "name": venue["name"].strip(),
        "location": venue["location"].strip(),
        "capacity": int(venue["capacity"])
    }