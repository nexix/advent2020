import json
import re

f = open('p7in.txt', "r")

bag_dict = {}
count = 0
gold_list = []
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
for line in f.readlines():
	primary_bag, secondary_bags  = line.split('bags contain')
	primary_bag = primary_bag.strip()
	bags = secondary_bags.split(',')
	bag_dict[primary_bag] = {}
	for bag in bags:
		if 'no other bags' in bag:
			bag_dict[primary_bag] = {}
		else:
			bag_result = re.search(r"(\d+)(.*)bag", bag.strip())
			#print(bag_result.group(1), bag_result.group(2))
			bag_dict[primary_bag][bag_result.group(2).strip()] = int(bag_result.group(1))
	#print(json.dumps(bag_dict, indent=2))
	#input()

def get_contained_colors(color):
	#print(color)
	for subcolor in bag_dict[color]:
		#print(subcolor)
		#input()
		yield from get_contained_colors(subcolor)
		yield subcolor

def get_number_of_bags(color):
    return sum(int(count) + get_number_of_bags(subcolor) * int(count) for subcolor,count in bag_dict[color].items())


for color in bag_dict:
	print("COLOR ::",color)
	if "shiny gold" in get_contained_colors(color):
		gold_list.append(color)
	print(gold_list)
	#input()

print(len(gold_list))
print(get_number_of_bags("shiny gold"))