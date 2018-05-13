import requests
#URL = "https://www.geeksforgeeks.org/data-structures/"
URL="https://www.yahoo.com"
r = requests.get(URL)
print(r.content)