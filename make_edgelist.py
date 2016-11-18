# -*- coding: utf-8 -*-
import csv
import copy 

with open('characters_cleaned.csv', 'rb') as f:
    reader = csv.reader(f)
    chars_0 = map(list, reader)
chars = copy.deepcopy(chars_0)

f = open("edgelist.csv", "w")
f.write("Source,Target,Type\n")

for i in range(len(chars)-1):
	first = chars[i][0]
	second = chars[i+1][0]
	mult1 = first.split("/")
	mult2 = second.split("/")
	for m1 in mult1:
		for m2 in mult2:
			f.write(str(m1) + "," + str(m2) + ",Undirected\n")

f.close()