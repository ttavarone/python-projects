import requests
import json
import smtplib
import datetime
import time

#making a test time for today, a little later after writing the program
todayTestTime = datetime.datetime(2021, 3, 12, 22, 14, 0)

def getWeather(location):
	apiKey = "e416bdc0a08c56175bf8dc47e8b2ef04"
	url = "http://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+apiKey

	response = requests.get(url)
	response.raise_for_status()

	weatherData = json.loads(response.text)

	#degree_sign= u'\N{DEGREE SIGN}'
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

	return 'The current temperature is '+str(temp)+' degrees.'+'\n'+recommendation
	# print("The current temperature is "+str(temp)+degree_sign)
	# print(recommendation)

def smtpMail(recipient, subject, body):
	smtpServer = 'smtp.gmail.com'
	loginEmail = 'ttavarone@gmail.com'
	password = 'hyrdetxanptsxrhg'

	if not recipient or not subject or not body:
		return False

	smtpObj = smtplib.SMTP(smtpServer, 587)
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.login(loginEmail, password)
	smtpObj.sendmail(loginEmail, recipient, 'Subject: '+subject+' \n'+body)
	smtpObj.quit()

#gets the start time, we will check the time elapsed since start of sending email
startTime = time.time()

#time.sleep until the time comes to send the email
while datetime.datetime.now() < todayTestTime:
	time.sleep(1)

currentTime = time.strftime('%H:%M:%S', time.localtime(time.time()))
# weather = getWeather('new&york,ny')
smtpMail('ttavarone@me.com', currentTime, 'This is a test email.')

endTime = time.time()
elapsed = endTime - startTime
minutes = round(elapsed / 60)
elapsed %= 60
seconds = round(elapsed)

print('%d minutes and %d seconds elapsed since we started.' % (minutes, seconds))