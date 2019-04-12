from GameState import GameState
import sys

sys.setrecursionlimit(99999)

# minimizes for player -1, maximizes for player 1
def minimax(gamestate, player_idx, recursion_limit, cache):
	if recursion_limit < 0:
		return None

	if gamestate in cache:
		return cache[gamestate]

	winner = gamestate.check_win()
	if winner != 0:
		cache[gamestate] = winner
		return winner

	best = None
	recursion_limited = False
	for column in range(7):
		result = gamestate.drop(column, player_idx)
		#print(gamestate)
		#print("->")
		#print(result)
		#print(40*"-")
		if result is not None:
			result_val = minimax(result, -player_idx, recursion_limit-1, cache)
			if result_val is not None:
				fitness = player_idx * result_val
				if best is None or best < fitness:
					best = fitness
			else:
				recursion_limited = True
	
	if best is None: best = 0

	if recursion_limited and best <= 0:
		return None
	else:
		cache[gamestate] = 0.5 * best * player_idx
		return 0.5 * best * player_idx

print("testing minimax")


gs = GameState()
gs.drop_inplace(3,-1)
gs.drop_inplace(4,-1)
gs.drop_inplace(4,-1)
gs.drop_inplace(3,-1)
gs.drop_inplace(0,1)
gs.drop_inplace(1,1)
gs.drop_inplace(0,1)


def minimax_bfs(gamestate, player_idx, limit):
	cache = {}
	for i in range(limit+1):
		result = minimax(gamestate, player_idx, i, cache)
		if result != None:
			return result
	return None
	

print( minimax_bfs(gs, -1, 3) )
