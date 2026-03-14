# Crypto Data Pipeline

## Overview
This project builds an automated ETL pipeline that fetches cryptocurrency prices from the CoinGecko API, processes the data, and stores it in PostgreSQL

## Architecture
API → Python Script → Data Cleaning → PostgreSQL

##Pipeline Architecture

CoinGecko API
      ↓
Python ETL Script
      ↓
Data Cleaning (Pandas)
      ↓
PostgreSQL Database
      ↓
Logging 


## Tools Used
- Python
- Pandas
- Requests
- PostgreSQL
- Logging

## Pipeline Steps
1. Fetch cryptocurrency price data from CoinGecko API
2. Convert JSON response into a Pandas DataFrame
3. Clean and structure the data
4. Store processed data in PostgreSQL
5. Log pipeline execution
