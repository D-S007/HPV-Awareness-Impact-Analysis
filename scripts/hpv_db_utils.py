# hpv_db_utils.py
import os
import sqlite3
import pandas as pd
from sqlalchemy import create_engine

# ==============================
# Database Setup
# ==============================

DB_PATH = "/home/Davcote/Desktop/HPV-Awareness-Impact-Analysis/data/database/HPV.db"
OUTPUT_PATH = "/home/Davcote/Desktop/HPV-Awareness-Impact-Analysis/data/processed_data/summary_data.xlsx"

engine = create_engine(f"sqlite:///{DB_PATH}")
conn = sqlite3.connect(DB_PATH)


# ==============================
# Helper Functions
# ==============================

def run_sql(query: str) -> pd.DataFrame:
    """Run SQL query and return results as a pandas DataFrame."""
    return pd.read_sql_query(query, conn)


def exec_sql(query: str) -> None:
    """Execute a non-SELECT SQL statement (DDL/DML)."""
    cur = conn.cursor()
    cur.executescript(query)
    conn.commit()


def insert_processed(df: pd.DataFrame, name: str, engine=engine):
    """Insert a processed DataFrame into DB with prefix 'processed_'."""
    table_name = f"processed_{name}"
    try:
        df.to_sql(table_name, con=engine, if_exists="replace", index=False)
        print(f"✅ Inserted into table: {table_name} ({len(df)} rows)")
    except Exception as e:
        print(f"❌ Error inserting {table_name}: {e}")


def insert_file_to_db(file_path: str, engine=engine):
    """Insert a CSV or Excel file into the SQLite DB."""
    try:
        if not os.path.exists(file_path):
            print(f"❌ File not found: {file_path}")
            return

        table_name = os.path.splitext(os.path.basename(file_path))[0]

        if file_path.lower().endswith(".csv"):
            df = pd.read_csv(file_path)
            df.to_sql(table_name, con=engine, if_exists="replace", index=False)
            print(f"✅ Inserted CSV into table: {table_name} ({len(df)} rows)")

        elif file_path.lower().endswith((".xls", ".xlsx")):
            xls = pd.read_excel(file_path, sheet_name=None)
            for sheet_name, df in xls.items():
                sheet_table = f"{table_name}_{sheet_name}"
                df.to_sql(sheet_table, con=engine, if_exists="replace", index=False)
                print(f"✅ Inserted Excel sheet '{sheet_name}' into table: {sheet_table} ({len(df)} rows)")
        else:
            print(f"❌ Unsupported file type: {file_path}")

    except Exception as e:
        print(f"❌ Error inserting {file_path}: {e}")


# ==============================
# Workflow: Create + Copy + Export
# ==============================

def create_summary_tables():
    """Create new demographic, pretest, post_test tables with INTEGER schema and copy raw data."""

    # Drop if exists
    exec_sql("""
    DROP TABLE IF EXISTS demographic;
    DROP TABLE IF EXISTS pretest;
    DROP TABLE IF EXISTS post_test;
    """)

    # Create demographic
    exec_sql("""
    CREATE TABLE demographic (
        Sno INTEGER,
        "1" INTEGER, "2" INTEGER, "3" INTEGER, "4" INTEGER,
        "5" INTEGER, "6" INTEGER, "7" INTEGER, "8" INTEGER
    )
    """)

    # Create pretest
    exec_sql("""
    CREATE TABLE pretest (
        Sno INTEGER,
        "1" INTEGER, "2" INTEGER, "3" INTEGER, "4" INTEGER, "5" INTEGER,
        "6" INTEGER, "7" INTEGER, "8" INTEGER, "9" INTEGER, "10" INTEGER,
        "11" INTEGER, "12" INTEGER, "13" INTEGER, "14" INTEGER, "15" INTEGER,
        "16" INTEGER, "17" INTEGER, "18" INTEGER, "19" INTEGER, "20" INTEGER,
        "21" INTEGER, "22" INTEGER, "23" INTEGER, "24" INTEGER, "25" INTEGER,
        "26" INTEGER, "27" INTEGER, "28" INTEGER, "29" INTEGER, "30" INTEGER,
        "31" INTEGER, "32" INTEGER, "33" INTEGER,
        Total_points INTEGER
    )
    """)

    # Create post_test
    exec_sql("""
    CREATE TABLE post_test (
        Sno INTEGER,
        "1" INTEGER, "2" INTEGER, "3" INTEGER, "4" INTEGER, "5" INTEGER,
        "6" INTEGER, "7" INTEGER, "8" INTEGER, "9" INTEGER, "10" INTEGER,
        "11" INTEGER, "12" INTEGER, "13" INTEGER, "14" INTEGER, "15" INTEGER,
        "16" INTEGER, "17" INTEGER, "18" INTEGER, "19" INTEGER, "20" INTEGER,
        "21" INTEGER, "22" INTEGER, "23" INTEGER, "24" INTEGER, "25" INTEGER,
        "26" INTEGER, "27" INTEGER, "28" INTEGER, "29" INTEGER, "30" INTEGER,
        "31" INTEGER, "32" INTEGER, "33" INTEGER,
        Total INTEGER
    )
    """)

    # Copy data into pretest (first 58 rows)
    exec_sql("""
    INSERT INTO pretest
    SELECT * FROM raw_data_1_HPV_CODED
    LIMIT 58
    """)

    # Copy data into post_test (first 58 rows)
    exec_sql("""
    INSERT INTO post_test
    SELECT * FROM raw_data_coded_hpv_2
    LIMIT 58
    """)

    # Copy data into demographic (first 58 rows)
    exec_sql("""
    INSERT INTO demographic
    SELECT * FROM raw_data_coded_demo_2
    LIMIT 58
    """)

    print("✅ demographic, pretest, and post_test tables created and filled.")


def export_summary_excel(output_path: str = OUTPUT_PATH):
    """Export demographic, pretest, and post_test tables to Excel."""
    df_demo = run_sql("SELECT * FROM demographic")
    df_pre = run_sql("SELECT * FROM pretest")
    df_post = run_sql("SELECT * FROM post_test")

    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        df_demo.to_excel(writer, sheet_name="demographic", index=False)
        df_pre.to_excel(writer, sheet_name="pretest", index=False)
        df_post.to_excel(writer, sheet_name="post_test", index=False)

    print(f"✅ summary_data.xlsx created at: {output_path}")


# ==============================
# Main Runner
# ==============================

if __name__ == "__main__":
    create_summary_tables()
    export_summary_excel()
    conn.commit()
    conn.close()
