#!/usr/bin/python3

data = []
with open('input', 'r') as f:
	for line in f:
		data.append(line[:-1])

nums = data[0]
data = data[1:]

def read_line(d):
	str_line = d.pop(0)
	line = []
	for elt in str_line.split():
		line.append(int(elt))
	return line
	

def read_grille(d):
	d.pop(0)
	grille = []
	for i in range(5):
		line = read_line(d)
		grille.append(line)
	return grille
	

players = []
while data:
	grille = read_grille(data)
	players.append(grille)

print(len(players))
print(players[0])


# on peut commencer
