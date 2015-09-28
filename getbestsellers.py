#Using NY times API: http://developer.nytimes.com/docs/books_api/Books_API_Best_Sellers

import requests
import json
import datetime
from dates import datesList


#API Key for NY Times
query_params = {'api-key': '5381b9be882d1bb43424ff4d9724131b:13:71711206'}

# Create JSON file with current date in name
dt = str(datetime.datetime.now())

# Get data
for date in datesList:
    date = str(date)
    endpoint = 'http://api.nytimes.com/svc/books/v3/lists/'+date+'/picture-books.json'
    response = requests.get(endpoint, params=query_params)
    datadict = json.loads(response.text)
    
# Save to file
    if datadict['num_results'] != 0:
        with open('bestsellers_'+dt+'.json', 'a') as f:
            data = response.json()
            json.dump(data, f)
            f.write('\n')