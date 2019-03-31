from GameState import GameState
import sys

sys.setrecursionlimit(99999)

cache = {}

# minimizes for player -1, maximizes for player 1
def minimax(gamestate, player_idx):
	if gamestate in cache:
		return cache[gamestate]

	winner = gamestate.check_win()
	if winner != 0:
		cache[gamestate] = winner
		return winner

	best = None
	for column in range(7):
		result = gamestate.drop(column, player_idx)
		print(gamestate)
		print("->")
		print(result)
		print(40*"-")
		if result is not None:
			result_val = minimax(result, -player_idx) * 0.9 # prioritize fast wins
			if best is None or best < player_idx * result_val:
				best = player_idx * result_val
	if best is None: best = 0
	
	cache[gamestate] = best
	return best

print("testing minimax")

print( minimax(GameState(), -1) )
