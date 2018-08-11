### 条件测试
#### 检查是否相等
- 用==来判断，相等则返回True
```
print((1+1)==2)
```
- 判断时区分大小写

#### 检查不相等
- 用!=来判断

#### 比较数字
- 用<,>,<=,>=来判断

#### 检查多个条件
- 用and，or来连接两个或者多个条件
- and表示且，必须所连接两边都满足条件才是True
- or表示或，只要两个条件其中有一个满足就是True

#### 判断特定的值是否已包含在列表中
- 用关键字in来判断在列表中
```
a = (1,2,3,4,5)
print(1 in a)

>True
```
- 用关键字not in来判断不在列表中
```
a = (1,2,3,4,5)
print(1 not in a)

>False
```
#### 布尔值，布尔表达式
- 只有True，False两种值
```
b1 = 1==2
bi = 2==2
```
### if语句
#### 简单的if语句
```
a = 1
if a ==1:
	print('haha')
```
#### if-else语句
```
a = 3
if a>0:
	print('正数')
else:
	print('负数')
```
#### if-elif-else语句
```
a = 3
if a>0:
	print('正数')
elif a<0:
	print('负数')
else:
	print('零')
```
#### 使用多个elif
- 多个限制条件
- else语句有些情况可以省去
#### 测试多个条件
- 在测试多个条件时可以用多个if来判断
```
a = 3
if a ==3
	print('you are right')
if a ==2
	print('low')
if a ==4
	print('high')
......
```
- python里没有swith-case语句
### 使用if语句检查列表
#### 检查特殊元素
```
for i in range(4):
	if(i == 2):
		print(i)
```
#### 确定列表是否为空
```
requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + ".")
	print("\nFinished making your pizza!")
else:print("Are you sure you want a plain pizza?)
```
#### 使用多个列表
```
available_toppings = ['mushrooms', 'olives', 'green peppers',
						'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")
```
#### if语句的格式
- 判断符号与条件之间最好有空格