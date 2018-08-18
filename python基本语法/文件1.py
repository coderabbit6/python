with open('pai.txt') as f:
	con = f.read()
	print(con)

with open('pai.txt') as f:
	for line in f:
		print(line)