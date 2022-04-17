import sys

r_sym = [
	[" ", " ", " ", " "],	# dummy line
	[" ", "I", "V", "X"],
	[" ", "X", "L", "C"],
	[" ", "C", "D", "M"],
	[" ", "M", " ", " "]
]

conv_rules = [
	[0],			# dummy line
	[1],			# 1
	[1, 1],			# 2
	[1, 1, 1],		# 3
	[1, 2],			# 4
	[2],			# 5
	[2, 1],			# 6
	[2, 1, 1],		# 7
	[2, 1, 1, 1],	# 8
	[1, 3],			# 9
	[3] 			# 10
]

# initial settings
def to_roman (a_in):
	result = ""
	level = 0

	while a_in>0:
		# cut lowest digit
		a_in_tmp=int(a_in/10)
		digit = a_in-a_in_tmp*10

		# position of digit
		level = level+1

		# convert digit
		symbol = ""
		if digit!=0:
			for i in conv_rules[digit]:
				symbol = symbol+r_sym[level][i]
	
		# add converted digit to result
		result = symbol+result
		a_in = a_in_tmp

	print(result)
	return