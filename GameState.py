class GameState:
	def __init__(self):
		self.state = []
		for i in range(7):
			self.state.append(6*[0])

		self.stacksizes = 7*[0]
	
	def drop(self, player_id, column_idx):
		assert(player_id in [-1,1])

		self.state[column_idx][ self.stacksizes[column_idx] ] = player_id
		self.stacksizes[column_idx] += 1
		
	def gameStateSafeAccess(self,col,row):
		if (col < 0) or (col > 6):
			return 0
		if (row < 0) or (row > 5):
			return 0
		return self.state[col][row]

	def check_win(self):
		print(self.state)
		for column in range(7):
			for row in range(6):
				verticalValue = sum(map(lambda x : self.gameStateSafeAccess(column,row+x),range(4)))
				horizontalValue = sum(map(lambda x : self.gameStateSafeAccess(column+x,row),range(4)))
				diagRising = sum(map(lambda x : self.gameStateSafeAccess(column+x,row+x),range(4)))
				diagFalling = sum(map(lambda x : self.gameStateSafeAccess(column+x,row-x),range(4)))
				
				player1 = max([verticalValue,horizontalValue,diagRising,diagFalling])
				player2 = min([verticalValue,horizontalValue,diagRising,diagFalling])
				
				if(player1 == 4):
					return 1
				if(player2 == -4):
					return -1
		return 0

def testSomebodyWin():
	gs = GameState()
	gs.drop(-1,0)
	gs.drop(-1,2)
	gs.drop(-1,3)
	
	return gs.check_win()
	
