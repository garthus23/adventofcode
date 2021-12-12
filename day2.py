#!/usr/bin/python3

horizontal=0
aim=0
depth=0

with open("input", "r") as file:
	for line in file:
#		print(line, end='')
#		line = line.replace("\n", "")
		line=line.strip()
		print([line])
		x,y=line.split()
		y=int(y)
		if x == "forward":
			horizontal += y
			depth += aim * y
		if x == "down":
			aim += y
		if x == "up":
			aim -= y
	
print(depth*horizontal)
