import tkinter as tk
from PIL import Image, ImageTk
import shogi
import random
import time

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

fuImage = ImageTk.PhotoImage(Image.open('images/fu.png'))
kyouImage = ImageTk.PhotoImage(Image.open('images/kyou.png'))
keImage = ImageTk.PhotoImage(Image.open('images/ke.png'))
ginImage = ImageTk.PhotoImage(Image.open('images/gin.png'))
kinImage = ImageTk.PhotoImage(Image.open('images/kin.png'))
ooImage = ImageTk.PhotoImage(Image.open('images/oo.png'))
gyouImage = ImageTk.PhotoImage(Image.open('images/gyou.png'))
hishaImage = ImageTk.PhotoImage(Image.open('images/hisha.png'))
kakuImage = ImageTk.PhotoImage(Image.open('images/kaku.png'))
toImage = ImageTk.PhotoImage(Image.open('images/to.png'))
narikyouImage = ImageTk.PhotoImage(Image.open('images/narikyou.png'))
narikeImage = ImageTk.PhotoImage(Image.open('images/narike.png'))
nariginImage = ImageTk.PhotoImage(Image.open('images/narigin.png'))
ryuuImage = ImageTk.PhotoImage(Image.open('images/ryuu.png'))
umaImage = ImageTk.PhotoImage(Image.open('images/uma.png'))

vfuImage = ImageTk.PhotoImage(Image.open('images/v_fu.png'))
vkyouImage = ImageTk.PhotoImage(Image.open('images/v_kyou.png'))
vkeImage = ImageTk.PhotoImage(Image.open('images/v_ke.png'))
vginImage = ImageTk.PhotoImage(Image.open('images/v_gin.png'))
vkinImage = ImageTk.PhotoImage(Image.open('images/v_kin.png'))
vooImage = ImageTk.PhotoImage(Image.open('images/v_oo.png'))
vgyouImage = ImageTk.PhotoImage(Image.open('images/v_gyou.png'))
vhishaImage = ImageTk.PhotoImage(Image.open('images/v_hisha.png'))
vkakuImage = ImageTk.PhotoImage(Image.open('images/v_kaku.png'))
vtoImage = ImageTk.PhotoImage(Image.open('images/v_to.png'))
vnarikyouImage = ImageTk.PhotoImage(Image.open('images/v_narikyou.png'))
vnarikeImage = ImageTk.PhotoImage(Image.open('images/v_narike.png'))
vnariginImage = ImageTk.PhotoImage(Image.open('images/v_narigin.png'))
vryuuImage = ImageTk.PhotoImage(Image.open('images/v_ryuu.png'))
vumaImage = ImageTk.PhotoImage(Image.open('images/v_uma.png'))
zeroImage = ImageTk.PhotoImage(Image.open('images/zero.png'))

gomaToImage_angleSente = {
	('先手', '步'):fuImage,
	('先手', '香'):kyouImage,
	('先手', '桂'):keImage,
	('先手', '銀'):ginImage,
	('先手', '金'):kinImage,
	('先手', '飛'):hishaImage,
	('先手', '角'):kakuImage,
	('先手', '王'):ooImage,
	('先手', 'と'):toImage,
	('先手', '杏'):narikyouImage,
	('先手', '圭'):narikeImage,
	('先手', '全'):nariginImage,
	('先手', '竜'):ryuuImage,
	('先手', '馬'):umaImage,
	('後手', '步'):vfuImage,
	('後手', '香'):vkyouImage,
	('後手', '桂'):vkeImage,
	('後手', '銀'):vginImage,
	('後手', '金'):vkinImage,
	('後手', '飛'):vhishaImage,
	('後手', '角'):vkakuImage,
	('後手', '王'):vgyouImage,
	('後手', 'と'):vtoImage,
	('後手', '杏'):vnarikyouImage,
	('後手', '圭'):vnarikeImage,
	('後手', '全'):vnariginImage,
	('後手', '竜'):vryuuImage,
	('後手', '馬'):vumaImage,
	('', '  '):zeroImage
}
gomaToImage_angleGote = {
	('後手', '步'):fuImage,
	('後手', '香'):kyouImage,
	('後手', '桂'):keImage,
	('後手', '銀'):ginImage,
	('後手', '金'):kinImage,
	('後手', '飛'):hishaImage,
	('後手', '角'):kakuImage,
	('後手', '王'):gyouImage,
	('後手', 'と'):toImage,
	('後手', '杏'):narikyouImage,
	('後手', '圭'):narikeImage,
	('後手', '全'):nariginImage,
	('後手', '竜'):ryuuImage,
	('後手', '馬'):umaImage,
	('先手', '步'):vfuImage,
	('先手', '香'):vkyouImage,
	('先手', '桂'):vkeImage,
	('先手', '銀'):vginImage,
	('先手', '金'):vkinImage,
	('先手', '飛'):vhishaImage,
	('先手', '角'):vkakuImage,
	('先手', '王'):vooImage,
	('先手', 'と'):vtoImage,
	('先手', '杏'):vnarikyouImage,
	('先手', '圭'):vnarikeImage,
	('先手', '全'):vnariginImage,
	('先手', '竜'):vryuuImage,
	('先手', '馬'):vumaImage,
	('', '  '):zeroImage
}

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
		print(maingame.moveRecorder[-1])
		while root:
			root.update_idletasks()
			root.update()
	time.sleep(0.0001)
	maingame.makeMove(random.choice(pml))