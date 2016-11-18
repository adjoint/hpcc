# -*- coding: utf-8 -*-

print 5

with open("hpcc.txt") as f:
    content = f.readlines()

char = ":"

out = open("characters.csv", "w")

for line in content:
	array = line.split(char)
	if len(array) > 1:
		print array[0]
		out.write(str(array[0]) + "\n")

out.close()