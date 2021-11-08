import random
import graph
from constants import *

class GraphGenerator():
	def gen():
		adjMatrix = [ [0] * VERTEX_COUNT ] * VERTEX_COUNT
		for vertex in range(VERTEX_COUNT):
			vertexConnections = adjMatrix[vertex]
			currentVertexDegree = vertexConnections.count(1)
			finalVertexDegree = min(
				random.randint(MIN_VERTEX_DEGREE, MAX_VERTEX_DEGREE) - currentVertexDegree,
				VERTEX_COUNT - vertex - 1
			)
			
			for newConnection in range(finalVertexDegree+1):
				isConnectedAlready = True
				tryCount = 0
				
				while (isConnectedAlready and tryCount < VERTEX_COUNT):
					newConnectionVertex = random.choise(range(vertex + 1, VERTEX_COUNT))
					tryCount+=1
					newConnectionVertexDegree = adjMatrix[newConnectionVertex].count(1)
					
					if (vertexConnections[newConnectionVertex] == 0 and
							newConnectionVertexDegree < MAX_VERTEX_DEGREE):
						isConnectedAlready = False
						adjMatrix[vertex][newConnectionVertex] = 1
						adjMatrix[newConnectionVertex][vertex] = 1
		
		return graph.Graph(adjMatrix)