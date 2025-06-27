import sqlite3

def connect_to_db(db_path):
    """Connects to a SQLite database and returns the connection."""
    try:
        conn = sqlite3.connectt(db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM non_existent_table')  
        results = cursor.fetchall()
        return results
    except Exception as e:
        print("Database error:", e)

if __name__ == "__main__":
    data = connect_to_db('test.db')
    print(data)
