class GameState:
	def __init__(self):
		self.state = []
		for i in range(7):
			self.state.append(6*[0])

		self.stacksizes = 7*[0]
	
	def flipColors(self):
		self.state = list(map(lambda x : [-y for y in x]),self.state)
		
	def clone(self):
		newState = GameState()
		newState.state = list(map(lambda x : list(map(lambda y : y,x)),self.state))
		return newState
	
	def drop(self,column_idx,player_id):
		cloned = self.clone()
		if not cloned.drop_inplace(column_idx,player_id):
			return None
		return cloned
	
	def drop_inplace(self, column_idx,player_id):
		if(self.stacksizes[column_idx] >= 6):
			return False
		
		assert(player_id in [-1,1])

		self.state[column_idx][ self.stacksizes[column_idx] ] = player_id
		self.stacksizes[column_idx] += 1
		
		return True
		
	def gameStateSafeAccess(self,col,row):
		if (col < 0) or (col > 6):
			return 0
		if (row < 0) or (row > 5):
			return 0
		return self.state[col][row]

	def check_win(self):
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

	def __hash__(self):
		deletedMinusOne = list(map(lambda x : [1 if y==1 else 0 for y in x],self.state))
		
		_hash = 0
		for column in range(7):
			for row in range(6):
				_hash = _hash*2 + deletedMinusOne[column][row]
			_hash = _hash * 8 + self.stacksizes[column]
				

		return _hash
	
	def __eq__(self, other):
		return self.__hash__() == other.__hash__()
	def __str__(self):
		return str(self.state)

def testSomebodyWin():
	gs = GameState()
	gs.drop(0,-1)
	gs.drop(2,-1)
	gs.drop(3,-1)
	
	return gs.check_win()


print(testSomebodyWin())
