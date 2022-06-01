import json
import requests

# url = "https://jsonplaceholder.typicode.com/posts"
# url = "https://api.instantwebtools.net/v1/airlines"
# url = "https://api.instantwebtools.net/v1/passenger/:id2"
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)
json_data = response.content.decode()
print(json_data)
with open('get_one.json', 'w') as file:
    json.dump(get_one.json, file)