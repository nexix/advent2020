f = open('p3in.txt', "r")

valid = 0
for line in f:
	(count, letter, password) = line.split(' ')
	(cmin,cmax) = count.split('-')
	letter = letter.strip(':')
	print(cmin,cmax,letter,password, end='')
	cmin_found = False
	cmax_found = False
	if letter == password[int(cmin)-1]:
		#print("CMIN ::",int(cmin)-1,password[int(cmin)-1])
		cmin_found = True
	if letter == password[int(cmax)-1]:
		#print("CMAX ::",int(cmax)-1,password[int(cmax)-1])
		cmax_found = True
	if (cmin_found == True and cmax_found == True):
		pass
	elif (cmin_found == True or cmax_found == True):
		print("VALID\n")
		valid = valid + 1
print("VALID ::", valid)