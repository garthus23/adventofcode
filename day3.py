#!/usr/bin/python3

"""
PART 1
"""

"""
arr = [0,0,0,0,0,0,0,0,0,0,0,0]
dec = 1
gamma = 0
epsilon = 0


with open("input", "r") as file:
	for line in file:
		line=line.strip()[::-1]
		for i in range(len(line)):
			arr[i] = arr[i] + int(line[i])
	for i in range(len(arr)):
			if arr[i] > 500:
				arr[i] = 1
				gamma = gamma + dec
			else:
				arr[i] = 0
				epsilon = epsilon + dec
			dec = dec * 2
print(gamma*epsilon)

"""
"""
PART 2
"""


data=[]
with open("input", "r") as file:
	for line in file:
		data.append(line[:-1])

def getlist(data, n):
	list1 = []
	list0 = []

	for i in data:
		if i[n] == '1':
			list1.append(i)
		if i[n] == '0':
			list0.append(i)
	return list0, list1
c = []
a,b = getlist(data,0)

if (len(a) > len(b)):
	c = a	
else:
	c = b
for i in range(1, len(c)):
	if len(c) == 1 :
		break
	a,b = getlist(c, i)
	if (len(a) > len(b)):
		c = a 
	else:
		c = b

d = []
a,b = getlist(data,0)

if (len(a) > len(b)):
	d = b
else:
	d = a
for i in range(1, len(d)):
	if len(d) == 1 :
		break
	a,b = getlist(d, i)
	if (len(a) > len(b)):
		d = b
	else:
		d = a


print(c)
print(d)
print(int(c[0],2)* int(d[0], 2))
