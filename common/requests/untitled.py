import time
import random
originalTime = time.time()

	# temp = originalTime + 30 * 60 + random.randint(1,10*60)
	# temp = originalTime + 10 * index + random.randint(5,10)
temp = originalTime + random.randint(5,10)
print('temp:',int(temp),'now:',int(originalTime))

while True:



	if time.time() > temp:
		print('zheli break')
		break
	else:
		time.sleep(5)