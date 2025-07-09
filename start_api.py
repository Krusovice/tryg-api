import uvicorn
from db_functions import connect_db, save_and_close_db, list_database_values, insert_replace_data

# Creating database.
DB_PATH = "database.db"
conn, cursor = connect_db(DB_PATH)

# Inserting some values if database is empty.
database_values = list_database_values(cursor)
if not database_values:
	key = "mykey"
	timestamp, value = 100,'one_hundred'
	insert_replace_data(cursor,key,timestamp,value)

	timestamp, value = 101,'one_hundred_and_one'
	insert_replace_data(cursor,key,timestamp,value)
	save_and_close_db(conn)

if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8080)