import sys

f = open('p8in.txt', "r")

code_list = []
accumulator = 0
visited = []

for line in f.readlines():
	op, arg = line.split(" ")
	code_list.append([op.strip(), arg.strip()])

def bootstrap(count):
	global accumulator
	print(code_list[count])
	if code_list[count][0] == 'acc':
		if "+" in code_list[count][1]:
			accumulator += int(code_list[count][1].strip('+'))
			return 1
		else:
			accumulator -= int(code_list[count][1].strip('-'))
			return 1
	if code_list[count][0] == 'nop':
		return 1
	if code_list[count][0] == 'jmp':
		return int(code_list[count][1])

i=0
while True:
	i += bootstrap(i)
	if i in visited:
		print(accumulator)
		sys.exit(0)
	else:
		visited.append(i)

