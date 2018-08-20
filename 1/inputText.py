# while True:
# 	reply = input('please enter txt\<n></n>')
# 	if reply == 'aaa':break
# 	print(reply.upper())

import sys
sys.stdout = open('log.txt','a')
print('hello')
print('JD')
sys.stdout.close()