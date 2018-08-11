name = 'hello,my python! '
two_name = "hahaha"
print(name)  #打印字符串
print(name.title())	#str.title()首字母大写
print(name.upper())	#str.upper()全部大写
print(name.lower())	#str.lower()全部小写

#字符串的拼接
print(name + two_name)	#直接用加号连接两个字符串
print(name + " " + "wuwuwu")
#制表符\t，换行符\n
print("\tname")
print("name\tname")
print("name\nname")
print("name\n\thaha")
a = name.rstrip()	#str.rstrip()可以消除字符串末位空白
print(a + "1")

#还可以剔除字符串开头的空白，或同时剔除字符串两端的空白。为此，可分别使用方法lstrip() 和strip() ：

#引号可以嵌套表示
b = 'you say"i am tom "'
print(b)

