import random
import networkx as nx
import matplotlib.pyplot as plt
import networkx.algorithms.clique as cl

def generateGraph(n,p):
	g = nx.Graph()
	for i in range(n):
		g.add_node(i)
	for i in range(n):
		for j in range(n):
			g.add_edge(i,j)
	e = random.sample(g.edges, int(len(g.edges)*p))
	g.clear_edges();
	g.add_edges_from(e)
	return g

def draw(g,title="",nodes_with_different_col = None):
	plt.figure(figsize=(10,5))
	ax = plt.gca()
	ax.set_title(title)
	if nodes_with_different_col == None:
		nx.draw(g, node_size=900, with_labels=True,ax=ax)
	else:
		colors = []
		for node in g.nodes:
			if node in nodes_with_different_col:
				colors.append('yellow')
			else:
				colors.append('pink')
		nx.draw(g, node_size=900, node_color=colors,with_labels=True,ax=ax)
	plt.show()

def report_real_max_clique(g):
	print("------------------------ BEST CLIQUE BY NETWORX ---------------------------")
	clique = max_clique(g)
	print(f"Clique size = {len(list(clique.nodes))}")
	print(f"Nodes in clique -> {sorted(list(clique.nodes))}")

def max_clique(g):
	cliques = list(cl.enumerate_all_cliques(g))
	max_clique_graph = g.subgraph(nodes=cliques[-1])
	return max_clique_graph