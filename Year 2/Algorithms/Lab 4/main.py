import pickle

import geneticMaxClique
import utils

if __name__ == '__main__':
	
	CREATE_NEW_GRAPH = False
	
	try:
		if CREATE_NEW_GRAPH:
			raise
		with open("graph", "rw") as file:
			g = pickle.load(file)
	except:
		n = 300		# Количество вершин. Длинна генома особи
		p = 0.1		# Процент сохраненных ребер
		g = utils.generateGraph(n,p)

		with open("graph", "bw") as file:
			pickle.dump(g, file)

	gens = 10		# Количество итераций
	population = 80	# Размер популяции. Чем больше значение - тем больше вариантов будет перебрано
	mutChance = 1	# Шанс мутировать. Чем больше шанс - тем больше вариантов будет перебрано

	#utils.report_real_max_clique(g)
	geneticMaxClique.GeneticAlgorithm(g,gens,population,mutChance,True)