import sqlite3
from config import logger

DB_NAME="properties.db"

def get_db_connection(db_name: str=DB_NAME):
    return sqlite3.connect(db_name)

def initialize_db(db_name: str=DB_NAME):
    """
    Initializes the database with the required tables.
    """
    logger.info("Initializing Database")

    with get_db_connection(db_name=DB_NAME) as conn:

        conn.execute("DROP TABLE IF EXISTS listings")
        
        conn.execute("""
            CREATE TABLE IF NOT EXISTS listings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                price REAL,
                location TEXT NOT NULL,
                UNIQUE(title, location)
            )
        """)
        conn.commit()
        
def insert_properties(properties, db_name: str=DB_NAME):        
    """
    Inserts a list of property dictionaries into the database.
    """
    inserted = 0
    duplicates = 0
    failed = 0
    with get_db_connection() as conn:
        cursor = conn.cursor()
        for item in properties:
            try:
                cursor.execute(
                    """
                    INSERT INTO listings (title, price, location)
                    VALUES (?, ?, ?)
                    """,
                    (item['title'], item['price'], item['location'])
                )
                inserted += 1
                
            except sqlite3.IntegrityError:
                logger.info(
                    "Duplicate skipped: %s (%s)",
                    item["title"],
                    item["location"]
                )
                duplicates += 1
                    
            except sqlite3.Error as e:
                logger.error(f"Error inserting item {item}: {e}")
                failed += 1
        conn.commit()
    logger.info(f"Inserted {inserted} items, {duplicates} duplicates, {failed} failed.")