import sys

p1_input = []

f = open('p1in.txt', "r")

for line in f:
	p1_input.append(line.strip())

for i in (range(len(p1_input))):
	for j in (range(len(p1_input))):
		if int(p1_input[i]) + int(p1_input[j]) < 2020:
			for k in (range(len(p1_input))):
				if k != i or k != j:
					if int(p1_input[i]) + int(p1_input[j]) + int(p1_input[k]) == 2020:
						print(p1_input[i],p1_input[j],p1_input[k])
						print(int(p1_input[i]) * int(p1_input[j]) * int(p1_input[k]))
						sys.exit(0)	