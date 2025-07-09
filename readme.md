# Tryg-API-Test
A simple Python-SQLite database and API that allows for interacting with database using API calls.

# Database
The database uses sqlite with one table and following columns:

- `key` *(TEXT)* - key.
- `timestamp` *(INTEGER)* - timestamp.
- `value` *(TEXT)* - value to be returned with get method.
- `id` *(PRIMARY KEY)* - automatically generated per insert/replacement.


The database contains functions to support API calls.
The id is utilized for tracking all generated values. Can be used to assess and comply with concurrent API calls.

# API
Created with FastAPI with API calls for sql functions to allow for listing, inserting, replacing and fetching values from database.

# Setup
- python version 3.11.2
- Install dependencies and run the API:

```
python -m venv venv
source venv/bin/activate # For windows: venv/scripts/activate
pip install -r requirements.txt
```

# Run API and Test
`python start_api.py` - Initiates the api on port 8080.
`python test_api.py` - Runs a few api calls to verify expected behaviour.

# Examples of API Calls

Listing all items in database. 
Returning most recent "value" for combination of key and timestamp.
`curl http://localhost:8080/list_values`

Fetching value for a specified key and timestamp input.
Value is returned for timestamp equal or less (closest) to timestamp input.
None is returned if key doesnt match key input.
None is returned if all timestamp values are larger than timestamp input.
`curl "http://localhost:8080/get_value?key=mykey&timestamp=102"`

Insert or replace a value for combination of key and timestamp.
Note that a history of all values are stored and can be retrived using id column.
`curl -X PUT http://localhost:8080/insert_replace_value 
	-H "Content-Type: application/json" 
	-d "{\"key\": \"mykey\", \"timestamp\": 102, \"value\": \"one_hundred_and_two\"}"
`
