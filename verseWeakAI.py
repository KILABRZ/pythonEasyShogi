import tkinter as tk
import shogi
import simpleBot
import random
import time
import gc


root = tk.Tk()

from gomaImage import *
W = 800
H = 800
DW = 175
DH = 175
gomaTPlace1 = 100
gomaTPlace2 = 670
GRID = 50

mainbase = tk.Canvas(root, width=W, height=H)
maingame = shogi.shogi()
maingame.cameraAngle = '後手'

prepos = 0
possibleNextPos = []
newpos = 0
nari = 0
eventFlag = 'doNothing'
#  doNothing, waitForChoosePiece, waitForChooseMove, waitForChooseNari, chooseMoveFinish,

def getgrid(x, y):
	x -= DW
	x = x//GRID
	y -= DH
	y = y//GRID
	return (x, y)

def suji2grid(suji, dan, temae):
	if temae == '先手':
		suji -= 1
		dan -= 1
		dan = 8-dan
	else:
		suji -= 1
		dan -= 1
		suji = 8-suji
	return (suji, dan)
def grid2suji(i, j, temae):
	if temae == '先手':
		j = 8 - j
		dan = j + 1
		suji = i + 1
	else:
		i = 8 - i
		dan = j + 1
		suji = i + 1
	return (suji, dan)

def getxy(i, j):
	return (DW+i*GRID, DH+j*GRID)

def pasteboard(cv, shogistate):
	board = shogistate.board
	for pos in board.keys():
		if not shogi.legalPos(pos):
			continue
		i, j = suji2grid(pos[0], pos[1], shogistate.cameraAngle)
		x, y = getxy(i, j)
		if shogistate.cameraAngle == '先手':
			if pos == prepos or pos in possibleNextPos:
				cv.create_image(x, y, image=gomaToYellowImage_angleSente[board[pos]])
			else:
				cv.create_image(x, y, image=gomaToImage_angleSente[board[pos]])

		else:
			if pos == prepos or pos in possibleNextPos:
				cv.create_image(x, y, image=gomaToYellowImage_angleGote[board[pos]])
			else:
				cv.create_image(x, y, image=gomaToImage_angleGote[board[pos]])
	mx = 0
	my = 0
	for mochigoma in shogistate.board[(0, 0)]:
		if mx >= 10:
			my += 1
			mx = 0
		if shogistate.cameraAngle == '先手':
			cv.create_image(DW+mx*GRID, gomaTPlace2+my*GRID, image=gomaToImage_angleSente[mochigoma])
		else:
			cv.create_image(DW+mx*GRID, gomaTPlace1-my*GRID, image=gomaToImage_angleGote[mochigoma])
		mx += 1


	mx = 0
	my = 0
	for mochigoma in shogistate.board[(10, 0)]:
		if mx >= 10:
			my += 1
			mx = 0
		if shogistate.cameraAngle == '先手':
			cv.create_image(DW+mx*GRID, gomaTPlace1-my*GRID, image=gomaToImage_angleSente[mochigoma])
		else:
			cv.create_image(DW+mx*GRID, gomaTPlace2+my*GRID, image=gomaToImage_angleGote[mochigoma])
		mx += 1

