import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

# Logging configuration
logging.basicConfig(
    filename='logs/ingestion_db.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode="a"  # append
)

# Ensure database folder exists
db_folder = "/home/Davcote/Desktop/HPV-Awareness-Impact-Analysis/data/database"
os.makedirs(db_folder, exist_ok=True)

# Build database path
db_path = os.path.join(db_folder, "HPV.db")

# Database engine for HPV.db inside data/database/
engine = create_engine(f"sqlite:///{db_path}")

def ingest_db(df, table_name, engine):
    """Ingest a DataFrame into the database."""
    try:
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        logging.info(f'Table "{table_name}" ingested successfully.')
    except Exception as e:
        logging.error(f'Error ingesting table "{table_name}": {e}')

def load_raw_data(raw_data_path):
    """Load CSV and Excel files from raw data folder and ingest into db."""
    start_time = time.time()
    try:
        if not os.path.exists(raw_data_path):
            logging.error(f'Raw data folder not found: {raw_data_path}')
            return

        for file in os.listdir(raw_data_path):
            file_path = os.path.join(raw_data_path, file)

            # CSV ingestion
            if file.lower().endswith('.csv'):
                try:
                    df = pd.read_csv(file_path)
                    table_name = os.path.splitext(file)[0]  # drop .csv
                    logging.info(f'Ingesting CSV file "{file}" as table "{table_name}"')
                    ingest_db(df, table_name, engine)
                except Exception as e:
                    logging.error(f'Error processing CSV {file}: {e}')

            # Excel ingestion
            elif file.lower().endswith(('.xls', '.xlsx')):
                try:
                    xls = pd.read_excel(file_path, sheet_name=None)  # dict of DataFrames
                    for sheet_name, df in xls.items():
                        table_name = f"{os.path.splitext(file)[0]}_{sheet_name}"  
                        # e.g., summary_sheet1
                        logging.info(f'Ingesting Excel sheet "{sheet_name}" from "{file}" as table "{table_name}"')
                        ingest_db(df, table_name, engine)
                except Exception as e:
                    logging.error(f'Error processing Excel {file}: {e}')

        end_time = time.time()
        total_time = (end_time - start_time) / 60  # minutes
        logging.info('All files ingested successfully')
        logging.info(f'Total time taken to ingest files: {total_time:.2f} minutes')

    except Exception as e:
        logging.error(f'Error in load_raw_data: {e}')

if __name__ == "__main__":
    raw_data_dir = "/home/Davcote/Desktop/HPV-Awareness-Impact-Analysis/data/raw_data"
    load_raw_data(raw_data_dir)
    logging.info('Ingestion process completed.')
