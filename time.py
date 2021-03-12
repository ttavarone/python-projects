import time

now = time.time()
for secs in range(5):
	time.sleep(1)
later = time.time()

print(round(abs(now - later), 2))