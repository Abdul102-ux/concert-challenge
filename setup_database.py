import sqlite3

def setup_database():
    print("Connecting to the database...")
    conn = sqlite3.connect('concerts.db')
    cursor = conn.cursor()

    print("Creating bands table...")
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS bands (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        hometown TEXT NOT NULL
    )
    ''')

    print("Creating venues table...")
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS venues (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        city TEXT NOT NULL
    )
    ''')

    print("Creating concerts table...")
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS concerts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        band_id INTEGER NOT NULL,
        venue_id INTEGER NOT NULL,
        date TEXT NOT NULL,
        FOREIGN KEY (band_id) REFERENCES bands(id),
        FOREIGN KEY (venue_id) REFERENCES venues(id)
    )
    ''')

    print("Committing changes and closing connection...")
    conn.commit()
    conn.close()
    print("Database setup complete.")

if __name__ == "__main__":
    setup_database()
