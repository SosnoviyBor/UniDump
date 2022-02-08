import random

def generate(task:int, maxConnections:int):
	adjMatrix = []
	for i in range(task):
		adjMatrix.append(list(range(task)))

	length = len(adjMatrix)
	skip = 1
	for y in range(length):
		power = 0
		for x in range(skip, length):
			val = random.randint(0, 1)
			if power == maxConnections:
				val = 0
			
			adjMatrix[y][x] = val
			adjMatrix[x][y] = adjMatrix[y][x]
			
			if adjMatrix[x][y] != adjMatrix[y][x]:
				raise Exception("An error ocured while generating your matrix")
			if val == 1:
				power += 1

		skip += 1
		adjMatrix[y][y] = 0
	
	return adjMatrix