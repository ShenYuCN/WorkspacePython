"""

Execute once every other time

10s 
"""
import time
originalTime = time.time()
index = 1

while True:

	temp = originalTime + 10 * index
	print('now:',int(time.time()),'temp:',int(temp))


	if time.time() > temp:
		print('here to do something -------------------')
		print('now:',int(time.time()),'temp:',int(temp))

		index += 1
		time.sleep(3)
	else:
		print('sleeping')
		time.sleep(3)