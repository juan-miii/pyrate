from typing import List, Dict
from google_play_scraper import Sort, reviews_all
import os
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

def get_google_reviews() -> List[Dict[str, str]]:
    """
    Downloads all reviews from Google Play using the reviews_all function.

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing the downloaded reviews.

    Raises:
        ValueError: If the environment variable `GOOGLE_APP_ID` is not set.
    """
    # Read configuration from .env
    app_id: str = os.getenv("GOOGLE_APP_ID", "")
    language: str = os.getenv("LANGUAGE", "es")
    country: str = os.getenv("COUNTRY", "es")

    logging.debug("Configuration: Google App ID: %s, Language: %s, Country: %s", app_id, language, country)

    if not app_id:
        logging.error("GOOGLE_APP_ID is not set in the .env file")
        raise ValueError("GOOGLE_APP_ID is not set in the .env file")

    logging.info(f"Downloading all reviews for the app with ID '{app_id}'...")

    try:
        # Download all reviews
        all_reviews: List[Dict[str, str]] = reviews_all(
            app_id,
            sleep_milliseconds=200,  # Delay between requests to avoid being blocked
            lang=language,
            country=country,
            sort=Sort.NEWEST  # Sort by the most recent reviews
        )
        logging.info(f"Downloaded {len(all_reviews)} reviews.")
        return all_reviews

    except Exception as e:
        logging.error(f"Error downloading reviews: {e}")
        raise
