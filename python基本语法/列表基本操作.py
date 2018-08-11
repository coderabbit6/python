#修改、添加和删除元素
a = ['Tom','bob','Lili','Cuihua']
a[0] = 'naya'		#可直接修改列表元素
print(a)

#添加元素
#在列表末尾添加:append(值)方法
a.append('xiaowu')
print(a)

#在列表任意位置添加：insert(索引，值)方法 
a.insert(2,'xiaoling')	#注意是在索引前插入
print(a)

#删除元素
#使用del(索引)方法
del(a[0])
print(a)		#注意用del方法后无法再访问被删除元素

#使用pop(索引)方法：默认弹出末尾元素，并继续使用弹出的值
b = a.pop()	#末尾元素弹出
c = a.pop(0)#第一个元素弹出
print(b)	#弹出的元素
print(c)
print(a)	#之后的列表

#根据值来删除元素 remove(值)方法
a.remove('Lili')
print(a)

