#函数定义
- ```
  def shuchu():

    print("我在输出")

  shuchu()
   ```

#参数
```
def hello(person,me) :

    print("hello,{0},i am {1}".format(person, me))
    
hello("zhangsan","libai")
```
#返回值
###无论有无返回值都用return
###无返回值时return None
```
def bijiao(a):
    if a>250:
        return "我大"
    elif a<250:
        return "你大"
    else :
        return "你是250"
print(bijiao(300))
print(bijiao(250))
print(bijiao(100))
```
#help
`help(print)`

`help(bijiao)`

#九九乘法表
```
for r in range(1,10):
    for c in range(1,r+1):
        print("r*c={0}".format(r*c),end="  ")
    print("")
 ```
#函数文档
```angular2html
    '''
        这是文档
    '''
```

