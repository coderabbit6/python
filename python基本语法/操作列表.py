# a = [1,2,3,4,5,6,7,8]
# for i in a:
# 	print("i am {0}".format(i))

# for i in range(5):
# 	print(i)

# b = list(range(7))
# print(b)

squares = [value**2 for value in range(1,11)]
print(squares)

a = [1,2,3,4,5,6,7]
# print(a[1:4])

b = a[:]
# print(a)
# print(b)
a.append(25)
b.append(36)
print(a)
print(b)