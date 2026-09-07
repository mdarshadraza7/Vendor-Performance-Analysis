import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time


# Configure logging
logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)


# Create database connection
engine = create_engine("sqlite:///inventory.db")

# Load data into database
def ingest_db(df, table_name, engine):
    """This function will ingest dataframe into database table."""

    df.to_sql(
        table_name,
        con=engine,
        if_exists="replace",
        index=False
    )


# Read CSV files and load into database
def load_raw_data():
    """This function will load CSV files as DataFrames and ingest them into DB."""

    start = time.time()
    logging.info("--- Starting Data Ingestion ---")

    for file in os.listdir("data"):
        if file.endswith(".csv"):
            try:
                df = pd.read_csv("data/" + file)
                print(df.shape)
                ingest_db(df, file[:-4], engine)
                logging.info(f"Successfully loaded {file} into database")

            except Exception as e:
                logging.error(f"Error processing {file}: {e}")
             
    end = time.time()
    total_time = (end - start) / 60
    logging.info("--- Ingestion Complete ---")
    logging.info(f"Total Time taken: {total_time:.2f} minutes")


if __name__ == "__main__":
    load_raw_data()