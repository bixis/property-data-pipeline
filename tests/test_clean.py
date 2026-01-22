import pytest
from pipeline.clean import normalize_listings, clean_price



def test_clean_price():
    assert clean_price("$1,200.50") == 1200.50
    assert clean_price("€999.99") == 999.99
    assert clean_price("1200") == 1200.0
    assert clean_price("") is None
    assert clean_price(None) is None
    assert clean_price("invalid") is None
    
    
def test_normalize_listings():
    raw_data = [
        {"title": "Apartment A", "price": "$1,200.00", "location": "City X"},
        {"title": "House B", "price": "€950.50", "location": "City Y"},
        {"title": "Condo C", "price": None, "location": "City Z"},
        {"title": "Villa D", "price": "invalid", "location": "City W"},
    ] # This raw data was AI generated for testing purposes.
    
    normalized = normalize_listings(raw_data)
    
    assert len(normalized) == 2  # Two entries should be skipped due to invalid prices
    
    assert normalized[0] == {
        "title": "Apartment A",
        "price": 1200.00,
        "location": "City X"
    }
    
    assert normalized[1] == {
        "title": "House B",
        "price": 950.50,
        "location": "City Y"
    }