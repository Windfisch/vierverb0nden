from GameState import GameState
import sys
from math import log

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

#print("testing minimax")


#gs = GameState()
#gs.drop_inplace(3,-1)
#gs.drop_inplace(2,-1)
#gs.drop_inplace(2,-1)
#gs.drop_inplace(3,-1)
#gs.drop_inplace(0,1)
#gs.drop_inplace(6,1)
#gs.drop_inplace(0,1)

cache = {}
limit = 5
def minimax_bfs(gamestate, player_idx):
	#cache = {}
	for i in range(limit+1):
		#print("limit %d" % i)
		result = minimax(gamestate, player_idx, i, cache)
		if result != None:
			return result
	
	cache[gamestate] = None
	return None
	
def sign(n):
	if n<0: return -1
	if n>0: return 1
	return 0

def prettify_result(num):
	if num == 0 or num == None:
		return 0
	else:
		return sign(num) * (-round(log(abs(num),2)))

def pprint(num):
	if num == 0 or num == None:
		print("?")
	else:
		print("%d wins in %d turns" % (num/abs(num), -round(log(abs(num),2))))

