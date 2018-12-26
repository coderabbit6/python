## 内置数据结构
- 列表
- 元组
- 集合
- 字典

### 列表
#### 生成列表
`
l = []
l1 = [10,2,3,4]
l2 = list(l1)
`

#### 列表常用操作
- 访问
- 分片
`
#访问列表元素
l = [1,2,3,4,5]
print(l[2])
print(l[-1])
`

`
#分片操作
l = [1,2,3,4,5]
print(l[:])
print(l[2:])
print(l[:3])
#步长
print(l[1:5:2])
`

- 注意分片产生新的列表

#### 列表常用操作
- del删除(不生成新的列表)
- +可以连接两个列表
- 乘以一个常数
- in

#### 列表的遍历
- 用for i in list语法结构:
   - in后面应该是可以迭代的内容
`
l = [1,2,3,4,5,6]
for i in l:
	print(i)
`
- range()
`
for i in range(5):
	print(i)
print(type(range(4)))
`
- 双层列表遍历
`
l = [['a',1],['b',2],['c',3]]
for w,n in l:
	print(w,"and",n)
`

#### 列表内涵
- 生成列表
`
a = [1,2,3,4,5]
b = [i for i in a]
c = [i*2 for i in a]
d = [i*3 for i in range(100) if i<20]
`