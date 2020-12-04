import json

f = open('p4in.txt', "r")

keys_required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
keys_optional = ['cid']

passport_list = []
passport_dict = {}
passport_keys = []
valid_pass = 0
count = 0 

for line in f.readlines():
	if line.rstrip() != "":
		passport_dict.update(dict(x.split(":") for x in line.split(" ")))
	else:
		passport_list.append(passport_dict)
		passport_dict = {}

for passport in passport_list:
	for key,value in passport.items():
		passport_keys.append(key)
	difference = [ele for ele in keys_required if not ele in passport_keys]
	if difference:
		pass
	else:
		valid_pass += 1
	passport_keys = []

print()
print("TOTAL PASSPORTS ::", len(passport_list))
print("VALID PASSPORTS ::",valid_pass)
#print(json.dumps(passport_list, indent=2))