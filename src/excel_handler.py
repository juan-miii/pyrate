import pandas as pd
import os
import time
import logging
from typing import List, Dict

MAX_RETRIES: int = 5  # Maximum number of retry attempts
SLEEP_TIME: int = 5  # Seconds to wait between retry attempts

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

def save_to_excel(google_reviews: List[Dict[str, str]], filename: str = "reviews.xlsx") -> None:
    """
    Saves the reviews to an Excel file in the './out' directory, ensuring no duplicates.
    If the file is open, it retries several times before failing.

    Args:
        google_reviews (List[Dict[str, str]]): List of dictionaries containing Google Play reviews.
        filename (str): The name of the Excel file to save the reviews to.

    Raises:
        ValueError: If the 'reviewId' field is not present in the downloaded data.
    """
    output_dir = os.path.abspath("./out")
    os.makedirs(output_dir, exist_ok=True)

    # Full path of the file
    file_path = os.path.join(output_dir, filename)

    # Attempt to load the existing file
    try:
        existing_google = pd.read_excel(file_path, sheet_name="Google Play")
        logging.info("Loaded existing file.")
    except FileNotFoundError:
        existing_google = pd.DataFrame()
        logging.info("No existing file found. A new file will be created.")

    # Convert the new reviews to a DataFrame
    new_google_df = pd.DataFrame(google_reviews)

    # Check for key fields in the data
    if "reviewId" not in new_google_df.columns:
        logging.error("The 'reviewId' field is not present in the downloaded data.")
        raise ValueError("The 'reviewId' field is not present in the downloaded data.")

    # Combine with existing data and remove duplicates
    combined_google_df = pd.concat([existing_google, new_google_df]).drop_duplicates(subset="reviewId", keep="first")

    # Attempt to save to the Excel file
    for attempt in range(MAX_RETRIES):
        try:
            with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
                combined_google_df.to_excel(writer, sheet_name="Google Play", index=False)
            logging.info(f"Reviews updated and saved to {file_path}")
            break
        except PermissionError:
            logging.warning(f"The file {file_path} is open. Retrying ({attempt + 1}/{MAX_RETRIES})...")
            time.sleep(SLEEP_TIME)  # Wait 5 seconds before retrying
    else:
        # If the file is still open after several attempts, notify the user
        logging.error(f"Failed to save the file {file_path} after {MAX_RETRIES} attempts.")