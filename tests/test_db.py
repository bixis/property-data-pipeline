import os
import pytest
from db import initialize_db, insert_properties, get_db_connection

TEST_DB = "test_properties.db"

def setup_function():
    """
    Setup a fresh test database before each test.
    """
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
    initialize_db(db_name=TEST_DB)


def teardown_function():
    """
    Remove the test database after each test.
    """
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
        
def test_insert_multiple_uniques():
    ...
    
def test_price_formatting():
    ...
    
def test_insert_empty_list():
    ...
            
        
def test_deduplication():
    test_data = [
        {"title": "Apartment A", "price": 1200.0, "location": "City X"},
        {"title": "Apartment A", "price": 1200.0, "location": "City X"},  # Duplicate
        {"title": "House B", "price": 950.5, "location": "City Y"},
    ]
    
    stats = insert_properties(test_data, db_name=TEST_DB)
    
    # Assert that one duplicate was skipped
    assert stats['inserted'] == 2
    assert stats['duplicates'] == 1
    assert stats['failed'] == 0
    
    # Assert database state
    with get_db_connection(TEST_DB) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM listings")
        count = cursor.fetchone()[0]
        assert count == 2  # Only two unique entries should be present
        print()
        