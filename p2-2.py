f = open('p2in.txt', "r")

valid = 0
for line in f:
	(count, letter, password) = line.split(' ')
	(cmin,cmax) = count.split('-')
	letter = letter.strip(':')
	print(cmin,cmax,letter,password, end='')
	cmin_found = False
	cmax_found = False
	if bool(letter == password[int(cmin)-1]) ^ bool(letter == password[int(cmax)-1]):
		print("VALID\n")
		valid = valid + 1
print("VALID ::", valid)

#xor truth table:
#A B R
#F F F
#F T T
#T F T
#T T F