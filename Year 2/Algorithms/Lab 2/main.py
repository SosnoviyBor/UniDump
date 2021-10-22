import rbtree
import random
import pickle
import timeit

try:
	tree = pickle.load(open("tree_save", 'rb'))
except:
	tree = rbtree.RedBlackTree()

	for i in range(1, 10001):
		tree.insert(i)

	with open('tree_save', 'wb') as tree_file:
		pickle.dump(tree, tree_file)

tree.print_tree()

for i in range(1,11):
	randint = random.randint(1,10000)
	print("#################\nKey: "+str(randint))
	tree.get_node(randint)

tree.delete_node(randint)