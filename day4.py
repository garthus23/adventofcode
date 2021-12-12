#!/usr/bin/python3
# Bingo Game


# Define the list Pulled Numbers
def pull(arr):
	pulled = []
	pulled = getput[0].split(',')
	return pulled

# Define the rows of the grill
def rows(arr):
	row = []
	for line in arr:
		if line is not "":
			row.append(line.split())
	return row

# Define the Grill
def grills(arr):
	grill = []
	grill_t = []
	
	while len(arr) > 0:	
		for i in range(5):
			grill.append(arr.pop(0))
		grill_t.append(grill)
		grill = []
	return grill_t

# check if number is in Grill
def marknumbers(number, grill_t):
	for x in range(len(grill_t)):
		for y in range(len(grill_t[x])):
			for z in range(len(grill_t[x][y])):
				foundnum = grill_t[x][y][z]
				if int(foundnum) == number:
					grill_t[x][y][z] = int(foundnum)
	return grill_t 

# verify if we have a row or column of int (Bingo !)
def verify(grill_t):
	




getput = []
with open("input", "r") as file:
	for line in file:
		getput.append(line[:-1])
	
pulled = pull(getput)
getput.pop(0)
row = rows(getput)
grill_t = grills(row)


for number in pulled:
	grill_t = marknumbers(int(number), grill_t)
	verify(grill_t)
