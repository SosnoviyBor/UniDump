import copy
class Board:

	def __init__(self, height, width):
		self.w = width
		self.h = height
		self.vals = []
		for i in range(height):
			self.vals.append(["·"]*width)
		self.turn = 1 # 0=H="-"; 1=V="|"

	def copy(self):
		return copy.deepcopy(self)

	def show(self):
		print("\n    ", end="")
		for c in range(self.w):
			print(c%10, end=" ")
		print('\n  +-', '--'*self.w, '+', sep = '')
		for r in range(len(self.vals)):
			print(r%10, ' | ', sep='', end='')
			for val in self.vals[r]:
				print(val, end=' ')
			print('|')
		print('  +-', '--'*self.w, '+\n', sep = '')


	def play(self, pos):
		# Returns true if successful
		r = pos[0]
		c = pos[1]
		try:
			if self.turn: # V
				if self.vals[r][c] == '·' and self.vals[r+1][c] == '·':
					self.vals[r][c] = '#'
					self.vals[r+1][c] = '#'
				else:
					print("Attempted play at [", r, ", ", c, "] is not a legal move for V!", sep = "")
					return False
			else: # H
				if self.vals[r][c] == '·' and self.vals[r][c+1] == '·':
					self.vals[r][c] = 'x'
					self.vals[r][c+1] = 'x'
				else:
					print("Attempted play at [", r, ", ", c, "] is not a legal move for H!", sep = "")
					return False
		except:
			print("Attempted play at [", r, ", ", c, "] is not a legal move!", sep = "")
			return False
		self.turn = not self.turn
		return True