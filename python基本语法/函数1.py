# a = 2
# b = 3
# a,b = b,a
# print(a)
# print(b)
# def get_max(a,b):
# 	if a > b:
# 		return a
# 	if a <= b:
# 		return b

# print(get_max(2,3))
# NAME = ["wangwang","shishi"]
# a = 3
# def s1():
# 	global a
# 	a = 5
# 	# NAME = [1,2,3,4]
# 	NAME.append('yaoyao')

# s1()
# print(NAME)
# print(a)


# def infor(id,name):
# 	s_infor = {'id' : id,'name' :name}
# 	return s_infor
# a = infor('01','xiaohong')
# print(a)

# def list_append(List1,List2):
# 	for i in range(5):
# 		List1.append(i)
# 		List2[i] = List1.pop()
# a = [1,2,3,4,5,6,7]
# b = [2]
# list_append(b,a)
# print(a)
# print(b)

def show(*num):
	for i in num:
		print(i)
show(1,2,3,4)
show(5,6)