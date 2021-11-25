import beehive
import generator

workerBees = 8
scoutBees = 1
vertices = 300
maxConnections = 50

#adjMatrix = generator.generate(vertices, maxConnections)

adjMatrix = [
	[0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
	[1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
	[0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
	[0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 
	[1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0], 
	[0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
	[0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], 
	[0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], 
	[0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], 
	[0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0], 
	[0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0], 
	[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1], 
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0]
]

beehive = beehive.beehive(adjMatrix, workerBees, scoutBees)
coloredVertices = beehive.paint()

with open("result.txt", "w") as file:
	for i in range(len(coloredVertices)):
		file.write(f"Vertice {i} -> color #{coloredVertices[i]}\n")
	file.write(f"\nTotal colores used: {max(coloredVertices)}")

print(f"Total colores used: {max(coloredVertices)}")
print("Task completed! Check the result.txt file")