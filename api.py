from fastapi import FastAPI, HTTPException
from db_functions import connect_db, save_and_close_db, insert_replace_data, list_database_values, fetch_key_timestamp_value
from pydantic import BaseModel
from start_api import DB_PATH

# Class for pydantic validation
class Item(BaseModel):
    key: str
    timestamp: int
    value: str

# API and functions
app = FastAPI()

@app.get("/list_items")
def list_items():
    conn, cursor = connect_db(DB_PATH)
    items = list_database_values(cursor)
    save_and_close_db(conn)
    return [{'key':item[0], 'timestamp':item[1], 'value':item[2], 'id':item[3]} for item in items]

@app.get("/get_value")
def get_value(key: str, timestamp: int):
    conn, cursor = connect_db(DB_PATH)
    value = fetch_key_timestamp_value(cursor, key, timestamp)

    if value is None:
        raise HTTPException(status_code=404, detail="No value found for key-timestamp combination.")
    else:
        return value

@app.put("/insert_replace_value")
def insert_replace_value(item: Item):
    key = item.key
    timestamp = item.timestamp
    value = item.value

    conn, cursor = connect_db(DB_PATH)

    # Checkign if value exists for key-timestamp combination
    # For returning a message on the action.
    value_exists = fetch_key_timestamp_value(cursor, key, timestamp)

    if value_exists:
        message = 'Replacing existing item'
    else:
        message = 'Creating new item'

    insert_replace_data(cursor, key, timestamp, value)
    save_and_close_db(conn)

    return message