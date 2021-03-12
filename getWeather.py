import requests
import json

location = "palermo"
apiKey = "e416bdc0a08c56175bf8dc47e8b2ef04"
url = "http://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+apiKey

response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)

degree_sign= u'\N{DEGREE SIGN}'
temp = weatherData['main']['temp']
temp = round((temp-273.15)*(9/5)+32, 1)
recommendation = ""

if temp < 45.0:
    recommendation = "You should bring a heavy jacket."
elif temp >= 45.0 and temp < 65.0:
    recommendation = "You only need a light jacket."
elif temp >= 65.0 and temp <= 75.0:
    recommendation = "You may not even need a jacket... your choice."
elif temp > 72.5:
    recommendation = "You do not need a jacket."
elif temp > 78:
    recommendation = "You should wear shorts and a short sleeves."
else:
    recommendation = "The temperature is too extreme, use your judgement."

print("The current temperature is "+str(temp)+degree_sign)
print(recommendation)