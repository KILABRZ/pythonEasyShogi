import shogi
import os
import random
import simpleBot
import gc
maingame = shogi.shogi()
KLA1 = simpleBot.autochesser([800, 1, 3, 40, 7])
KLA2 = simpleBot.autochesser([600, 50, 30, 1, 11])

dval1 = KLA1.valueing(maingame)
dval2 = KLA2.valueing(maingame)

val1 = 0
val2 = 0

while True:
#	os.system('cls')
	maingame.easyBoardPrint()
	print(val1, val2)
	maingame.getPML()
	pml = maingame.possibleMoveList
	if len(pml) == 0:
		break
	if maingame.chesser == '先手':
		move, val1, alpha1 = KLA1.getMove(maingame, 2)
		val1 -= dval1
		val1 = int(val1)
		print(val1, alpha1)
		maingame.makeMove(move)
	else:
		move, val2, alpha2 = KLA2.getMove(maingame, 2)
		val2 -= dval2
		val2 = int(val2)
		print(val2, alpha2)
		maingame.makeMove(move)
	gc.collect()


endingDeclare = maingame.moveRecorder[-1]
print(endingDeclare)