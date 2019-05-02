import shogi
import random
import copy
gomaValue = {
	'步':1,
	'香':4,
	'桂':5,
	'銀':8,
	'金':9,
	'杏':9,
	'全':9,
	'圭':9,
	'と':10,
	'角':12,
	'飛':12,
	'馬':16,
	'竜':17,
	'王':50
}

def SIT0(n, shogistate):
# GOMA NUMBER CONSIDER
	sentegomaNum = 0
	gotegomaNum = 0
	for suji in range(1, 10):
		for dan in range(1, 10):
			if shogistate.board[(suji, dan)][0] == '先手':
				sentegomaNum += gomaValue[shogistate.board[(suji, dan)][1]]
			elif shogistate.board[(suji, dan)][0] == '後手':
				gotegomaNum += gomaValue[shogistate.board[(suji, dan)][1]]
	for mochigoma in shogistate.board[(0, 0)]:
		sentegomaNum += gomaValue[mochigoma[1]]
	for mochigoma in shogistate.board[(10, 0)]:
		gotegomaNum += gomaValue[mochigoma[1]]
	difference = sentegomaNum - gotegomaNum
	if shogistate.chesser == '先手':
		return n * difference
	else:
		return -n * difference
def SIT1(n, shogistate):
	# 5 dan koe
	Pt = 0
	for dan in range(1, 10, 1):
		for suji in range(1, 10, 1):
			if shogistate.board[(suji, dan)][0] == shogistate.chesser and dan >= 5:
				Pt += 1
			if shogistate.board[(suji, dan)][0] == shogistate.chesser and dan <= 5:
				Pt += 1
	return Pt*n
def SIT2(n, shogistate):
	# under OTE
	if shogistate.isUnderOte():
		return -n
	else:
		return 1
def SIT3(n, shogistate):
	# Ou's front pieces
	pt = 0
	odan = 0
	osuji = 0
	for dan in range(1, 10, 1):
		for suji in range(1, 10, 1):
			if shogistate.board[(suji, dan)] == (shogistate.chesser, '王'):
				odan, osuji = dan, suji
	for suji in [suji-1, suji, suji+1]:
		for dan in range(1, 10, 1):
			if not shogi.legalPos((suji, dan)): continue
			if shogistate.chesser == '先手' and shogistate.board[(suji, dan)][0] == '後手' and dan >= odan:
				pt -= 10
			if shogistate.chesser == '後手' and shogistate.board[(suji, dan)][0] == '先手' and dan <= odan:
				pt -= 10

			if shogistate.chesser == '先手' and shogistate.board[(suji, dan)][0] == '先手' and dan >= odan:
				pt += 10
			if shogistate.chesser == '後手' and shogistate.board[(suji, dan)][0] == '後手' and dan <= odan:
				pt += 10
	return n*pt
def SIT4(n, shogistate):
	# good place of kaku and sha
	pt = 0
	kakusuji = 0
	kakudan = 0
	shasuji = 0
	shadan = 0
	another = '先手' if shogistate.chesser == '後手' else '後手'
	for suji in range(1, 10):
		for dan in range(1, 10):
			if shogistate.board[(suji, dan)] == (shogistate.chesser, '角') or shogistate.board[(suji, dan)] == (shogistate.chesser, '馬'):
				kakudan = dan
				kakusuji = suji
			if shogistate.board[(suji, dan)] == (shogistate.chesser, '飛') or shogistate.board[(suji, dan)] == (shogistate.chesser, '竜'):
				shadan = dan
				shasuji = suji

	for dsuji, ddan in [(1, 1), (1, -1), (-1, -1), (-1, 1)]:
		for i in range(1, 9):
			kakuppos = (kakusuji+i*dsuji, kakudan+i*ddan)
			if not shogi.legalPos(kakuppos):
				break
			if shogistate.board[kakuppos][0] != '':
				break
			else:
				pt += n*1.2
	for dsuji, ddan in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
		for i in range(1, 9):
			shappos = (shasuji+i*dsuji, shadan+i*ddan)
			if not shogi.legalPos(shappos):
				break
			if shogistate.board[shappos][0] != '':
				break
			else:
				pt += n*1.2
	for suji in range(1, 10):
		for dan in range(1, 10):
			if shogistate.board[(suji, dan)] == (another, '角') or shogistate.board[(suji, dan)] == (another, '馬'):
				kakudan = dan
				kakusuji = suji
			if shogistate.board[(suji, dan)] == (another, '飛') or shogistate.board[(suji, dan)] == (another, '竜'):
				shadan = dan
				shasuji = suji

	for dsuji, ddan in [(1, 1), (1, -1), (-1, -1), (-1, 1)]:
		for i in range(1, 9):
			kakuppos = (kakusuji+i*dsuji, kakudan+i*ddan)
			if not shogi.legalPos(kakuppos):
				break
			if shogistate.board[kakuppos][0] != '':
				break
			else:
				pt -= n*0.8
	for dsuji, ddan in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
		for i in range(1, 9):
			shappos = (shasuji+i*dsuji, shadan+i*ddan)
			if not shogi.legalPos(shappos):
				break
			if shogistate.board[shappos][0] != '':
				break
			else:
				pt -= n*0.8
	return pt

