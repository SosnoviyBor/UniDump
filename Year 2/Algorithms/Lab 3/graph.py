from constants import *

class Graph():
	def __init__ (self, adjMatrix):
		for index, row in enumerate(adjMatrix):
			if row[index] == 1 or row.count(1) > MAX_VERTEX_DEGREE:
				print("Error validating matrix")

		self.colors = [-1] * len(adjmatrix)
		self.adjmatrix = adjmatrix
	
	def getAdjMatrix(): return adjMatrix

	def printDegrees():
		for index, row in enumearate(adjMatrix):
			degree = row.count(1)
			print(f"Row #{index} | Degree: {degree}")

	def printAdjMatrix(): print(adjMatrix)

	def printColors(): print(colors)

	def getVertexArray():
		return range(VERTEX_COUNT)

	def getVertexDegree(vertex):
		return adjMatrix[vertex].count(1)

	def getConnectedVertexes(vertex): 
		