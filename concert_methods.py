import sqlite3

def get_band_for_concert(concert_id):
    conn = sqlite3.connect('concerts.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT bands.* FROM bands
    JOIN concerts ON bands.id = concerts.band_id
    WHERE concerts.id = ?
    ''', (concert_id,))
    band = cursor.fetchone()
    conn.close()
    return band

def get_venue_for_concert(concert_id):
    conn = sqlite3.connect('concerts.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT venues.* FROM venues
    JOIN concerts ON venues.id = concerts.venue_id
    WHERE concerts.id = ?
    ''', (concert_id,))
    venue = cursor.fetchone()
    conn.close()
    return venue

def get_concerts_for_venue(venue_id):
    conn = sqlite3.connect('concerts.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT concerts.* FROM concerts
    WHERE concerts.venue_id = ?
    ''', (venue_id,))
    concerts = cursor.fetchall()
    conn.close()
    return concerts

def get_bands_for_venue(venue_id):
    conn = sqlite3.connect('concerts.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT DISTINCT bands.* FROM bands
    JOIN concerts ON bands.id = concerts.band_id
    WHERE concerts.venue_id = ?
    ''', (venue_id,))
    bands = cursor.fetchall()
    conn.close()
    return bands

def is_hometown_show(concert_id):
    conn = sqlite3.connect('concerts.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT (bands.hometown = venues.city) AS hometown_show
    FROM concerts
    JOIN bands ON concerts.band_id = bands.id
    JOIN venues ON concerts.venue_id = venues.id
    WHERE concerts.id = ?
    ''', (concert_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] == 1

def get_introduction(concert_id):
    conn = sqlite3.connect('concerts.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT "Hello " || venues.city || "!!!!! We are " || bands.name || " and we're from " || bands.hometown AS introduction
    FROM concerts
    JOIN bands ON concerts.band_id = bands.id
    JOIN venues ON concerts.venue_id = venues.id
    WHERE concerts.id = ?
    ''', (concert_id,))
    introduction = cursor.fetchone()
    conn.close()
    return introduction[0]

def play_in_venue(band_name, venue_title, date):
    conn = sqlite3.connect('concerts.db')
    cursor = conn.cursor()

    
    cursor.execute('SELECT id FROM bands WHERE name = ?', (band_name,))
    band_result = cursor.fetchone()
    if band_result is None:
        print(f"Band '{band_name}' not found.")
        conn.close()
        return
    band_id = band_result[0]

    
    cursor.execute('SELECT id FROM venues WHERE title = ?', (venue_title,))
    venue_result = cursor.fetchone()
    if venue_result is None:
        print(f"Venue '{venue_title}' not found.")
        conn.close()
        return
    venue_id = venue_result[0]

    
    cursor.execute('SELECT id FROM concerts WHERE band_id = ? AND venue_id = ? AND date = ?', (band_id, venue_id, date))
    if cursor.fetchone() is not None:
        print(f"Concert by band '{band_name}' at venue '{venue_title}' on {date} already exists.")
        conn.close()
        return

    
    cursor.execute('INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?)',
                   (band_id, venue_id, date))
    
    conn.commit()
    conn.close()
    print(f"Added concert for band '{band_name}' at venue '{venue_title}' on {date}.")

def get_all_introductions(band_name):
    conn = sqlite3.connect('concerts.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT DISTINCT "Hello " || venues.city || "!!!!! We are " || bands.name || " and we're from " || bands.hometown AS introduction
    FROM concerts
    JOIN bands ON concerts.band_id = bands.id
    JOIN venues ON concerts.venue_id = venues.id
    WHERE bands.name = ?
    ''', (band_name,))
    introductions = cursor.fetchall()
    conn.close()
    return [intro[0] for intro in introductions]


def get_most_performances():
    conn = sqlite3.connect('concerts.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT bands.name FROM bands
    JOIN concerts ON bands.id = concerts.band_id
    GROUP BY bands.id
    ORDER BY COUNT(concerts.id) DESC
    LIMIT 1
    ''')
    band = cursor.fetchone()
    conn.close()
    return band[0]

def get_concert_on_date(venue_title, date):
    conn = sqlite3.connect('concerts.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT concerts.* FROM concerts
    JOIN venues ON concerts.venue_id = venues.id
    WHERE venues.title = ? AND concerts.date = ?
    LIMIT 1
    ''', (venue_title, date))
    concert = cursor.fetchone()
    conn.close()
    return concert

def get_most_frequent_band(venue_title):
    conn = sqlite3.connect('concerts.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT bands.name FROM bands
    JOIN concerts ON bands.id = concerts.band_id
    JOIN venues ON concerts.venue_id = venues.id
    WHERE venues.title = ?
    GROUP BY bands.id
    ORDER BY COUNT(concerts.id) DESC
    LIMIT 1
    ''', (venue_title,))
    band = cursor.fetchone()
    conn.close()
    return band[0]
