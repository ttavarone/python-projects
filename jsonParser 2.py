import json
from datetime import datetime

#variables to count different calls
total = 0
lightsCall = 0
fanCall = 0
unknownCall = 0
questionCall = 0
randomCall = 0
setAlarmCall = 0
setTimerCall = 0

minDat = datetime.today()
maxDat = datetime.strptime('2021-2-1', '%Y-%m-%d')

#constant for the json data
GOOGLE_DATA = 'MyActivity.json'

def maxDate(date1, date2):
  if(date1 > date2):
    return date1
  else:
    return date2
    
def minDate(date1, date2):
  if(date1 < date2):
    return date1
  else:
    return date2

def percentTotal(x):
  return str("{:.2f}".format((x/total)*100))+'%'

#opens stream to load json data
f = open(GOOGLE_DATA)
#loads it as a json object for parsing
loadedGoogleData = json.load(f)

#goes thru the loaded data to find calls to assistant
for data in loadedGoogleData:
  total+=1
  if(data['header'] == 'Assistant'):
    date = str(data['time'])
    date = date[:10]
    dateObj = datetime.strptime(date, '%Y-%m-%d')
    #print('Date of entry: '+date)
    #print(data.keys())
    #print()
    #print(data['title'])
    #print(str(data['time']))
    if 'locationInfos' in data:
      print(data['locationInfos']['url'])
    
    maxDat = maxDate(dateObj, maxDat)
    minDat = minDate(dateObj, minDat)
    
    title = data['title']
    #count calls
    if 'light' in title:
      lightsCall+=1
    if 'fan' in title:
      fanCall+=1
    if 'Unknown' in title:
      unknownCall+=1
    if 'what' in title or 'who' in title or 'when' in title or 'how' in title or 'why' in title:
      questionCall+=1
    if 'alarm' in title:
      setAlarmCall+=1
    if 'timer' in title:
      setTimerCall+=1
    
#date comparison for range of dates
#***will need to format out time later***

print('max='+str(maxDat))
print('min='+str(minDat))

print("Calls to change lights: "+str(lightsCall))
print("Calls to change fan: "+str(fanCall))
print("Unknown calls: "+str(unknownCall))
print("Question calls: "+str(questionCall))
print("Set Alarm calls: "+str(setAlarmCall))
print("Set Timer calls: "+str(setTimerCall))
#total counted vs total expected
print("Total calls expected: "+str(total))
totalCounted=lightsCall+fanCall+unknownCall+questionCall+randomCall+setAlarmCall+setTimerCall
print("Total calls counted: "+str(totalCounted))
difference = total-totalCounted
print("Unaccounted calls: "+str(difference))

#Percentage of calls to totals
print("Lights: "+percentTotal(lightsCall))
print("Fan: "+percentTotal(fanCall))
print("Questions: "+percentTotal(questionCall))
print("Unknown: "+percentTotal(unknownCall))
print("Random: "+percentTotal(randomCall))
print("Set Alarm: "+percentTotal(setAlarmCall))
print("Set Timer: "+percentTotal(setTimerCall))