import os

left = 0
right = 0
up = 0
down = 0

north = 'north'
east = 'east'
south = 'south'
west = 'west'
last = north

with open('input.txt', 'r+') as x:
	y = x.read()
	y = y.split(', ')
	for z in y:
		print(z, sep='')
		if z[0] == 'R' and last == 'north':
			right+=int(z[1:])
			last = 'east'
		elif z[0] == 'R' and last == 'east':
			down +=int(z[1:])
			last = 'south'
		elif z[0] == 'R' and last == 'south':
			left+=int(z[1:])
			last = 'west'
		elif z[0] == 'R' and last == 'west':
			up+=int(z[1:])
			last = 'north'
		elif z[0] == 'L' and last == 'east':
			up +=int(z[1:])
			last = 'north'
		elif z[0] == 'L' and last == 'south':
			right+=int(z[1:])
			last = 'east'
		elif z[0] == 'L' and last == 'north':
			left+=int(z[1:])
			last = 'west'
		elif z[0] == 'L' and last == 'west':
			down+=int(z[1:])
			last = 'south'
		else:
			print('?')
print("LRUD: [{0},{1},{2},{3}]\nNESW: [{4},{5},{6},{7}]".format(left, right, up, down, north, east, south, west))
x1 = right - left
y1 = up - down
res = x1 + y1
print(res)
