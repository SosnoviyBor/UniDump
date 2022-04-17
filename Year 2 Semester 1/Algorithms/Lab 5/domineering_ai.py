import random
import math

# # # AI's # # #
# All return play [r,c]
def human_play(board):
	r = input("It is your turn to make a play!\nRow: ")
	c = input("Column: ")
	return [int(r), int(c)]

def random_play(board):
	return random.choice(possible_plays(board, board.turn))

def ab_prune_ld(board):
	return ab_prune(board, 1)

def ab_prune(board, max_depth=5):
	count = 0
	a = -math.inf
	b = math.inf
	max_score = -math.inf
	max_play = []
	hs = h_symm(board)
	vs = v_symm(board)
	rs = r_symm(board)

	sorted_plays = sort_plays(possible_plays(board, board.turn), board, moves_score)
	for elem in sorted_plays:
		pp = elem[1]
		new_board = elem[2]
		if (hs or rs) and (pp[1] > (board.w + board.turn - 2) // 2):
			# Plays on right side of board can be cut off
			continue
		if vs and (pp[0] > (board.h - board.turn - 1) // 2):
			# Plays on bottom of board can be cut off
			continue
		count += 1
		new_score, add_count = minsym(new_board, board.turn, max_depth, a, b, moves_score)
		count += add_count
		if new_score > max_score:
			max_score = new_score
			max_play = [pp]
		elif new_score == max_score:
			max_play.append(pp)
		a = max(a, new_score)
	return random.choice(max_play)



# # # HELPER FUNCTIONS # # #
def moves_score(board, player):
	# spaces only I can play - spaces only opponent can play
	return len(possible_plays(board, player)) - len(possible_plays(board, not player))

def possible_plays(board, player):
	# given board and player 0 (H) or 1 (V)
	# returns a list of coordinates [r,c] of row-column pairs indicating the location of a possible play for player
	plays = []
	if player == 0: # H
		for r in range(board.h): # All rows
			for c in range(board.w - 1): # All columns except last
				if board.vals[r][c] == '·' and board.vals[r][c+1] == '·':
					plays.append([r,c])
	else: # V
		for r in range(board.h - 1): # All rows except last
			for c in range(board.w): # All columns
				if board.vals[r][c] == '·' and board.vals[r+1][c] == '·':
					plays.append([r,c])
	return plays

def h_symm(board):
	# Returns True if board is horizontally symmetric
	for r in range(board.h):
		for c in range(board.w//2):
			if (board.vals[r][c] == '·') != (board.vals[r][board.w - c - 1] == '·'):
				return False
	return True

def v_symm(board):
	# Returns True if board is vertically symmetric
	for r in range(board.h//2):
		for c in range(board.w):
			if (board.vals[r][c] == '·') != (board.vals[board.h - r - 1][c] == '·'):
				return False
	return True

def r_symm(board):
	# Returns True if board is rotationally symmetric
	for r in range(board.h):
		for c in range(board.w//2):
			if (board.vals[r][c] == '·') != (board.vals[board.h - r - 1][board.w - c - 1] == '·'):
				return False
	return True

def minsym(board, player, max_depth, a, b, eval_fn):
	# Even layers of alphabeta with symmetric pruning (opponent's turn)
	# Returns worst SCORE opponent can force
	count = 0
	if max_depth == 0: # At max_depth -> return my evaluated score on current board
		return eval_fn(board, player), count
	else:
		min_score = math.inf
		hs = h_symm(board)
		vs = v_symm(board)
		rs = r_symm(board)
		for pp in possible_plays(board, board.turn):
			if (hs or rs) and (pp[1] > (board.w + board.turn - 2) // 2):
				# Plays on right side of board can be cut off
				continue
			if vs and (pp[0] > (board.h - board.turn - 1) // 2):
				# Plays on bottom of board can be cut off
				continue
			count += 1
			new_board = board.copy()
			new_board.play(pp)
			new_score, add_count = maxsym(new_board, player, max_depth-1, a, b, eval_fn)
			count += add_count
			min_score = min(new_score, min_score)
			b = min(b, min_score)
			if a > b:
				break # a cut-off
		return min_score, count

def maxsym(board, player, max_depth, a, b, eval_fn):
	# Odd layers of alphabeta with symmetric pruning (my turn)
	# Returns best SCORE I can force
	count = 0
	if max_depth == 0: # At max_depth -> return my evaluated score on current board
		return eval_fn(board, player), count
	else:
		max_score = -math.inf
		hs = h_symm(board)
		vs = v_symm(board)
		rs = r_symm(board)
		for pp in possible_plays(board, board.turn):
			if (hs or rs) and (pp[1] > (board.w + board.turn - 2) // 2):
				# Plays on right side of board can be cut off
				continue
			if vs and (pp[0] > (board.h - board.turn - 1) // 2):
				# Plays on bottom of board can be cut off
				continue
			count += 1
			new_board = board.copy()
			new_board.play(pp)
			new_score, add_count = minsym(new_board, player, max_depth-1, a, b, eval_fn)
			count += add_count            
			max_score = max(new_score, max_score)
			a = max(a, max_score)
			if a > b:
				break # b cut-off
		return max_score, count

def sort_plays(plays, board, eval_fn):
	# Sorts plays by the value of the gamestate
	foo = []
	for p in plays:
		new_board = board.copy()
		new_board.play(p)
		eval_fn(new_board, board.turn)
		foo.append((eval_fn(new_board, board.turn), p, new_board))
	return sorted(foo, reverse = True)