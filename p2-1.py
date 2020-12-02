f = open('p2in.txt', "r")

p3_input = {}

valid = 0
for line in f:
	(count, letter, password) = line.split(' ')
	(cmin,cmax) = count.split('-')
	letter = letter.strip(':')
	print(cmin,cmax,letter,password, end='')
	count = 0
	for i in range(len(password)):
		if letter in password[i]:
			count = count + 1
	print("COUNT ::", count)
	if count >= int(cmin) and count <= int(cmax):
		print("VALID\n")
		valid = valid + 1
print("\nVALID ::", valid)
