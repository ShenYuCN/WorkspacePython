"""

Execute once every other time

And random 

10s   random(1-5)
"""
import time
import random
originalTime = time.time()
index = 1


temp = originalTime + 10 * index + random.randint(1,5)
print('now:',int(originalTime),'temp:',int(temp))


while True:


	if time.time() > temp:
		print('now:',int(time.time()),'temp:',int(temp))

		print('here to do something -------------------')
		index += 1
		temp = originalTime + 10 * index + random.randint(1,5)
		print('now:',int(time.time()),'new_temp:',int(temp))
		time.sleep(3)
	else:
		print('sleeping')
		time.sleep(3)



"""


now: 1537795403 temp: 1537795417
sleeping
sleeping
sleeping
sleeping
sleeping
now: 1537795418 temp: 1537795417
here to do something -------------------
now: 1537795418 new_temp: 1537795428
sleeping
sleeping
sleeping
now: 1537795430 temp: 1537795428
here to do something -------------------
now: 1537795430 new_temp: 1537795437
sleeping
sleeping
now: 1537795439 temp: 1537795437
here to do something -------------------
now: 1537795439 new_temp: 1537795446

"""