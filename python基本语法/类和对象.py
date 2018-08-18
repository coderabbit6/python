# class Dog():
# 	def __init__(self,name,age):
# 		self.name = name
# 		self.age = age
# 	def sit(self):
# 		print(self.name + " is sitting now")
# 	def roll_over(self):
# 		print(self.name + " is rooling now")

# my_dog = Dog('xiaojuan',20)
# my_dog.roll_over()
# my_dog.sit()
# print(my_dog.name)

# class Student():
# 	def __init__(self,id,name,age):
# 		self.id = id
# 		self.name = name
# 		self.age = age
# 	def getinfo(self):
# 		info = {'id':self.id,'name':self.name,'age':self.age}
# 		return info
# xiaoming = Student('01','xiaojuan',20)
# print(xiaoming.getinfo())

# class Student():
# 	def __init__(self,id,name,age):
# 		self.id = id
# 		self.name = name
# 		self.age = age
# 		self.sex = '男'
# 	def getinfo(self):
# 		info = {'id':self.id,'name':self.name,'age':self.age,'sex':self.sex}
# 		return info
# xiaoming = Student('01','xiaojuan',20)
# print(xiaoming.getinfo())
# xiaoming.age = 23
# print(xiaoming.getinfo())

# class Person():
# 	def __init__(self,name,age):
# 		self.name = name
# 		self.age = age
# 	def getinfo(self):
# 		print(str(self.name) + ' ' + str(self.age))
# class Student(Person):
# 	def __init__(self,name,age,id):
# 		super().__init__(name,age)
# 		self.id = id
# 	def getinfo(self):
# 		print(str(self.name) + ' ' + str(self.age) + ' ' + str(self.id))

# xiao = Student('xiaojuan',20,'01')
# xiao.getinfo()

class Course():
	def __init__(self,teacher = 'zhang'):
		self.teacher = teacher
	def print_courseT(self):
		print(str(self.teacher))
class Person():
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def getinfo(self):
		print(str(self.name) + ' ' + str(self.age))
class Student(Person):
	def __init__(self,name,age,id):
		super().__init__(name,age)
		self.id = id
		self.course = Course()
	def getinfo(self):
		print(str(self.name) + ' ' + str(self.age) + ' ' + str(self.id))

xiao = Student('xiaojuan',20,'01')
xiao.getinfo()
xiao.course.print_courseT()