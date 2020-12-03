f = open('p3in.txt', "r")

over_list = [ 	[1,1],
				[3,1],
				[5,1],
				[7,1],
				[1,2] ]
tree = 0
result = 1
mult = []

for over_set in over_list:
	lines = f.readlines()[over_set[1]::over_set[1]]
	over_start = over_set[0]
	over = over_set[0]
	for line in lines:
		line = line.strip()
		if over >= len(line):
			over = over - len(line)
		if line[over] == '#':
			tree = tree + 1
		over = over + over_start
	mult.append(tree)
	f.seek(0,0)
	tree = 0
print(mult)
for m in mult:
	result = m * result
print(result)