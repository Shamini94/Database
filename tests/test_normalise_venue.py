import pytest
from seed import normalise_venue
from utils.normalise_venue import normalise_venue

def test_normalise_venue_trims_name():
    venue = {
        "name": "  Nexus, University of Leeds  ",
        "address": "Discovery Way, Leeds, LS2 3AA",
        "capacity": 200
    }

    assert normalise_venue(venue) == {
        "name": "Nexus, University of Leeds",
        "address": "Discovery Way, Leeds, LS2 3AA",
        "capacity": 200
    }

def test_handles_null_address():
    venue = {
        "name": "Online – Zoom",
        "address": None,
        "capacity": 500
    }

    result = normalise_venue(venue)

    assert result["address"] is None