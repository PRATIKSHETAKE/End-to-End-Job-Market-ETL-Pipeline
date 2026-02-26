import pandas as pd
import sqlite3

def load_data_to_db():
    print("Starting database load process...")
    try:
        df = pd.read_csv("clean_jobs_data.csv")
    except FileNotFoundError:
        print("Error: 'clean_jobs_data.csv' not found.")
        return

    db_name = "jobs_database.db"
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    table_name = "tech_jobs"

    df.to_sql(table_name, conn, if_exists='replace', index=False)
    print(f"Data successfully loaded into the '{table_name}' table in {db_name}!")


    cursor.execute(f"SELECT [Job Title], Company, Extracted_Skills FROM {table_name} LIMIT 3")
    rows = cursor.fetchall()
    print("\nDatabase Preview:")
    for row in rows:
        print(f"- {row[0]} | {row[1]} | Skills: {row[2]}")

    conn.close()

if __name__ == "__main__":
    load_data_to_db()
