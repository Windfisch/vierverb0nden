
def generateEmptyGameState():
	state = []
	for i in range(7):
		state.append(6*[0])
	return state

def gameStateSafeAccess(gameState,col,row):
	if (col < 0) or (col > 6):
		return 0
	if (row < 0) or (row > 5):
		return 0
	return gameState[col][row]

def didSomebodyWin(gameState):
	for column in range(7):
		for row in range(6):
			verticalValue = sum(map(lambda x : gameStateSafeAccess(gameState,column,row+x),range(4)))
			horizontalValue = sum(map(lambda x : gameStateSafeAccess(gameState,column+x,row),range(4)))
			diagRising = sum(map(lambda x : gameStateSafeAccess(gameState,column+x,row+x),range(4)))
			diagFalling = sum(map(lambda x : gameStateSafeAccess(gameState,column+x,row-x),range(4)))
			
			player1 = max([verticalValue,horizontalValue,diagRising,diagFalling])
			player2 = min([verticalValue,horizontalValue,diagRising,diagFalling])
			
			if(player1 == 4):
				return 1
			if(player2 == -4):
				return -1
	return 0

def testSomebodyWin():
	state = generateEmptyGameState()
	state[0][0] = -1
	state[1][0] = 0
	state[2][0] = -1
	state[3][0] = -1
	
	return didSomebodyWin(state)
	
print testSomebodyWin()
			
