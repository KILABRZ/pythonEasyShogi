import shogi
import random
newGame = shogi.shogi()
while newGame.round <= 1600:
	print('Round = ', newGame.round)
	if newGame.isUnderOte():
		print('王手盤面')
	newGame.easyBoardPrint()
	
	newGame.getPML()
	if len(newGame.possibleMoveList) == 0:
		break
	move = random.choice(newGame.possibleMoveList)
	print(move)
	newGame.makeMove(move)

endingDeclare = newGame.moveRecorder[-1]
print(endingDeclare)