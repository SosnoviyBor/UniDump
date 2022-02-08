class Node():
	def __init__(self, data):
		self.data = data	# holds the key
		self.parent = None	# pointer to the parent
		self.left = None	# pointer to left child
		self.right = None	# pointer to right child
		self.color = 1		# 0 = Black, 1 = Red