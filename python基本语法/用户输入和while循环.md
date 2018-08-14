## 用户输入
#### input()函数
- 用户输入数据会以字符串形式存入变量
```
num = input("请输入一个数字： ")
print(num)
```
- int()函数可以将字符串强制转换成数字
```
a = int('30')
print(a)
```
- 取模运算：求模运算符 （%）是一个很有用的工具，它将两个数相除并返回余数（可以用来判断奇偶）
```
print(3%2)
print(5%4)
```

## while循环
#### while循环的使用
```
a = 9
while a>=0:
	print(a)
	a--
```

#### 让用户选择何时退出循环
```直到用户输入quit时退出循环
s = ''
while a !='quit':
	s = input()
	if s != 'quit': 
		print(s)
```

- 设置标志判断情况，及时退出循环
```
s = " "
flag = True
while flag:
	s = input()
	if s == 'quit':
		flag = Flase
	else:
		print(s)
```
- 使用break退出循环
```
a = 4
while True:
	print(a)
	a++
	if a == 9:
		break
``` 
- 使用continue跳过循环
```
a = 1
while a <= 100:
	if a % 2 ==0 :
		continue
	print(a)
	a++
```

#### 用while循环来处理列表和字典
- 在列表之间移动元素
```
a = [1,2,3,4,5]
b = []
while a:
	b.append(a.pop())
print(b)
```

- 删除包含特定值的所有列表元素
```
a = [1,2,3,4,5,63,3,3,4,5]
while 3 in a:
	a.remove(3)
print(a)
```
- 使用用户输入来填充字典
```
a = {}
flag = True
while flag :
	id = input("输入你的学号：")
	name = input("请输入你的名字：")
	a[id] = name
	repeat = input(还有人吗？yes/no)
	if repeat == 'no':
		flag = False
print(a)
```
