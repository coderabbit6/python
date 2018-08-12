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