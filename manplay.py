import shogi
import os
maingame = shogi.shogi()

while True:
	os.system('cls')
	maingame.easyBoardPrint()
	maingame.getPML()
	pml = maingame.possibleMoveList
	if len(pml) == 0:
		break
	while True:
		movestring = input().split()
		try:
			presuji = int(movestring[0])
			predan = int(movestring[1])
			newsuji = int(movestring[2])
			newdan = int(movestring[3])

			if movestring[4] == '+':
				nari = True
			else:
				nari = False
			move = ((presuji, predan), (newsuji, newdan), nari)
			if not maingame.makeMove(move):
				print('move wrong')
				continue
			break
		except:
			continue


endingDeclare = maingame.moveRecorder[-1]
print(endingDeclare)