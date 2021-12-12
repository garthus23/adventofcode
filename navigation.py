import sys

waypoint = [10, 1]
boat = [0, 0]

for l in sys.stdin:
	letter, num = l[0], l[1:]
	num = int(num)
	print(letter, num)
	# F
	if letter == 'F':
		xb, yb = boat
		xw, yw = waypoint
		boat = (xb + num * xw, yb + num * yw)
	if letter == 'N':
		waypoint[1] += num
	if letter == 'S':
		waypoint[1] -= num
	if letter == 'E':
		waypoint[0] += num
	if letter == 'W':
		waypoint[0] -= num
	num = num // 90
	if letter == 'R':
		for _ in range(num):
			xw, yw = waypoint
			waypoint = [yw, -xw]
	if letter == 'L':
		for _ in range(num):
			xw, yw = waypoint
			waypoint = [-yw, xw]

print(sum(map(abs, boat)))
	
		
	# R
	# L
	# N
	# S
	# W
	# E

