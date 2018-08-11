a = ['2','5','3','6','4']

#使用方法sort() 对列表进行永久性排序
a.sort()
print(a)

#你还可以按与字母顺序相反的顺序排列列表元素，为此，只需向sort() 方法传递参数reverse=True 。
a.sort(reverse = True)
print(a)

#临时排序
print(sorted(a))
print(a)

a.reverse()
print(a)

print(len(a))