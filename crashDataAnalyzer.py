import requests
import json
import re
import numpy as np

dataUrl = "https://data.cityofnewyork.us/resource/h9gi-nx95.json"

response = requests.get(dataUrl)
response.raise_for_status()

crashData = response.json()

#gathers all the recorded zip codes and boroughs
zipCodes = set(zc['zip_code'] for zc in crashData if 'zip_code' in zc.keys())
boroughs = set(b['borough'] for b in crashData if 'borough' in b.keys())

#we will count how many times each borough is mentioned compare it to the others to find the most
# accident prone borough
incidentByBoro = []

unrecordedBoro = 0
for borough in boroughs:
	boroCount = 0
	for incident in crashData:
		if 'borough' in incident.keys():
			if incident['borough'] == borough:
				boroCount += 1
		else:
			unrecordedBoro += 1
	incidentByBoro.append((borough, boroCount))
#incidentByBoro.append(('unrecordedBoro', unrecordedBoro))

incidentByBoro.sort(key= lambda x: x[1])
#print(incidentByBoro)

#this does the same thing as above but it finds the most accident prone zip codes
incidentByZip = []

unrecordedZip = 0
for zipCode in zipCodes:
	zipCount = 0
	for incident in crashData:
		if 'zip_code' in incident.keys():
			if incident['zip_code'] == zipCode:
				zipCount += 1
		else:
			unrecordedZip += 1
	incidentByZip.append((zipCode, zipCount))
#incidentByZip.append(('unrecordedZip', unrecordedZip))

incidentByZip.sort(key= lambda x: x[1])
#print(incidentByZip)

#find the max for both lists of incidents
print(max(incidentByBoro, key= lambda x:x[1]))
print(max(incidentByZip, key= lambda x:x[1]))