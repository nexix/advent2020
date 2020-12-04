import json
import re

f = open('p4in.txt', "r")

keys_required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
keys_optional = ['cid']
eye_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

passport_list = []
passport_dict = {}
passport_keys = []
valid_pass = 0
invalid_pass = 0
pattern = re.compile(r"^(\d+)(cm|in)$")

for line in f:
	if line.rstrip() != "":
		passport_dict.update(dict(x.split(":") for x in line.split(" ")))
	else:
		passport_list.append(passport_dict)
		passport_dict = {}		

for passport in passport_list:
	print(passport)
	for key,value in passport.items():
		if key == 'byr':
			if 1920 <= int(value.strip()) <= 2002:
				pass
			else:
				print(value.strip())
				continue
		if key == 'iyr':
			if 2010 <= int(value.strip()) <= 2020:
				pass
			else:
				print(value.strip())
				continue
		if key == 'eyr':
			if 2020 <= int(value.strip()) <= 2030:
				pass
			else:
				print(value.strip())
				continue
		if key == 'hgt':
			if re.match(pattern, value.strip()):
				value, unit = pattern.findall(value.strip()).pop()
				if unit == 'cm':
					if 150 <= int(value.strip('cm,\n')) <= 193:
						pass
					else:
						print(value.strip())
						continue
				if unit == 'in':
					if 59 <= int(value.strip('in,\n')) <= 76:
						pass
					else:
						print(value.strip())
						continue
			else:
				continue
		if key == 'hcl':
			if re.search(r"^#[a-f0-9]{6}$", value.strip()):
				pass
			else:
				print(value.strip())
				continue
		if key == 'ecl':
			if value.strip() in eye_color:
				pass
			else:
				print(value.strip())
				continue
		if key == 'pid':
			if re.search(r"^[0-9]{9}$", value.strip()):
				pass
			else:
				print(value.strip())
				continue
		passport_keys.append(key)
	difference = [ele for ele in keys_required if not ele in passport_keys]
	if difference:
		invalid_pass += 1
		pass
	else:
		print("VALID ::", difference)
		valid_pass += 1
	passport_keys = []

print()
print("TOTAL PASSPORTS ::", len(passport_list))
print("VALID PASSPORTS ::",valid_pass)