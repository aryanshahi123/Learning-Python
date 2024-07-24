import requests
import json

url = "https://jsonguide.technologychannel.org/quotes.json"

f = requests.get(url)
data = json.loads(f.text)


for quote in data:
    print(quote['text'])