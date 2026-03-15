### Crypto Data Pipeline

## Overview:

This project is a simple data pipeline that collects cryptocurrency price data from the CoinGecko API. The data is processed using Python and stored in both a CSV file and a PostgreSQL database.The goal of the project is to demonstrate a basic ETL pipeline with data extraction from an API, transformation using Pandas, and storage in a database.

## Pipeline Architecture

CoinGecko API
      ↓
Python ETL Script
      ↓
Data Cleaning (Pandas)
      ↓
PostgreSQL Database
      ↓
Logging 

## Technologies Covered
Python
Pandas
Requests
PostgreSQL
psycopg2
JSON configuration file
Logging for pipeline monitoring

## working of pipeline:
The pipeline follows simple ETL pipeline
Extract:
->The script requests cryptocurrency price data from the CoinGecko API.

Transform:
->The JSON response from the API is converted into a Pandas DataFrame.The data is then reshaped so that
  each cryptocurrency appears as a row with its price and timestamp.

Load:
->The processed data is stored in two places:
  In a CSV file for simple file storage and PostgreSQL database for structured storage and querying 

## Schema Design

The PostgreSQL database contains a table called "crypto_prices" used to store cryptocurrency price data.

Table structure:

crypto_prices  
--------------
id  
coin  
price_usd  
timestamp  

- **id** – Primary key automatically generated for each record  
- **coin** – Name of the cryptocurrency (e.g., bitcoin, ethereum)  
- **price_usd** – Price of the cryptocurrency in USD  
- **timestamp** – Time when the data was collected

## Running of pipeline:
To execute the pipeline.

1. Install Dependencies
Install the required Python libraries listed in requirements.txt.
-->pip install -r requirements.txt
2. Run the pipeline
Execute the main pipeline script:
-->python crypto_pipeline.py

After running the script, cryptocurrency price data is fetched from the API, processed using Python and Pandas, and stored in CSV file: output/crypto_prices.csv  and PostgreSQL table: crypto_prices

## Conclusion:

-->This project implements a simple ETL pipeline that collects cryptocurrency price data from an API, processes it using Python and Pandas, and stores the results in PostgreSQL Database.
-->The pipeline also includes logging and exception handling to improve reliability and traceability. Overall, this project highlights the fundamental concepts of data ingestion, transformation, and storage in a basic data engineering workflow