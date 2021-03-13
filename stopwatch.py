import time

input()
print('Started')
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
	while True:
		input()
		laptime = round(time.time()-lastTime,2)
		print('Lap %d: Time: %f' % (lapNum, laptime), end='')
		lapNum += 1

except KeyboardInterrupt:
	print('\nDone')