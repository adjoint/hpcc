# -*- coding: utf-8 -*-
import csv
import copy 
import operator

with open('characters_cleaned.csv', 'rb') as f:
    reader = csv.reader(f)
    chars_0 = map(list, reader)
chars = copy.deepcopy(chars_0)

f = open("edgelist.csv", "w")
unique_nodes = {}

for char in chars:
	mult = char[0].split("/")
	for c in mult:
		if c not in unique_nodes.keys():
			unique_nodes[c] = 1
		else:
			unique_nodes[c] +=1

sorted_nodes = sorted(unique_nodes.items(), key=operator.itemgetter(1), reverse=True)
print sorted_nodes