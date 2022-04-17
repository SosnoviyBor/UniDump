import random
import itertools
import numpy as np
from networkx import Graph

import utils

class GeneticAlgorithm():
	def __init__(self,graph,generations,population,mutChance,draw=False):
		self.graph = graph
		self.generations = generations
		self.populationSize = population
		self.mutChance = mutChance
		self.draw = draw

		self.vert_n = len(graph.nodes)
		self.population = []
		self.population2= []
		self.best = (-1,-float("inf"),[],[])	# generation, value(aim), nodes in clique, genotype

		self.start()
		
	def start(self):
		self.population = self.random_population_init()
		eval_res = self.evaluate(self.population,0)		
		for t in range(self.generations):
			self.population2 = self.select(self.population,eval_res)
			self.population2 = self.mutate(self.population2)
			eval_res = self.evaluate(self.population2,t+1)
			self.population = self.population2
		
		print(f"------------------------ ITERATION #{self.best[0]} ---------------------------")
		print(f"Clique size = {len(self.best[2])}\nNodes in clique -> {sorted(self.best[2])}")
		if self.draw:
			utils.draw(self.graph, f"Best clique found in {self.generations} iterations", self.best[2])

	def random_population_init(self):
		population = []
		for i in range(self.populationSize):
			population.append(list(np.random.randint(2, size=self.vert_n)))
		return population

	def select(self,population, evaluation_results):
		pop2 = []
		for i in range(self.populationSize):
			indexes = []
			results = []
			for j in range(2):
				ind = random.randint(0,self.populationSize-1)
				indexes.append(ind)
				results.append(evaluation_results[ind])
			pop2.append(population[indexes[results.index(max(results))]])
		return pop2

	def mutate(self,population):
		pop2 = []
		for g in population:
			if (random.random()<=self.mutChance):
				mod_g = g
				pos = random.randint(0,len(mod_g)-1)
				if (mod_g[pos]==1):
					mod_g[pos]=0
				else:
					mod_g[pos]=1
				pop2.append(mod_g)
			else:
				pop2.append(g)
		return pop2

	def evaluate(self,population,iter):
		res = []
		for genotype in population:
			extracted_clique = list(self.clique_extraction(genotype).nodes)
			res.append(len(extracted_clique))
			if len(extracted_clique)>self.best[1]:
				self.best = [iter,len(extracted_clique),extracted_clique,genotype]
		return res;

	def clique_extraction(self,genotype):
		g = self.genotype_to_graph(genotype)
		while (not self.is_clique(g)):
			smallest_degree_nodes = self.find_smallest_degree_nodes(g)
			g.remove_node(smallest_degree_nodes[(random.randint(0, len(smallest_degree_nodes)-1))][0]);
		return g

	def genotype_to_graph(self,genotype):
		g = Graph()
		nodes = self.genotype_to_nodes(genotype)
		g.add_nodes_from(nodes)
		for e in list(itertools.combinations(nodes,2)):
			if self.graph.has_edge(e[0],e[1]):
				g.add_edge(e[0],e[1])
		return g

	def genotype_to_nodes(self, genotype):
		nodes = []
		for i in range(len(genotype)):
			if genotype[i] == 1:
				nodes.append(i)
		return nodes

	def is_clique(self,g):
		degree = len(g.nodes)-1
		for d in g.degree():
			if d[1]<degree:
				return False
		return True
		
	def find_smallest_degree_nodes(self,g):
		s = sorted(list(g.degree()), key=lambda tup: tup[1])
		if len(s)==0:
			return None

		small_degree_nodes = []
		small_degree_nodes.append(s[0])
		small= s[0][1]
		third_small_flag = False
		for i in s[1:]:
			if i[1]==small:
				small_degree_nodes.append(i)
			elif third_small_flag:
				return small_degree_nodes
			else:
				small_degree_nodes.append(i)
				small =i[1]
				third_small_flag = True
		return small_degree_nodes