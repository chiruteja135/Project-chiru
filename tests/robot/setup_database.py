import sqlite3

def execute_sql_script(sql_file_path, db_file_path):
    # Connect to the SQLite database (it will be created if it doesn't exist)
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()

    # Read the SQL script
    with open(sql_file_path, 'r') as sql_file:
        sql_script = sql_file.read()

    # Execute the SQL script
    cursor.executescript(sql_script)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    # Path to your SQL script and database file
    sql_file_path = 'setup.sql'
    db_file_path = 'database.db'

    # Execute the SQL script
    execute_sql_script(sql_file_path, db_file_path)
    print("Database setup completed.")
