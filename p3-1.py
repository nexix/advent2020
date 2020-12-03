f = open('p3in.txt', "r")
next(f)

over = 3
tree = 0
for line in f:
	line = line.strip()
	if over >= len(line):
		over = over - len(line)
	if line[over] == '#':
		tree = tree + 1
	over = over + 3
print(tree)