import sqlite3
def connect_db(database_path):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    initiate_database(cursor)
    return conn, cursor

def initiate_database(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS important_data (
            id INTEGER PRIMARY KEY,
            key_ TEXT NOT NULL,
            timestamp INTEGER,
            value TEXT
            );
        """)

def save_and_close_db(conn):
    conn.commit()
    conn.close()

def insert_replace_data(cursor, key, timestamp, value):
    cursor.execute("""
        insert or replace into important_data (key_, timestamp, value) values (?, ?, ?)
        """, (key, timestamp, value))

def list_database_values(cursor):
    cursor.execute("""
        select key_, timestamp, value, id from important_data
        order by key_, timestamp desc, id desc;
        """)
    return cursor.fetchall()

def fetch_key_timestamp_value(cursor, key, timestamp):
    cursor.execute("""
        select value from important_data 
        where key_=? and timestamp <=?
        order by timestamp desc, id desc limit 1;
        """, (key,timestamp))

    value = cursor.fetchone()
    if value == None:
        return None
    else:
        return value[0]