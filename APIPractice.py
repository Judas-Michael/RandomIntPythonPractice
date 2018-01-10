pip install requests

import requests
import os

set OMDB_KEY=abcd1234


key = os.environ['OMDB_KEY'] #Read key from environment variable
base_url = 'http://www.omdbapi.com/'
movie = input('What movie name?')
params = { 'apikey' : key, 't' : movie }
data = requests.get(base_url, params ).json()

print(data) # Just for debugging
print("Rating for that movie: ")
print(data['Ratings'][0]['Value'])