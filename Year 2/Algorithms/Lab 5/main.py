from board import *
from domineering_ai import *

def get_players():
	players = [("Human", human_play), ("AI Easy", random_play), ("AI Medium", ab_prune_ld), ("AI Hard", ab_prune)]
	print("\nPlayers:")
	for i in range(len(players)):
		print(i, players[i][0])
		
	V = players[int(input("\nEnter index of V-player: "))][1]
	H = players[int(input("Enter index of H-player: "))][1]
	return V, H


h = int(input("Enter board height: "))
w = int(input("Enter board width: "))
V, H = get_players()

board = Board(h,w)
board.show()
while True:
	# V turn
	if not possible_plays(board, 1): # V has no plays: game over
		print("H wins!")
		break
	while not board.play(V(board)): # Repeat until legal move
		pass
	board.show()
	# H turn
	if not possible_plays(board, 0): # H has no plays: game over
		print("V wins!")
		break
	while not board.play(H(board)): # Repeat until legal move
		pass
	board.show()