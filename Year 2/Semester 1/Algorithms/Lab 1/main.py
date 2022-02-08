from traverser import Astar, BFS, shuffle

# https://deniz.co/8-puzzle-solver/

default = [
	[0,1,2],
	[3,4,5],
	[6,7,8]
]
# comment to use perfect puzzle
default = shuffle(default)

preset1 = [
	[1,2,3],
	[4,0,6],
	[7,5,8]
]
preset2 = [
	[4,6,1],
	[7,0,8],
	[3,2,5]
]
preset3 = [
	[0,3,2],
	[5,7,4],
	[8,6,1]
]

# i think, you need only 1 algo to work at the same time
BFS(default, 40)
Astar(default, 30)