def chooseMove(event):
	global eventFlag, prepos, newpos, possibleNextPos, nari
	x, y = event.x+GRID//2, event.y+GRID//2
	if y >= gomaTPlace2:
		print('mouse is on the table')
		x -= DW
		y -= gomaTPlace2
		x //= GRID
		y //= GRID
		print(x, y)
		if x < 0 or y < 0 or x >= 10:
			eventFlag = 'doNothing'
			return 0

		idx = x + y*10
		gomaT = (0, 0) if maingame.chesser == '先手' else (10, 0)
		if idx < 0 or idx >= len(maingame.board[gomaT]):
			eventFlag = 'doNothing'
			return 0
		while idx > 0:
			if maingame.board[gomaT][idx] == maingame.board[gomaT][idx-1]:
				idx -= 1
			else:
				break
		prepos = (0, idx) if maingame.chesser == '先手' else (10, idx) 
		possibleNextPos = [nextmove[1] for nextmove in maingame.possibleMoveList if nextmove[0] == prepos]
		if len(possibleNextPos) <= 0:
			prepos = 0
			eventFlag = 'doNothing'
			return 0
		print(prepos)
		eventFlag = 'waitForChooseMove'
		return 1
	print(x, y)
	i, j = getgrid(x, y)
	print(i, j)
	suji, dan = grid2suji(i, j, maingame.cameraAngle)
	print(suji, dan)
	pos = (suji, dan)
	if eventFlag == 'doNothing':
		return 0
	if eventFlag == 'waitForChoosePiece':
		if not shogi.legalPos(pos):
			eventFlag = 'doNothing'
			return 0
		elif maingame.board[pos][0] != maingame.chesser:
			eventFlag = 'doNothing'
			return 0
		else:
			prepos = pos
			possibleNextPos = [nextmove[1] for nextmove in maingame.possibleMoveList if nextmove[0] == prepos]
			if len(possibleNextPos) <= 0:
				prepos = 0
				eventFlag = 'doNothing'
				return 0
			eventFlag = 'waitForChooseMove'
			return 1
	if eventFlag == 'waitForChooseMove':
		if not shogi.legalPos((suji, dan)):
			eventFlag = 'doNothing'
			possibleNextPos = []
			prepos = 0
			return 0
		elif pos not in possibleNextPos:
			eventFlag = 'doNothing'
			possibleNextPos = []
			prepos = 0
			return 0
		else:
			newpos = pos
			eventFlag = 'waitForChooseNari'
			pmove = [nextmove for nextmove in maingame.possibleMoveList if nextmove[0] == prepos and nextmove[1] == newpos]
			if len(pmove) == 0:
				eventFlag = 'doNothing'
				possibleNextPos = []
				prepos = 0
				return 0
			if len(pmove) == 1:	
				nari = pmove[0][2]
				eventFlag = 'chooseMoveFinish'
			return 0
	if eventFlag == 'waitForChooseNari':
		print('choose to do Nari by enter Y, Space or Enter')

def chooseNari(key):
	global eventFlag, prepos, newpos, possibleNextPos, nari
	print('get key', key.char)
	if eventFlag != 'waitForChooseNari':
		return 0
	else:
		if key.char == 'y' or key.char == 'Y' or key.char == ' ':
			nari = True
			eventFlag = 'chooseMoveFinish'
		else:
			nari = False
			eventFlag = 'chooseMoveFinish'


mainbase.bind('<Button-1>', chooseMove)
root.bind('<KeyPress>', chooseNari)
mainbase.pack()

def closing():
	root.destroy()
root.protocol("WM_DELETE_WINDOW", closing)


rival = simpleBot.autochesser([700, 14, 100, 124, 125, 6, 120, 22, 1])

dval = rival.valueing(maingame)
val = 0

while True:
	mainbase.delete('all')
	pasteboard(mainbase, maingame)
	mainbase.pack()
	root.update_idletasks()
	root.update()
	maingame.getPML()
	pml = maingame.possibleMoveList
	if len(pml) == 0:
		mainbase.pack()	
		root.update_idletasks()
		root.update()
		file = open('gamerecord_'+str(random.randint(0, 1000000))+'.txt', 'w')
		print(maingame.moveRecorder[-1])
		for move in maingame.moveRecorder:
			print(str(move)+'\n')
			file.write(str(move))
		file.close()
		while root:
			root.update_idletasks()
			root.update()
	time.sleep(0.0001)
	if maingame.chesser == '先手':
		move, val = rival.getMove(maingame, 3, 10)
		val -= dval
		val = int(val)
		print(val)
		maingame.makeMove(move)
	else:
		if eventFlag == 'doNothing':
			eventFlag = 'waitForChoosePiece'
		if eventFlag == 'chooseMoveFinish':
			move = (prepos, newpos, nari)
			maingame.makeMove(move)
			prepos = 0
			newpos = 0
			nari = 0
			possibleNextPos = []
			eventFlag = 'doNothing'


	gc.collect()

