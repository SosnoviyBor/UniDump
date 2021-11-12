from typing import *
import random

class beehive():
	def __init__(self, 
				 graph: List[List[int]], 
				 workerBeesCount: int, 
				 scoutBeesCount: int) -> None:
		
		for i in range(0,len(graph)):
			if len(graph[0]) != len(graph[i]) or graph[i][i] != 0:
				raise ValueError("Wrong graph matrix provided")
		
		self.graph = graph
		self.workerBeesCount = workerBeesCount
		self.scoutBeesCount = scoutBeesCount
		pass

	def paint(self):
		coloredVertices = self.__greedyPaint()	# Первичная, грубая, разрисовка графа
		processedVertices = set()
		availableBees = self.workerBeesCount

		while len(processedVertices) != len(self.graph):	# Находимся в цикле, пока не обойдем весь граф
			toProcess = []
			
			i = 0
			while i < self.scoutBeesCount:	# Разведчики составляют пути для рабочих (случайным способом)
				if len(processedVertices) == len(self.graph):
					break

				randomVertex = self.__getRandomVertex(processedVertices)
				toProcess.append(randomVertex)
				processedVertices.add(randomVertex)
				i+=1
			
			toProcess.sort(key=self.__getDegree, reverse=True)

			for vertex in toProcess:	# Проходимся по всем вершинам, что нам разведали разведчики пока у нас не закончатся либо пчелы, либо соседи
				neighbours = self.__getNeighbours(vertex)

				processVertices = min(availableBees, len(neighbours))
				i = 0

				for neighbour in neighbours: # Красим, пока у нас либо не кончатся работяги, либо соседи
					if processVertices == i:
						break
				
					colorCount = self.__countColors(coloredVertices)
					if self.__trySwappingColors(vertex, neighbour, coloredVertices):	# Пытаемся поменять местами две вершины в надежде, что это поможет оптимизировать закраску
						j = 1
						while j <= len(colorCount): # Красим обе вершины в максимально оптимальный цвет
							if (self.__isColorValid(j, vertex, coloredVertices)
									and colorCount[coloredVertices[vertex] - 1]) < colorCount[j - 1]:
								coloredVertices[vertex] = j
								colorCount = self.__countColors(coloredVertices)

							if (self.__isColorValid(j, neighbour, coloredVertices)
									and colorCount[coloredVertices[neighbour] - 1]) < colorCount[j - 1]:
								coloredVertices[neighbour] = j
								colorCount = self.__countColors(coloredVertices)
							
							j+=1

					i+=1

				availableBees = max(availableBees - len(neighbours), 0)
		return coloredVertices
	
	def __countColors(self, coloredVertices:List[int]):
		colorsCount = []
		for color in coloredVertices:
			while len(colorsCount) <= color - 1:
				colorsCount.append(0)
			
			colorsCount[color - 1] = colorsCount[color - 1] + 1

		return colorsCount
	
	def __trySwappingColors(self, v1:int, v2:int, coloredVertices:List[int]):
		if (self.__isColorValidNoConsider(coloredVertices[v1], v2, coloredVertices, v1)
				and self.__isColorValidNoConsider(coloredVertices[v2], v1, coloredVertices, v2)):
			tmp = coloredVertices[v1]
			coloredVertices[v1] = coloredVertices[v2]
			coloredVertices[v2] = tmp
			return True
		else:
			return False
	
	def __getDegree(self, vertex:int):
		return sum( filter( lambda v: self.graph[vertex][v] == 1, range( 0, len(self.graph) ) ) )
	
	def __greedyPaint(self):
		color = 0
		coloredVertices = [None] * len(self.graph)
		processedVertices = set()
		currentVertex = 0

		while len(processedVertices) != len(self.graph):
			color+=1
			self.__recursivePaint(color, coloredVertices, processedVertices, currentVertex)

			currentVertex+=1
			while currentVertex in processedVertices:
				currentVertex+=1

		return coloredVertices

	def __recursivePaint(self, color:int, coloredVertices:List[int],
						processedVertices:Set[int], currentVertex:int):
		if (not self.__isColorValid(color, currentVertex, coloredVertices)
				or currentVertex in processedVertices):
			return
		
		coloredVertices[currentVertex] = color
		processedVertices.add(currentVertex)

		for neighbour in self.__getNeighbours(currentVertex):
			for neighboursNeighbour in self.__getNeighbours(neighbour):
				if not neighboursNeighbour in processedVertices:
					self.__recursivePaint(color, coloredVertices, processedVertices, neighboursNeighbour)
		return
	
	def __isColorValidNoConsider(self, color:int, vertex:int, coloredVertices:List[int], notConsider:int):
		for neighbour in self.__getNeighbours(vertex):
			if notConsider == neighbour:
				continue
			
			if coloredVertices[neighbour] == color:
				return False
		return True

	def __isColorValid(self, color:int, vertex:int, coloredVertices:List[int]):
		for neighbour in self.__getNeighbours(vertex):
			if coloredVertices[neighbour] == color:
				return False
		return True

	def __getNeighbours(self, vertex:int):
		return list( filter( lambda x: self.graph[vertex][x] == 1, range(0, len(self.graph)) ) )

	def __getRandomVertex(self, processedVertices:Set[int]):
		availableVertices = list( filter( lambda vertex: not vertex in processedVertices, range(0, len(self.graph)) ) )
		return random.choice(availableVertices)