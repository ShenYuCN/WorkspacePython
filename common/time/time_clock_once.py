"""

do something only once in the future 
"""

import time
originalTime = time.time()

	# temp = originalTime + 30 * 60 + random.randint(1,10*60)
	# temp = originalTime + 10 * index + random.randint(5,10)
temp = originalTime + random.randint(5,10)
print('temp:',int(temp),'originalTime:',int(originalTime))

while True:

	if time.time() > temp:
		print('temp:',int(temp),'now:',int(time.time()))
		print('here to do something')
		break
	else:
		print('sleeping')
		time.sleep(3)