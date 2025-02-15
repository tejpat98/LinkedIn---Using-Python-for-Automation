import requests
import json

base_url = "https://api.upcitemdb.com/prod/trial/lookup"

parameters = {"upc": "025000044908"}

response = requests.get(base_url, params=parameters)
info = json.loads(response.text)
item = info["items"][0]
title = item["title"]
brand = item["brand"]

print(f'title: {title}, \nbrand: {brand}')