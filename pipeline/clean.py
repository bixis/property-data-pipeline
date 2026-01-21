import re # REGEX module
from config import logger

def clean_price(price: str) -> float:
    """
    Cleans and converts a price string to a float.
    """
    if not price:
        logger.debug("Price is missing or has no valid identity")
        return None
    clean_price = re.sub(r'[^\d.]', '', price)  # Removes non-numeric characters

    try:
        return float(clean_price)
    except ValueError:
        logger.debug(f"Failed to convert price '{price}' to float")
        return None
    

def normalize_listings(listings: list[dict]) -> list[dict]:
    """
    Normalize listing data by ensuring consistent field names and formats.
    """
    
    logger.info(f"Normalizing '{len(listings)}' data")
    
    normalized = []
    failed_prices = 0
    
    for item in listings:
        
        price = clean_price(item.get("price"))
        if price is None:
            failed_prices += 1
            logger.debug(f"Skipping item due to invalid price: {item}")
            continue
        
        normalized.append({
            "title": item.get("title"),
            "price": clean_price(item.get("price")),
            "location": item.get("location"),
        })
        
        if failed_prices:
            logger.warning(f"Skipped '{failed_prices}' items due to invalid prices")
            
    return normalized

    