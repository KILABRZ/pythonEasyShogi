import shogi
import random
import time
newGame = shogi.shogi()
while newGame.round <= 500:
	print('Round = ', newGame.round)
	if newGame.isUnderOte():
		print('王手盤面')
	newGame.easyBoardPrint()
	
	newGame.getPML()
	if len(newGame.possibleMoveList) == 0:
		break
	print(len(newGame.possibleMoveList))
	move = random.choice(newGame.possibleMoveList)
	print(move)
	newGame.makeMove(move)

endingDeclare = newGame.moveRecorder[-1]
print(endingDeclare)