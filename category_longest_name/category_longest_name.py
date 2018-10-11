import simplejson
str = open('cate').read()
all_dict=simplejson.loads(str)
all_list = list(all_dict.values())
print(all_list[0])
# for item in all_dict.items():
# 	print('aaa:',item)