# -*- coding: utf-8 -*-
import csv
import copy 

with open('characters_cleaned.csv', 'rb') as f:
    reader = csv.reader(f)
    chars_0 = map(list, reader)
chars = copy.deepcopy(chars_0)

edges = {}
f = open("edgelist_weighted.csv", "w")
f.write("Source,Target,Type,Weight\n")

def alphabetize(x,y):
	if x<=y:
		return (x,y)
	else:
		return (y,x)

for i in range(len(chars)-1):
	first = chars[i][0]
	second = chars[i+1][0]
	mult1 = first.split("/")
	mult2 = second.split("/")
	for m1 in mult1:
		for m2 in mult2:
			tup = alphabetize(m1,m2)
			if tup not in edges:
				edges[tup] = 1
			else:
				edges[tup] +=1

#print edges
for e in edges.keys():
	weight = edges[e]
	f.write(str(e[0]) + "," + str(e[1]) + ",Undirected," + str(weight)+ "\n")

f.close()











