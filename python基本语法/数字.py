# 2+3
# print(2 + 3)
# print(2 + 3*4)
# print((2 + 3)*4)

# #python提供和正常数学一致的运算方式
# print(2**3)	#两个*表示乘方运算

# #python的浮点数表示更为简单

# print(0.1*3)	#但需要注意的是，结果包含的小数位数可能是不确定的：0.30000000000000004
# print(0.3+1)

# #str()方法可将数字转化为字符串
# print(type(str(3)))	#<class 'str'>

print(12**40)
# is ,is not
a = 2
b = 2
s1 = "hello"
s2 = "hello"
print(a is b)
print(s1 is s2)

# help(list)
l = [2,3,4]
l2 = list(l)
print(l2)
print(id(l))
print(id(l2))
a = [1,2,3,4,5]
b = [i for i in a]
print(b)
a = [1,2,3,4,5]
b = [i for i in a]
c = [i*2 for i in a]
d = [i*3 for i in range(100) if i<20]
print(c)
print(d)
l = [['a',1],['b',2],['c',3]]
for w,n in l:
	print(w,"and",n)