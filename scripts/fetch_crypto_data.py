import requests
import pandas as pd
from datetime import datetime
import logging
import psycopg2
import json

# -------------------------------
# Logging Setup
# -------------------------------
logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

logging.info("Pipeline started")

try:

    # -------------------------------
    # Load configuration
    # -------------------------------
    with open("config/config.json") as f:
        config = json.load(f)

    api_url = config["api_url"]
    coins = config["coins"]
    currency = config["currency"]

    # Build API URL
    url = f"{api_url}?ids={coins}&vs_currencies={currency}"

    # -------------------------------
    # API Request
    # -------------------------------
    response = requests.get(url)

    if response.status_code != 200:
        logging.error("API request failed")
        exit()

    logging.info("API request successful")

    data = response.json()

    # -------------------------------
    # Convert JSON → DataFrame
    # -------------------------------
    df = pd.DataFrame(data).T
    df.columns = ["price_usd"]

    # Add timestamp column
    df["timestamp"] = datetime.now()

    # Reset index so coin becomes column
    df.reset_index(inplace=True)
    df.rename(columns={"index": "coin"}, inplace=True)

    # -------------------------------
    # Missing Data Handling
    # -------------------------------
    df.dropna(subset=["price_usd"], inplace=True)

    # -------------------------------
    # Save to CSV
    # -------------------------------
    df.to_csv(
        "output/crypto_prices.csv",
        mode="a",
        header=False,
        index=False
    )

    logging.info("Data saved to CSV")

    # -------------------------------
    # Store in PostgreSQL
    # -------------------------------
    conn = psycopg2.connect(
        host="localhost",
        database="crypto_pipeline",
        user="postgres",
        password="12345"
    )

    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute(
            """
            INSERT INTO crypto_prices (coin, price_usd, timestamp)
            VALUES (%s, %s, %s)
            """,
            (row["coin"], row["price_usd"], row["timestamp"])
        )

    conn.commit()

    cursor.close()
    conn.close()

    logging.info("Data stored in PostgreSQL successfully")

except Exception as e:
    logging.error(f"Pipeline failed: {e}")