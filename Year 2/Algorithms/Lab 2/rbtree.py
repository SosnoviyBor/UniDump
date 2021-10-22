import sys
import random
from node import Node


class RedBlackTree():
	def __init__(self):
		self.TNULL = Node(0)
		self.TNULL.color = 0
		self.TNULL.left = None
		self.TNULL.right = None
		self.root = self.TNULL
	"""
	--------------------------------------------------------------------------------------------------------
	########################################################################################################
	--------------------------------------------------------------------------------------------------------
	"""
	def rb_transplant(self, u, v):
		if u.parent == None:
			self.root = v
		elif u == u.parent.left:
			u.parent.left = v
		else:
			u.parent.right = v
		v.parent = u.parent

	def minimum(self, node):
		while node.left != self.TNULL:
			node = node.left
		return node

	def maximum(self, node):
		while node.right != self.TNULL:
			node = node.right
		return node

	# rotate left at node x | counter clockwise
	def left_rotate(self, x):
		y = x.right
		x.right = y.left
		if y.left != self.TNULL:
			y.left.parent = x

		y.parent = x.parent
		if x.parent == None:
			self.root = y
		elif x == x.parent.left:
			x.parent.left = y
		else:
			x.parent.right = y
		y.left = x
		x.parent = y

	# rotate right at node x | clockwise
	def right_rotate(self, x):
		y = x.left
		x.left = y.right
		if y.right != self.TNULL:
			y.right.parent = x

		y.parent = x.parent
		if x.parent == None:
			self.root = y
		elif x == x.parent.right:
			x.parent.right = y
		else:
			x.parent.left = y
		y.right = x
		x.parent = y
	"""
	--------------------------------------------------------------------------------------------------------
	########################################################################################################
	--------------------------------------------------------------------------------------------------------
	"""
	# search the tree for the key k
	# and return the corresponding node
	def get_node(self, k):
		return self.get_node_helper(self.root, k)

	def get_node_helper(self, node, key, i=0):
		i += 1
		if key == node.data:
			print("Iterations: "+str(i))
			return node
		elif node == self.TNULL:
			return False

		if key < node.data:
			return self.get_node_helper(node.left, key, i)
		else:
			return self.get_node_helper(node.right, key, i)
	"""
	--------------------------------------------------------------------------------------------------------
	########################################################################################################
	--------------------------------------------------------------------------------------------------------
	"""
	# insert the key to the tree in its appropriate position
	# and fix the tree
	def insert(self, key):
		node = Node(key)
		node.parent = None
		node.data = key
		node.left = self.TNULL
		node.right = self.TNULL
		node.color = 1 # new node must be red

		y = None
		x = self.root

		while x != self.TNULL:
			y = x
			if node.data < x.data:
				x = x.left
			else:
				x = x.right

		# y is parent of x
		node.parent = y
		if y == None:
			self.root = node
		elif node.data < y.data:
			y.left = node
		else:
			y.right = node

		# if new node is a root node, simply return
		if node.parent == None:
			node.color = 0
			return
		# if the grandparent is None, simply return
		if node.parent.parent == None:
			return

		# Fix the tree
		self.fix_insert(node)

	# fix the red-black tree
	def fix_insert(self, k):
		while k.parent.color == 1:
			if k.parent == k.parent.parent.right:
				u = k.parent.parent.left # uncle
				if u.color == 1:
					u.color = 0
					k.parent.color = 0
					k.parent.parent.color = 1
					k = k.parent.parent
				else:
					if k == k.parent.left:
						k = k.parent
						self.right_rotate(k)
					k.parent.color = 0
					k.parent.parent.color = 1
					self.left_rotate(k.parent.parent)
			else:
				u = k.parent.parent.right # uncle
				if u.color == 1:
					u.color = 0
					k.parent.color = 0
					k.parent.parent.color = 1
					k = k.parent.parent
				else:
					if k == k.parent.right:
						k = k.parent
						self.left_rotate(k)
					k.parent.color = 0
					k.parent.parent.color = 1
					self.right_rotate(k.parent.parent)
			if k == self.root:
				break
		self.root.color = 0
	"""
	--------------------------------------------------------------------------------------------------------
	########################################################################################################
	--------------------------------------------------------------------------------------------------------
	"""
	# delete the node from the tree
	def delete_node(self, key):
		node = self.root
		z = self.TNULL
		
		while node != self.TNULL:
			if node.data == key:
				z = node

			if node.data <= key:
				node = node.right
			else:
				node = node.left

		if z == self.TNULL:
			print("Couldn't find key in the tree")
			return

		y = z
		y_original_color = y.color
		if z.left == self.TNULL:
			x = z.right
			self.rb_transplant(z, z.right)
		elif (z.right == self.TNULL):
			x = z.left
			self.rb_transplant(z, z.left)
		else:
			y = self.minimum(z.right)
			y_original_color = y.color
			x = y.right
			if y.parent == z:
				x.parent = y
			else:
				self.rb_transplant(y, y.right)
				y.right = z.right
				y.right.parent = y

			self.rb_transplant(z, y)
			y.left = z.left
			y.left.parent = y
			y.color = z.color
		if y_original_color == 0:
			print("Node deleted successfully")
			self.fix_delete(x)

	# fix the rb tree modified by the delete operation
	def fix_delete(self, x):
		while x != self.root and x.color == 0:
			if x == x.parent.left:
				s = x.parent.right
				if s.color == 1:
					s.color = 0
					x.parent.color = 1
					self.left_rotate(x.parent)
					s = x.parent.right

				if s.left.color == 0 and s.right.color == 0:
					s.color = 1
					x = x.parent
				else:
					if s.right.color == 0:
						s.left.color = 0
						s.color = 1
						self.right_rotate(s)
						s = x.parent.right

					s.color = x.parent.color
					x.parent.color = 0
					s.right.color = 0
					self.left_rotate(x.parent)
					x = self.root
			else:
				s = x.parent.left
				if s.color == 1:
					s.color = 0
					x.parent.color = 1
					self.right_rotate(x.parent)
					s = x.parent.left

				if s.left.color == 0 and s.right.color == 0:
					s.color = 1
					x = x.parent
				else:
					if s.left.color == 0:
						s.right.color = 0
						s.color = 1
						self.left_rotate(s)
						s = x.parent.left 

					s.color = x.parent.color
					x.parent.color = 0
					s.left.color = 0
					self.right_rotate(x.parent)
					x = self.root
		x.color = 0
	"""
	--------------------------------------------------------------------------------------------------------
	########################################################################################################
	--------------------------------------------------------------------------------------------------------
	"""
	# print the tree structure on the screen
	def print_tree(self):
		self.print_helper(self.root, "", True)

	def print_helper(self, node, indent, last):
		if node != self.TNULL:
			sys.stdout.write(indent)
			if last:
				sys.stdout.write("R----")
				indent += "     "
			else:
				sys.stdout.write("L----")
				indent += "|    "

			s_color = "RED" if node.color == 1 else "BLACK"
			print(str(node.data) + "(" + s_color + ")")
			self.print_helper(node.left, indent, False)
			self.print_helper(node.right, indent, True)