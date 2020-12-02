import os

p1_input = []

f = open('p1in.txt', "r")

for line in f:
	p1_input.append(line.strip())

for i in (range(len(p1_input))):
	for j in (range(len(p1_input))):
		if int(p1_input[i]) + int(p1_input[j]) == 2020:
			print(p1_input[i],p1_input[j])
			print(int(p1_input[i]) * int(p1_input[j]))
