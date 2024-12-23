import logging
from google_review import get_google_reviews
from excel_handler import save_to_excel

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

def main():
    """
    Main function to download reviews from Google Play and save them to an Excel file.
    """
    try:
        logging.info("Starting the review scraping process...")

        # Fetch Google Play reviews
        logging.info("Fetching Google Play reviews...")
        google_reviews = get_google_reviews()

        # Save reviews to an Excel file
        logging.info("Saving reviews to an Excel file...")
        save_to_excel(google_reviews, filename="reviews.xlsx")
    
    except Exception as e:
        logging.error(f"An error occurred during the review scraping process: {e}")

if __name__ == "__main__":
    main()
