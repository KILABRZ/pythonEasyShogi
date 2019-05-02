import tkinter as tk
from gomaImage import *
import shogi
import random
import time
import simpleBot
import gc
root = tk.Tk()


W = 700
H = 700
DW = 125
DH = 125
gomaTPlace1 = 50
gomaTPlace2 = 600
GRID = 50

mainbase = tk.Canvas(root, width=W, height=H)

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
			cv.create_image(x, y, image=gomaToImage_angleSente[board[pos]])
		else:
			cv.create_image(x, y, image=gomaToImage_angleGote[board[pos]])
	mx = 0
	for mochigoma in shogistate.board[(0, 0)]:
		if shogistate.cameraAngle == '先手':
			cv.create_image(DW+mx*GRID, gomaTPlace2, image=gomaToImage_angleSente[mochigoma])
		else:
			cv.create_image(DW+mx*GRID, gomaTPlace1, image=gomaToImage_angleGote[mochigoma])
		mx += 1


	mx = 0
	for mochigoma in shogistate.board[(10, 0)]:
		if shogistate.cameraAngle == '先手':
			cv.create_image(DW+mx*GRID, gomaTPlace1, image=gomaToImage_angleSente[mochigoma])
		else:
			cv.create_image(DW+mx*GRID, gomaTPlace2, image=gomaToImage_angleGote[mochigoma])
		mx += 1

mainbase.pack()


def closing():
	root.destroy()
root.protocol("WM_DELETE_WINDOW", closing)
maingame = shogi.shogi()
maingame.cameraAngle = '後手'

KLA1 = simpleBot.autochesser([700, 14, 100, 124, 125, 6, 120, 22, 1])
KLA2 = simpleBot.autochesser([700, 50, 110, 80, 211, 2, 80, 33, 1])
dval1 = KLA1.valueing(maingame)
dval2 = KLA2.valueing(maingame)
val1 = 0
val2 = 0

while True:
	mainbase.delete('all')
	pasteboard(mainbase, maingame)
	mainbase.pack()
	root.update_idletasks()
	root.update()
	maingame.getPML()
	pml = maingame.possibleMoveList
	maingame.printDefenseState()
	if len(pml) == 0:
		mainbase.pack()	
		root.update_idletasks()
		root.update()
		print(maingame.moveRecorder[-1])
		for move in maingame.moveRecorder:
			print(move)
		file.close()
		while root:
			root.update_idletasks()
			root.update()
	time.sleep(0.0001)
	if maingame.chesser == '先手':
		move, val1 = KLA1.getMove(maingame, 3, 10)
		val1 -= dval1
		val1 = int(val1)
		print(val1)
		maingame.makeMove(move)
	else:
		move = random.choice(maingame.possibleMoveList)
		maingame.makeMove(move)
	gc.collect()