#imports for drawing, time, getting restful api data, etc
from datetime import *
import pandas
import csv
import time
import json
import requests
from google.transit import gtfs_realtime_pb2
from protobuf_to_dict import protobuf_to_dict

#this gets the realtime data now in gtfs format; remember that the data is returned in protobuf format
feed = gtfs_realtime_pb2.FeedMessage()
response = requests.get("https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-bdfm", headers={"X-Api-Key": "60Xf2Sd7552LNP1KbqW9J5bEseFr9Vwp1lkJ5jSN"})
feed.ParseFromString(response.content)
# for entity in feed.entity:
# 	print(entity.vehicle)
subway_feed = protobuf_to_dict(feed)
realtime_data = subway_feed['entity']

collected_times = []

def station_time_lookup(train_data, station):
	for trains in train_data:
		if trains.get('trip_update', False) != False:
			uniqueTrainSchedule = trains['trip_update']
			#uniqueArrivalTimes = uniqueTrainSchedule['trip']
			for scheduledArrivals in uniqueTrainSchedule:
				if scheduledArrivals.get('stop_id', False) == station:
					timeData = scheduledArrivals['arrival']
					uniqueTime = timeData['time']
					if uniqueTime != None:
						collected_times.append(uniqueTime)

def parseCsv(file):
	#df = pandas.read_csv(file, usecols=['arrival_time', 'stop_id'])
	df = pandas.read_csv(file, usecols=['arrival_time', 'stop_id'], index_col="stop_id")
	print(df.loc["F03S"])
	#print(first, "\n\n\n")
	# if 'F03S' in df.values:
	# 	print(df.loc['F03S'])
	# else:
	# 	print("It does not exist")


	# arrivals = {"times":[]}
	# with open(file, 'r') as csvFile:
	# 	csvReader = csv.DictReader(csvFile)
	# 	for rows in csvReader:
	# 		arrivals["times"] = rows
	
stationName = 'D21S'

station_time_lookup(realtime_data, stationName)

# Sort the collected times list in chronological order (the times from the data
# feed are in Epoch time format)
collected_times.sort()

# Pop off the earliest and second earliest arrival times from the list
nearest_arrival_time = collected_times[0]
second_arrival_time = collected_times[1]

# Grab the current time so that you can find out the minutes to arrival
current_time = int(time.time())
time_until_train = int(((nearest_arrival_time - current_time) / 60))

# This final part of the code checks the time to arrival and prints a few
# different messages depending on the circumstance
if time_until_train > 3:
    print(f"""
It's currently {time.strftime("%I:%M %p")}
The next Brooklyn-bound B/D train from
Broadway-Lafayette Station arrives in
{time_until_train} minutes at {time.strftime("%I:%M %p", time.localtime(nearest_arrival_time))}""")
elif time_until_train <= 0:
    print(f"""
Welp... You *just* missed the train. (╯°□°）╯︵ ┻━┻
Ah well, the next train will arrive at {time.strftime("%I:%M %p", time.localtime(second_arrival_time))}""")
else:
    print(f"""
HURRY UP YOU HAVE {time_until_train} MINUTES TO GET TO
BROADWAY-LAFAYETTE IF YOU WANT TO GET HOME!
THE TRAIN GETS IN AT {time.strftime("%I:%M %p", time.localtime(nearest_arrival_time))}""")


# These are useful print statments used for script debugging, commented out
#
# for times in collected_times:
#     print(times, "=", time.strftime("%I:%M %p", time.localtime(times)))
# print(collected_times)
# print(nearest_arrival_time)
# print(second_arrival_time)
# print(time_until_train)