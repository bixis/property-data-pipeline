from dotenv import load_dotenv
import os
import time
import requests
from config import logger
from bs4 import BeautifulSoup

load_dotenv()

DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; PropertyDataPipeline/1.0)"
}

def fetch_page(url: str, retries: int=3) -> str:
    """
    Fetches the content of a web page.
    
    Args:
        url (str): The URL of the web page to fetch.
        retries (int): Number of retries in case of failure - default is 3.
        
    Returns:
        str: The HTML content of the page.
    
    Raises:
        requests.RequestException: If the request fails after retries.
    """
    for attempt in range(0,retries):
        try:
            logger.info(f"Fetching URL: {url}")
            response = requests.get(url, timeout=10, headers=DEFAULT_HEADERS)
            response.raise_for_status()
            logger.info(f"Successfully fetched URL: {url}")
            return response.text
        except requests.RequestException as e:
            logger.error(f"Error fetching URL {url}: {e}")
            raise
            time.sleep(2)


def fetch_properties_for_sale():
    """
    Fetches property listings for sale from a predefined URL.
    
    Returns:
        str: The HTML content of the property listings page.
    """
    url = os.getenv("FOR_SALE_URL")   
    html = fetch_page(url)
    soup = BeautifulSoup(html, 'html.parser')
    properties = []
    # I would need to parse all of this...
    # After looking a bit through the HTML structure, each property is
    # in a div with class "rh_prop_card rh_prop_card--listing" from each
    # card I'll be extracting the title, price and location
    

    return properties

fetch_properties_for_sale()