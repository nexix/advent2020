f = open('p5in.txt', "r")

rows = []
columns = []
ids = []

def populate():
	for i in range(0, 128):
		rows.append(i)
	for i in range(0, 9):
		columns.append(i)
	return(rows,columns)

#Part 1
for line in f.readlines():
	rows, columns = populate()
	for letter in line:
		print(letter)
		if letter == 'F':
			rows = rows[:int(len(rows)/2)]
			print(rows)
		elif letter == 'B':
			rows = rows[int(len(rows)/2):]
			print(rows)
		if letter == 'L':
			columns = columns[:int(len(columns)/2)]
			print(columns)
		elif letter == 'R':
			columns = columns[int(len(columns)/2):]
			print(columns)
	seat_id = rows[0] * 8 + columns[0]
	ids.append(seat_id)
	rows = []
	columns = []
	seat_id = None

sorted_list = sorted(ids)
print("\nHIGHEST ID ::",sorted_list[-1])

#Part 2
list_start = sorted_list[0]
for i in range(0, len(sorted_list)):
	if list_start == sorted_list[i]:
		pass
		list_start += 1
	else:
		print("MISSING ELEMENT ::",list_start)
		list_start += 2