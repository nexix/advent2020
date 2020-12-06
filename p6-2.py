f = open('p6in.txt', "r")

decs = []
answers = []
common = []
total = 0

for line in f.readlines():
	decs.append(line.strip())

for dec in decs:
	if dec != "":
		for answer in dec:
			answers.append(answer)
		common.append(set(answers))
		answers = []
	else:
		print(common, end='')
		u = set.intersection(*common)
		total = total + int(len(set(u)))
		print(len(set(u)))
		print()
		common = []

print(total)