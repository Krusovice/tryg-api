import requests
import json
URL = "http://localhost:8080"
key='mykey'



# Function for fetching value and printing return.
def fetch_value(key, timestamp):
	db_value = requests.get(f'{URL}/get_value?key={key}&timestamp={timestamp}')
	print(f'Fetching key:{key}, timestamp:{timestamp}. Returned: {db_value.text}')

# Listing all values in db.
db_items = requests.get(f'{URL}/list_items').json()
print('DB item list')
for i in db_items:
	print(i)

# Fetching value
timestamp=99
fetch_value(key,timestamp)

# Fetching value
timestamp=102
fetch_value(key,timestamp)

# Inserting new value of key-timestamp
new_item = {'key':'mykey', 'timestamp':102, 'value':'one_hundred_and_two'}
resp = requests.put(f'{URL}/insert_replace_value', json=new_item)
print(f'Replaced value for key:{new_item["key"]}, timestamp:{new_item["timestamp"]}')

# Fetching value from newly inserted key-timestamp
timestamp=102
fetch_value(key,timestamp)