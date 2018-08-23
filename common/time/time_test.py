import time
# 当前时间
now = time.time()
print('now',now)

localtime = time.localtime(time.time())
print('localtime',localtime)

strftime = time.strftime('%Y-%m-%d %H:%M:%S',localtime)
print('strftime',strftime)



# 时间戳字符串  格式化成 日期格式
timestamp = 1534525415
time_struct = time.localtime(timestamp)
print('time_stuct',time_struct)

final_format_time = time.strftime('%Y-%m-%d %H:%M:%S',time_struct)
print('final_format_time',final_format_time)
