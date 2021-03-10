#imports for drawing, time, getting restful api data, etc
from tkinter import *
from datetime import *
import time
import json
import requests

#main part that gets restful data
#returns the json file, writes the files to a txt file
def getStations():
	response = requests.get("http://mtaapi.herokuapp.com/stations")
	stations = response.json()

	#opens a txt file and writes the stations content to the text file
	#f = open("stations.txt", "w")
	#for station in stations['result']:
		#f.write(str(station))
	return stations

def findArrivals(id, stations):
	today = datetime.today()
	currTime = today.strftime("%H:%M:%S")
	delta1 = timedelta(minutes=5)
	delta2 = timedelta(minutes=10)
	delta3 = timedelta(minutes=30)

	# response = requests.get("http://mtaapi.herokuapp.com/api?id="+id)
	response = requests.get("http://mtaapi.herokuapp.com/api?id=F03N")
	times = response.json()
	times = times['result']
	for time in times['arrivals']:
		# arrivalTime = str(time)
		arrivalTime = datetime.strptime(str(time), "%H:%M:%S")
		print(arrivalTime)

def searchStationName(name):
	pass
def searchStationId(id):
	pass


#the data coming back from this api is already in json format from response.json()
#print(type(stations))

# for station in stations['result']:
# 	if "F" in station['id'] and "Parsons" in station['name']:
# 		print(station['id'])
# 		print(station['name'])

# stations = getStations()
# for station in stations['result']:
# 	print(station['id'])
# 	print(station['name'])