import timeit
from collections import deque
from state import State
from heapq import heappush, heappop, heapify
import itertools
import random

goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
goal_node = State
initial_state = list()
board_len = 9
board_side = 3

nodes_expanded = 0
max_search_depth = 0
max_frontier_size = 0

moves = list()
costs = set()


def BFS(puzzle, max_search_depth):
	print("\n########## BFS algo ##########")
	start_state = puzzle2state(puzzle)
	iterations = 0

	start = timeit.default_timer()

	global nodes_expanded
	global max_frontier_size
	global goal_node

	nodes_expanded = 0
	explored = set()
	queue = deque([State(start_state, None, None, 0, 0, 0)])

	while queue:

		node = queue.popleft()
		explored.add(node.map)

		if node.state == goal_state:
			goal_node = node

			stop = timeit.default_timer()
			end(iterations, stop-start)
			return queue

		neighbors = expand(node)

		for neighbor in neighbors:
			iterations += 1
			if neighbor.map not in explored:
				queue.append(neighbor)
				explored.add(neighbor.map)

				if neighbor.depth > max_search_depth:
					raise Exception("Exceeded maximum search depth")
	
	raise Exception("Impossible input")


def Astar(puzzle, max_search_depth):
	print("\n########## A* algo ##########")
	start_state = puzzle2state(puzzle)
	iterations = 0
	
	start = timeit.default_timer()

	global nodes_expanded
	global max_frontier_size
	global goal_node

	explored = set()
	heap = list()
	heap_entry = {}
	counter = itertools.count()
	nodes_expanded = 0

	key = h(start_state)
	root = State(start_state, None, None, 0, 0, key)
	entry = (key, 0, root)
	heappush(heap, entry)
	heap_entry[root.map] = entry

	while heap:
		node = heappop(heap)
		explored.add(node[2].map)

		if node[2].state == goal_state:
			goal_node = node[2]

			stop = timeit.default_timer()
			end(iterations, stop-start)
			return heap

		neighbors = expand(node[2])
		for neighbor in neighbors:
			iterations += 1
			neighbor.key = neighbor.cost + h(neighbor.state)
			entry = (neighbor.key, neighbor.move, neighbor)

			if neighbor.map not in explored:
				heappush(heap, entry)
				explored.add(neighbor.map)
				heap_entry[neighbor.map] = entry

				if neighbor.depth > max_search_depth:
					raise Exception("Exceeded maximum search depth")

			elif neighbor.map in heap_entry and neighbor.key < heap_entry[neighbor.map][2].key:
				hindex = heap.index((heap_entry[neighbor.map][2].key,
									 heap_entry[neighbor.map][2].move,
									 heap_entry[neighbor.map][2]))

				heap[int(hindex)] = entry
				heap_entry[neighbor.map] = entry
				heapify(heap)
	
	raise Exception("Impossible input")


def puzzle2state(puzzle):
	state = []

	print("Input:", end="")
	for i in range(0,3):
		print("\n", end="")
		for j in range(0,3):
			print (str(puzzle[i][j]) + " ", end="")
			state.append(puzzle[i][j])
	print("\n")
	return state

def end(iterations, time):
	print(
		"Time spent: " + format(time, '.8f') + "s" + "\n" +
		"Iterations: " + str(iterations) + "\n" +
		"Nodes expanded: " + str(nodes_expanded) + "\n" +
		"Search depth: " + str(goal_node.depth)
	)
	return


def expand(node):
	global nodes_expanded
	nodes_expanded += 1

	neighbors = list()
	neighbors.append(State(move(node.state, 1), node, 1, node.depth + 1, node.cost + 1, 0))
	neighbors.append(State(move(node.state, 2), node, 2, node.depth + 1, node.cost + 1, 0))
	neighbors.append(State(move(node.state, 3), node, 3, node.depth + 1, node.cost + 1, 0))
	neighbors.append(State(move(node.state, 4), node, 4, node.depth + 1, node.cost + 1, 0))

	return [neighbor for neighbor in neighbors if neighbor.state]


def move(state, position):
	new_state = state[:]
	index = new_state.index(0)

	if position == 1:  # Up
		if index not in range(0, board_side):
			temp = new_state[index - board_side]
			new_state[index - board_side] = new_state[index]
			new_state[index] = temp
			return new_state
		else:
			return None

	if position == 2:  # Down
		if index not in range(board_len - board_side, board_len):
			temp = new_state[index + board_side]
			new_state[index + board_side] = new_state[index]
			new_state[index] = temp
			return new_state
		else:
			return None

	if position == 3:  # Left
		if index not in range(0, board_len, board_side):
			temp = new_state[index - 1]
			new_state[index - 1] = new_state[index]
			new_state[index] = temp
			return new_state
		else:
			return None

	if position == 4:  # Right
		if index not in range(board_side - 1, board_len, board_side):
			temp = new_state[index + 1]
			new_state[index + 1] = new_state[index]
			new_state[index] = temp
			return new_state
		else:
			return None


def h(state):
	return sum(abs(b % board_side - g % board_side) + abs(b//board_side - g//board_side)
			   for b, g in ((state.index(i), goal_state.index(i)) for i in range(1, board_len)))


def shuffle (puzzle):
	state = []

	for i in range(0,3):
		for j in range(0,3):
			state.append(puzzle[i][j])
	
	random.shuffle(state)

	k = 0
	for i in range(0,3):
		for j in range(0,3):
			puzzle[i][j] = state[k]
			k += 1
	
	return puzzle