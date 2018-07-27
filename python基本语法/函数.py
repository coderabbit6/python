#函数定义

def shuchu():

    print("我在输出")

shuchu()

#参数
def hello(person,me):
    print("hello,{0},i am {1}".format(person, me))

hello("zhangsan","libai")

#返回值
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

#help
help(print)
help(bijiao)

#九九乘法表
for r in range(1, 10):
    for c in range(1, r+1):
        print("r*c={0}".format(r*c), end="  ")
    print("")

#函数文档
def wendang(a):
    '''
    这是文档
    i will help you
    :param a: name
    :return: None
    '''
    print("haha:{0}".format(a))
help(wendang)
print(wendang.__doc__)





