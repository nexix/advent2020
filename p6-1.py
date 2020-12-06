f = open('p6in.txt', "r")

decs = []
answers = []
total = 0

for line in f.readlines():
	decs.append(line.strip())

for dec in decs:
	if dec != "":
		for answer in dec:
			answers.append(answer)
	else:
		total = total + int(len(set(answers)))
		print(len(set(answers)))
		answers = []

print(total)