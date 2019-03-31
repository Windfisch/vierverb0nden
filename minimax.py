from GameState import GameState
import sys

sys.setrecursionlimit(99999)

cache = {}

# minimizes for player -1, maximizes for player 1
def minimax(gamestate, player_idx):
	if len(cache) % 1000 == 0: print(len(cache))
	if gamestate in cache:
		return cache[gamestate]

	winner = gamestate.check_win()
	if winner != 0:
		cache[gamestate] = winner
		return winner

	best = None
	for column in range(7):
		result = gamestate.drop(column, player_idx)
		#print(gamestate)
		#print("->")
		#print(result)
		#print(40*"-")
		if result is not None:
			result_val = minimax(result, -player_idx) * 0.9 # prioritize fast wins
			if best is None or best < player_idx * result_val:
				best = player_idx * result_val
	if best is None: best = 0
	
	cache[gamestate] = best
	return best

print("testing minimax")


gs = GameState()
gs.drop(1,-1)
gs.drop(2,-1)
gs.drop(3,-1)
gs.drop(2,1)
gs.drop(3,1)
gs.drop(4,1)
print( minimax(gs, -1) )
