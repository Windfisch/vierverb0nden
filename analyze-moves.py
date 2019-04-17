import json
import sys
import datetime
import math

from minimax import *
from GameState import *

for line in sys.stdin:
	try:
		data = json.loads(line)
	except:
		print("got corrupt line '%s'. probably this is the end of the stream" % line)
		continue
	
	if data["type"] == "state" and data['params']['turn'] != -1:
		field = data['params']['field']
		turn = data['params']['turn']

		gsturn = 1 if turn == 1 else -1

		# pr0gramm -1/0/1 = empty/blue/red = GameState 0/-1/1
		# GameState -1/0/1 = blue/empty/red
		gs = GameState()

		for col in range(7):
			l = [42] * 6
			n_coins = 6
			for row in range(6):
				if field[row][col] == -1:
					l[-row-1] = 0
					n_coins -= 1
				elif field[row][col] == 0:
					l[-row-1] = -1
				else:
					l[-row-1] = 1
			gs.state[col] = l
			gs.stacksizes[col] = n_coins

			#for x in gs.state[col]:
			#	print(x,end=", ")
			#print( " | %d" % gs.stacksizes[col])

		result = []
		for col in range(7):
			gs2 = gs.drop(col, gsturn)
			if gs2 is not None:
				result += [prettify_result(minimax_bfs(gs2, -gsturn))]
			else:
				result += [1234]

		data['params']['analysis'] = result
	
	print(json.dumps(data))

