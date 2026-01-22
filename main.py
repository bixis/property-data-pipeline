from config import logger
from scraper.fetch import fetch_page
from db import initialize_db, insert_properties
from pipeline.clean import normalize_listings



def main():
    logger.info("Application started - RE (Real Estate) Data Pipeline Started")
    raw_listings = [
    {"title": "Apartment Centro", "price": "$120.000", "location": "Montevideo"},
    {"title": "Apartment Centro", "price": "$125.000", "location": "Montevideo"},
    {"title": "House Colonia", "price": None, "location": "Colonia"},
]

    normalized = normalize_listings(raw_listings)
    initialize_db()
    insert_properties(normalized)
    logger.info("Application finished successfully.")
    

if __name__ == "__main__":
    main()
