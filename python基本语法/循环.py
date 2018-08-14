# ##求和
# #for循环
# a = 0
# for i in range(6):
#     a += i
#     print(i)
# print(a)

# #while循环

# b=0
# i=1
# while i<=5:
#     b+=i
#     i=i+1
# print(b)

# a = [1,2,3,4,5]
# b = []
# while a:
# 	b.append(a.pop())
# print(b)
# a = [1,2,3,4,5,63,3,3,4,5]
# while 3 in a:
# 	a.remove(3)
# print(a)
a = {}
flag = True
while flag :
	id = input("输入你的学号：")
	name = input("请输入你的名字：")
	a[id] = name
	repeat = input("还有人吗？yes/no  ")
	if repeat == 'no':
		flag = False
print(a)