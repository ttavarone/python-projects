import time

punches = []

name = input()
punchTime = time.time()

punchTime = time.strftime('%H:%M:%S', time.localtime(punchTime))

print('%s punch at %s' % (name, punchTime))