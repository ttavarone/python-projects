import requests
import json
import re
import numpy as np

dataUrl = "https://data.cityofnewyork.us/resource/h9gi-nx95.json"

response = requests.get(url)
response.raise_for_status()

crashData = json.loads(response.text)