def SIT5(n, shogistate):
	myfree = len(shogistate.possibleMoveList)
	shogistate.chesser = '先手' if shogistate.chesser == '後手' else '後手'
	anofree = len(shogistate.possibleMoveList)
	shogistate.chesser = '先手' if shogistate.chesser == '後手' else '後手'
	pt = myfree - anofree
	return pt * n

def SIT6(n, shogistate):
	pt = 0
	weakerlist = []
	for boardspace in shogistate.board.items():
		pos, goma = boardspace
		if not shogi.legalPos(pos): continue
		if goma == (shogistate.chesser, '桂'):
			weakerlist.append((pos, 1))
		if goma == (shogistate.chesser, '角'):
			weakerlist.append((pos, 13))
		if goma == (shogistate.chesser, '王'):
			weakerlist.append((pos, 47))
	for pakc in weakerlist:
		pos, val = pakc
		if shogistate.posIsUnderAttack(pos):
			pt -= n*4
		for d in [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]:
			x, y = d
			suji, dan = pos
			suji += x
			dan += y
			if not shogi.legalPos(pos): continue
			if shogistate.posIsUnderAttack(pos):
				pt -= n*val


	return pt

def SIT7(n, shogistate):
	if shogistate.round > 7: return 0
	shapos = 0
	for boardspace in shogistate.board.items():
		pos, goma = boardspace
		if not shogi.legalPos(pos): continue
		if goma == (shogistate.chesser, '飛'):
			shappos = pos
			break
	if shapos == 0:
		return -n/9
	if shapos[0] == (n % 9) + 1:
		return n/9
	else:
		return -n/90
def SIT8(n, shogistate):
	if len(shogistate.possibleMoveList) == 0:
		return -9999999999
		print('詰み筋')
	else:
		return 1


situations = [SIT0, SIT1, SIT2, SIT3, SIT4, SIT5, SIT6, SIT7, SIT8]
class autochesser:
	def __init__(self, valvec):
		self.number = 0
		self.valueingVector = valvec
	def valueing(self, shogistate):
		sumvalue = 0
		for para in self.valueingVector:
			if para == 0: continue
			sumvalue += situations[self.valueingVector.index(para)](para, shogistate)
		return sumvalue
	def getMove(self, shogistate, thinkingdepth, thinkingbreadth):
		if type(shogistate) is not shogi.shogi:
			return False
		if thinkingdepth <= 0:
			shogistate.getPML()
			return ('', self.valueing(shogistate))
		shogistate.getPML()
		if len(shogistate.possibleMoveList) == 0:
			return ('', -999999999)
		if len(shogistate.possibleMoveList) == 1:
			return (shogistate.possibleMoveList[0], 0)
		valuelist = list()
		for move in shogistate.possibleMoveList:
			newstate = copy.deepcopy(shogistate)
			newstate.makeMove(move)
			newstate.chesser = '先手' if newstate.chesser == '後手' else '後手'
			value = (self.valueing(newstate))
			valuelist.append((move, value + random.randint(-100, 100)))
			del newstate
		valuelist.sort(key=lambda val:-val[1])
		bestmove = ''
		bestvalue = -5000000
		if len(shogistate.possibleMoveList) < thinkingbreadth:
			thinkingbreadth = len(shogistate.possibleMoveList)
		for i in range(thinkingbreadth):
			move, value = valuelist[i]
			newstate = copy.deepcopy(shogistate)
			newstate.makeMove(move)

			newmove, realvalue = self.getMove(newstate, thinkingdepth-1, 3)
			if -realvalue > bestvalue:
				bestvalue = -realvalue
				bestmove = move
			del newstate
		return (bestmove, bestvalue)
