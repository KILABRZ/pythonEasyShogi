initialBoard = {
	(1, 1):('先手', '香'), (1, 2):('', '  '), (1, 3):('先手', '步'), (1, 4):('', '  '), (1, 5):('', '  '), 
	(2, 1):('先手', '桂'), (2, 2):('先手', '角'), (2, 3):('先手', '步'),  (2, 4):('', '  '), (2, 5):('', '  '),	
	(3, 1):('先手', '銀'), (3, 2):('', '  '), (3, 3):('先手', '步'), (3, 4):('', '  '), (3, 5):('', '  '),
	(4, 1):('先手', '金'), (4, 2):('', '  '), (4, 3):('先手', '步'), (4, 4):('', '  '), (4, 5):('', '  '),  
	(5, 1):('先手', '王'), (5, 2):('', '  '),  (5, 3):('先手', '步'), (5, 4):('', '  '), (5, 5):('', '  '), 
	(6, 1):('先手', '金'), (6, 2):('', '  '), (6, 3):('先手', '步'), (6, 4):('', '  '), (6, 5):('', '  '), 	
	(7, 1):('先手', '銀'), (7, 2):('', '  '), (7, 3):('先手', '步'), (7, 4):('', '  '), (7, 5):('', '  '), 
	(8, 1):('先手', '桂'), (8, 2):('先手', '飛'), (8, 3):('先手', '步'), (8, 4):('', '  '), (8, 5):('', '  '), 
	(9, 1):('先手', '香'), (9, 2):('', '  '), (9, 3):('先手', '步'), (9, 4):('', '  '), (9, 5):('', '  '), 
	(1, 6):('', '  '), (1, 7):('後手', '步'), (1, 8):('', '  '), (1, 9):('後手', '香'),
	(2, 6):('', '  '), (2, 7):('後手', '步'), (2, 8):('後手', '飛'), (2, 9):('後手', '桂'),
	(3, 6):('', '  '), (3, 7):('後手', '步'), (3, 8):('', '  '), (3, 9):('後手', '銀'),
	(4, 6):('', '  '), (4, 7):('後手', '步'), (4, 8):('', '  '), (4, 9):('後手', '金'),
	(5, 6):('', '  '), (5, 7):('後手', '步'), (5, 8):('', '  '), (5, 9):('後手', '王'),
	(6, 6):('', '  '), (6, 7):('後手', '步'), (6, 8):('', '  '), (6, 9):('後手', '金'),
	(7, 6):('', '  '), (7, 7):('後手', '步'), (7, 8):('', '  '), (7, 9):('後手', '銀'),
	(8, 6):('', '  '), (8, 7):('後手', '步'), (8, 8):('後手', '角'), (8, 9):('後手', '桂'),
	(9, 6):('', '  '), (9, 7):('後手', '步'), (9, 8):('', '  '), (9, 9):('後手', '香'),
	(0, 0):list(),
	(10, 0):list()
}

narigoma = {
	'步':'と',
	'香':'杏',
	'桂':'圭',
	'銀':'全',
	'角':'馬',
	'飛':'竜'
}

denarigoma = {
	'と':'步',
	'杏':'香',
	'圭':'桂',
	'全':'銀',
	'馬':'角',
	'竜':'飛',
	'步':'步',
	'桂':'桂',
	'香':'香',
	'銀':'銀',
	'金':'金',
	'飛':'飛',
	'角':'角',
	'王':'王'
}

sentegomaT = (0, 0)
gotegomaT = (10, 0)

fourdirection = [(0, 1), (1, 0), (0, -1), (-1, 0)]
fourdignodirection = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

def legalPos(suji, dan):
	if suji < 1 or suji > 9 or dan < 1 or dan > 9:
		return False
	return True


class shogi:
	def __init__(self):
		self.board = initialBoard
		self.chesser = '先手'
		self.moveRecorder = list()
		self.possibleMoveList = list()
		self.round = 1
		self.cameraAngle = '先手'
		self.stimulateFlag = False
	def isUnderOte(self):
		offsetSG = 0
		if self.chesser == '後手':
			offsetSG = -1
		else:
			offsetSG = 1
		suji = 1
		dan = 1
		for i in range(1, 10):
			for j in range(1, 10):
				if self.board[(i, j)] == (self.chesser, '王'):
					suji = i
					dan = j
					break
		another = '後手' if self.chesser == '先手' else '先手'
		if legalPos(suji-1, dan+2*offsetSG):
			if self.board[(suji-1, dan+2*offsetSG)] == (another, '桂'):
				return True
		if legalPos(suji+1, dan+2*offsetSG):
			if self.board[(suji+1, dan+2*offsetSG)] == (another, '桂'):
				return True
		if legalPos(suji, dan+1*offsetSG):
			if self.board[(suji, dan+1*offsetSG)] in ((another, '步'), (another, '金'), (another, '銀'), (another, '圭'), (another, '杏'), (another, '全'), (another, 'と')):
				return True
		if legalPos(suji-1, dan+1*offsetSG):
			if self.board[(suji-1, dan+1*offsetSG)] in ((another, '金'), (another, '銀'), (another, '圭'), (another, '杏'), (another, '全'), (another, 'と')):
				return True
		if legalPos(suji+1, dan+1*offsetSG):
			if self.board[(suji+1, dan+1*offsetSG)] in ((another, '金'), (another, '銀'), (another, '圭'), (another, '杏'), (another, '全'), (another, 'と')):
				return True
		if legalPos(suji-1, dan):
			if self.board[(suji-1, dan)] in ((another, '金'), (another, '圭'), (another, '杏'), (another, '全'), (another, 'と')):
				return True
		if legalPos(suji+1, dan):
			if self.board[(suji+1, dan)] in ((another, '金'), (another, '圭'), (another, '杏'), (another, '全'), (another, 'と')):
				return True
		if legalPos(suji-1, dan-1*offsetSG):
			if self.board[(suji-1, dan-1*offsetSG)] == (another, '銀'):
				return True
		if legalPos(suji+1, dan-1*offsetSG):
			if self.board[(suji+1, dan-1*offsetSG)] == (another, '銀'):
				return True
		if legalPos(suji, dan-1*offsetSG):
			if self.board[(suji, dan-1*offsetSG)] in ((another, '金'), (another, '圭'), (another, '杏'), (another, '全'), (another, 'と')):
				return True
		for i in range(1, 10, 1):
			if not legalPos(suji, dan+i*offsetSG): break
			if self.board[(suji, dan+i*offsetSG)] == (another, '香'): return True
			if self.board[(suji, dan+i*offsetSG)][0] != '': break

		for d in fourdirection:
			for i in range(1, 10, 1):
				checksuji = suji+d[0]*i
				checkdan = dan+d[1]*i
				if not legalPos(checksuji, checkdan): break
				if self.board[(checksuji, checkdan)] == (another, '飛'): return True
				if self.board[(checksuji, checkdan)] == (another, '竜'): return True
				if i == 1:
					if self.board[(checksuji, checkdan)] == (another, '馬'): return True
					if self.board[(checksuji, checkdan)] == (another, '王'): return True
				if self.board[(checksuji, checkdan)][0] != '': break
		for d in fourdignodirection:
			for i in range(1, 10, 1):
				checksuji = suji+d[0]*i
				checkdan = dan+d[1]*i
				if not legalPos(checksuji, checkdan): break
				if self.board[(checksuji, checkdan)][0] == self.chesser: break
				if self.board[(checksuji, checkdan)] == (another, '角'): return True
				if self.board[(checksuji, checkdan)] == (another, '馬'): return True
				if i == 1:
					if self.board[(checksuji, checkdan)] == (another, '竜'): return True
					if self.board[(checksuji, checkdan)] == (another, '王'): return True
				if self.board[(checksuji, checkdan)][0] != '': break
		return False
	def isLegalMove(self, move):
		underOteFlag = self.isUnderOte()
		prePiecePos, newPiecePos, nari = move
		if prePiecePos[0] < 0 or prePiecePos[0] > 10 or prePiecePos[1] < 0 or prePiecePos[1] > 10:
			return False
		if newPiecePos[0] < 1 or newPiecePos[0] > 9 or newPiecePos[1] < 1 or newPiecePos[1] > 9:
			return False
		if self.board[newPiecePos][0] == self.chesser:
			return False
		if prePiecePos[0] == 0:
			if underOteFlag:
				self.board[newPiecePos] = self.board[sentegomaT][prePiecePos[1]]
				if self.isUnderOte():
					self.board[newPiecePos] = ('', '  ')
					return False
			if self.board[sentegomaT][prePiecePos[1]][1] == '步' or self.board[sentegomaT][prePiecePos[1]][1] == '香':
				if newPiecePos[1] == 9: return False
			if self.board[sentegomaT][prePiecePos[1]][1] == '桂':
				if newPiecePos[1] >= 8: return False
			if self.board[sentegomaT][prePiecePos[1]][1] == '步':
				for dan in range(1, 10):
					if self.board[(newPiecePos[0], dan)] == ('先手', '步'): return False
				self.board[newPiecePos] = ('先手', '步')
				self.chesser = '後手'
				if self.isUnderOte():
					self.stimulateFlag = True
					if self.getPML() is False:
						self.chesser = '先手'
						self.board[newPiecePos] = ('', '  ')
						self.stimulateFlag = False
						return False
					else:
						self.chesser = '先手'
						self.board[newPiecePos] = ('', '  ')
						self.stimulateFlag = False
						self.possibleMoveList.pop()
				else:
					self.chesser = '先手'
					self.board[newPiecePos] = ('', '  ')
					self.stimulateFlag = False
			return True
		if prePiecePos[0] == 10:
			if underOteFlag:
				self.board[newPiecePos] = self.board[gotegomaT][prePiecePos[1]]
				if self.isUnderOte():
					self.board[newPiecePos] = ('', '  ')
					return False
			if self.board[gotegomaT][prePiecePos[1]][1] == '步' or self.board[gotegomaT][prePiecePos[1]][1] == '香':
				if newPiecePos[1] == 1: return False
			if self.board[gotegomaT][prePiecePos[1]][1] == '桂':
				if newPiecePos[1] <= 2: return False
			if self.board[gotegomaT][prePiecePos[1]][1] == '步':
				for dan in range(1, 10):
					if self.board[(newPiecePos[0], dan)] == ('後手', '步'): return False
				self.board[newPiecePos] = ('後手', '步')
				self.chesser = '先手'
				if self.isUnderOte():
					self.stimulateFlag = True
					if self.getPML() is False:
						self.chesser = '後手'
						self.board[newPiecePos] = ('', '  ')
						self.stimulateFlag = False
						return False
					else:
						self.chesser = '後手'
						self.board[newPiecePos] = ('', '  ')
						self.stimulateFlag = False
						self.possibleMoveList.pop()
				else:
					self.chesser = '後手'
					self.board[newPiecePos] = ('', '  ')
					self.stimulateFlag = False
			return True
		
		if self.board[prePiecePos][0] != self.chesser:
			return False
		if (self.board[prePiecePos][1] == '香' or self.board[prePiecePos][1] == '步') and newPiecePos[1] == 9 and self.chesser == '先手' and nari == False:
			return False
		if (self.board[prePiecePos][1] == '香' or self.board[prePiecePos][1] == '步') and newPiecePos[1] == 1 and self.chesser == '後手' and nari == False:
			return False
		if self.board[prePiecePos][1] == '桂' and newPiecePos[1] <= 2 and self.chesser == '後手' and nari == False:
			return False
		if self.board[prePiecePos][1] == '桂' and newPiecePos[1] >= 8 and self.chesser == '先手' and nari == False:
			return False
		


		if prePiecePos[0] >= 1 and prePiecePos[0] <= 9:
			tmpPiecePre = self.board[prePiecePos]
			tmpPieceNew = self.board[newPiecePos]
			self.board[newPiecePos] = self.board[prePiecePos]
			self.board[prePiecePos] = ('', '  ')
			if self.isUnderOte():
				self.board[newPiecePos] = tmpPieceNew
				self.board[prePiecePos] = tmpPiecePre
				return False
			self.board[newPiecePos] = tmpPieceNew
			self.board[prePiecePos] = tmpPiecePre
		return True


	def nariIki(self, dan):
		if self.chesser == '先手':
			if dan >= 7:
				return True
			else:
				return False
		else:
			if dan <= 3:
				return True
			else:
				return False
	
	def getPML(self):
		underOteFlag = self.isUnderOte()
		if not self.stimulateFlag:
			self.possibleMoveList.clear()
		offsetSG = 0
		if self.chesser == '後手':
			offsetSG = -1
		else:
			offsetSG = 1
		if self.chesser == '先手':
			for mochigoma in self.board[sentegomaT]:
				for suji in range(1, 10, 1):
					for dan in range(1, 10, 1):
						if self.board[(suji, dan)][0] == '':
							move = ((0, self.board[sentegomaT].index(mochigoma)), (suji, dan), False)
							if self.isLegalMove(move):
								self.possibleMoveList.append(move)
								if self.stimulateFlag: return True
		if self.chesser == '後手':
			for mochigoma in self.board[gotegomaT]:
				for suji in range(1, 10, 1):
					for dan in range(1, 10, 1):
						if self.board[(suji, dan)][0] == '':
							move = ((10, self.board[gotegomaT].index(mochigoma)), (suji, dan), False)
							if self.isLegalMove(move):
								self.possibleMoveList.append(move)
								if self.stimulateFlag: return True
		for key in self.board.keys():
			suji, dan = key	
			if self.board[key] == (self.chesser, '步'):
				move = ((suji, dan), (suji, dan+1*offsetSG), False)
				if self.isLegalMove(move):
					self.possibleMoveList.append(move)
					if self.stimulateFlag: return True
				if self.nariIki(dan+1*offsetSG):
					move = ((suji, dan), (suji, dan+1*offsetSG), True)
					if self.isLegalMove(move):
						self.possibleMoveList.append(move)
						if self.stimulateFlag: return True

						
			if self.board[key] == (self.chesser, '香'):
				for i in range(1, 9, 1):
					if dan+i*offsetSG < 1 or dan+i*offsetSG > 9:
						break
					move = ((suji, dan), (suji, dan+i*offsetSG), False)
					if self.isLegalMove(move): 
						self.possibleMoveList.append(move)
						if self.stimulateFlag: return True
					if self.nariIki(dan+i*offsetSG):
						move = ((suji, dan), (suji, dan+i*offsetSG), True)
						if self.isLegalMove(move): 
							self.possibleMoveList.append(move)
							if self.stimulateFlag: return True
					if self.board[(suji, dan+i*offsetSG)][0] != '':
						break


			if self.board[key] == (self.chesser, '桂'):
				moves = [((suji, dan), (suji-1, dan+2*offsetSG), False),
						((suji, dan), (suji+1, dan+2*offsetSG), False),]
				for move in moves:
					if self.isLegalMove(move):
						self.possibleMoveList.append(move)
						if self.stimulateFlag: return True
				if self.nariIki(dan+2*offsetSG):
					moves = [((suji, dan), (suji-1, dan+2*offsetSG), True),
						((suji, dan), (suji+1, dan+2*offsetSG), True),]
					for move in moves:
						if self.isLegalMove(move):
							self.possibleMoveList.append(move)
							if self.stimulateFlag: return True


			if self.board[key] == (self.chesser, '銀'):
				moves = [((suji, dan), (suji-1, dan+1*offsetSG), False),
						((suji, dan), (suji, dan+1*offsetSG), False),
						((suji, dan), (suji+1, dan+1*offsetSG), False),
						((suji, dan), (suji-1, dan-1*offsetSG), False),
						((suji, dan), (suji+1, dan-1*offsetSG), False)]
				for move in moves:
					if self.isLegalMove(move):
						self.possibleMoveList.append(move)
						if self.stimulateFlag: return True
				moves = [((suji, dan), (suji-1, dan+1*offsetSG), True),
						((suji, dan), (suji, dan+1*offsetSG), True),
						((suji, dan), (suji+1, dan+1*offsetSG), True),
						((suji, dan), (suji-1, dan-1*offsetSG), True),
						((suji, dan), (suji+1, dan-1*offsetSG), True)]
				for move in moves:
					if self.nariIki(move[1][1]) or self.nariIki(dan):
						if self.isLegalMove(move):
							self.possibleMoveList.append(move)
							if self.stimulateFlag: return True
			if self.board[key] in ((self.chesser, '金'), (self.chesser, '全'), (self.chesser, '圭'), (self.chesser, '杏'), (self.chesser, 'と')):
				moves = [((suji, dan), (suji-1, dan+1*offsetSG), False),
						((suji, dan), (suji, dan+1*offsetSG), False),
						((suji, dan), (suji+1, dan+1*offsetSG), False),
						((suji, dan), (suji-1, dan), False),
						((suji, dan), (suji+1, dan), False),
						((suji, dan), (suji, dan-1*offsetSG), False)]
				for move in moves:
					if self.isLegalMove(move):
						self.possibleMoveList.append(move)
						if self.stimulateFlag: return True
			if self.board[key] == (self.chesser, '王'):
				moves = [((suji, dan), (suji-1, dan+1*offsetSG), False),
						((suji, dan), (suji, dan+1*offsetSG), False),
						((suji, dan), (suji+1, dan+1*offsetSG), False),
						((suji, dan), (suji+1, dan), False),
						((suji, dan), (suji-1, dan), False),
						((suji, dan), (suji+1, dan-1*offsetSG), False),
						((suji, dan), (suji, dan-1*offsetSG), False),
						((suji, dan), (suji-1, dan-1*offsetSG), False)]
				for move in moves:
					if self.isLegalMove(move):
						self.possibleMoveList.append(move)
						if self.stimulateFlag: return True
			if self.board[key] == (self.chesser, '角') or self.board[key] == (self.chesser, '馬'):
				A, B, C, D = (True, True, True, True)
				if self.board[key] == (self.chesser, '馬'):
					moves = [((suji, dan), (suji+1, dan), False),
							((suji, dan), (suji, dan-1), False),
							((suji, dan), (suji-1, dan), False),
							((suji, dan), (suji, dan+1), False)]
					for move in moves:
						if self.isLegalMove(move): 
							self.possibleMoveList.append(move)
							if self.stimulateFlag: return True
				for i in range(1, 9, 1):
					if A:
						if suji+i <= 9 and dan+i <= 9:
							moveA = ((suji, dan), (suji+i, dan+i), False)
							if self.isLegalMove(moveA): 
								self.possibleMoveList.append(moveA)
								if self.stimulateFlag: return True
							if self.nariIki(dan) and self.board[key] == (self.chesser, '角'):
								moveA = ((suji, dan), (suji+i, dan+i), True)
								if self.isLegalMove(moveA): 
									self.possibleMoveList.append(moveA)
									if self.stimulateFlag: return True
							if self.board[(suji+i, dan+i)][0] != '':	
								A = False
					if B:
						if suji-i >= 1 and dan+i <= 9: 
							moveB = ((suji, dan), (suji-i, dan+i), False)
							if self.isLegalMove(moveB): 
								self.possibleMoveList.append(moveB)
								if self.stimulateFlag: return True
							if self.nariIki(dan) and self.board[key] == (self.chesser, '角'):
								moveB = ((suji, dan), (suji-i, dan+i), True)
								if self.isLegalMove(moveB): 
									self.possibleMoveList.append(moveB)
									if self.stimulateFlag: return True
							if self.board[(suji-i, dan+i)][0] != '':
								B = False
					if C:
						if suji+i <= 9 and dan-i >= 1: 
							moveC = ((suji, dan), (suji+i, dan-i), False)
							if self.isLegalMove(moveC): 
								self.possibleMoveList.append(moveC)
								if self.stimulateFlag: return True
							if self.nariIki(dan+i) and self.board[key] == (self.chesser, '角'):
								moveC = ((suji, dan), (suji+i, dan-i), True)
								if self.isLegalMove(moveC): 
									self.possibleMoveList.append(moveC)
									if self.stimulateFlag: return True
							if self.board[(suji+i, dan-i)][0] != '':
								C = False
					if D:
						if suji-i >= 1 and dan-i >= 1:
							moveD = ((suji, dan), (suji-i, dan-i), False)
							if self.isLegalMove(moveD): 
								self.possibleMoveList.append(moveD)
								if self.stimulateFlag: return True
							if self.nariIki(dan-i) and self.board[key] == (self.chesser, '角'):
								moveD = ((suji, dan), (suji-i, dan-i), True)
								if self.isLegalMove(moveD): 
									self.possibleMoveList.append(moveD)
									if self.stimulateFlag: return True
							if self.board[(suji-i, dan-i)][0] != '':
								D = False

			if self.board[key] == (self.chesser, '飛') or self.board[key] == (self.chesser, '竜'):
				A, B, C, D = (True, True, True, True)
				if self.board[key] == (self.chesser, '竜'):
					moves = [((suji, dan), (suji+1, dan+1), False),
							((suji, dan), (suji+1, dan-1), False),
							((suji, dan), (suji-1, dan+1), False),
							((suji, dan), (suji-1, dan-1), False)]
					for move in moves:
						if self.isLegalMove(move): 
							self.possibleMoveList.append(move)
							if self.stimulateFlag: return True
				for i in range(1, 9, 1):
					if A:
						if suji+i <= 9:
							moveA = ((suji, dan), (suji+i, dan), False)
							if self.isLegalMove(moveA): 
								self.possibleMoveList.append(moveA)
								if self.stimulateFlag: return True
							if self.nariIki(dan) and self.board[key] == (self.chesser, '飛'):
								moveA = ((suji, dan), (suji+i, dan), True)
								if self.isLegalMove(moveA): 
									self.possibleMoveList.append(moveA)
									if self.stimulateFlag: return True
							if self.board[(suji+i, dan)][0] != '':	
								A = False
					if B:
						if suji-i >= 1: 
							moveB = ((suji, dan), (suji-i, dan), False)
							if self.isLegalMove(moveB): 
								self.possibleMoveList.append(moveB)
								if self.stimulateFlag: return True
							if self.nariIki(dan) and self.board[key] == (self.chesser, '飛'):
								moveB = ((suji, dan), (suji-i, dan), True)
								if self.isLegalMove(moveB): 
									self.possibleMoveList.append(moveB)
									if self.stimulateFlag: return True
							if self.board[(suji-i, dan)][0] != '':
								B = False
					if C:
						if dan+i <= 9: 
							moveC = ((suji, dan), (suji, dan+i), False)
							if self.isLegalMove(moveC): 
								self.possibleMoveList.append(moveC)
								if self.stimulateFlag: return True
							if self.nariIki(dan+i) and self.board[key] == (self.chesser, '飛'):
								moveC = ((suji, dan), (suji, dan+i), True)
								if self.isLegalMove(moveC): 
									self.possibleMoveList.append(moveC)
									if self.stimulateFlag: return True
							if self.board[(suji, dan+i)][0] != '':
								C = False
					if D:
						if dan-i >= 1:
							moveD = ((suji, dan), (suji, dan-i), False)
							if self.isLegalMove(moveD): 
								self.possibleMoveList.append(moveD)
								if self.stimulateFlag: return True
							if self.nariIki(dan-i) and self.board[key] == (self.chesser, '飛'):
								moveD = ((suji, dan), (suji, dan-i), True)
								if self.isLegalMove(moveD): 
									self.possibleMoveList.append(moveD)
									if self.stimulateFlag: return True
							if self.board[(suji, dan-i)][0] != '':
								D = False
		if len(self.possibleMoveList) == 0:
			if not self.stimulateFlag:
				self.moveRecorder.append(str(self.round)+'手まで、'+self.chesser+'詰み\n')
			return False
		else:
			return True

	
	def makeMove(self, move):

		if move not in self.possibleMoveList:
			return False
		prePiecePos, newPiecePos, nari = move
		if prePiecePos[0] == 0 or prePiecePos[0] == 10:
			self.board[newPiecePos] = self.board[(prePiecePos[0], 0)][prePiecePos[1]]
			thelen = len(self.board[(prePiecePos[0], 0)]) - 1
			self.board[(prePiecePos[0], 0)][prePiecePos[1]] = self.board[(prePiecePos[0], 0)][thelen]
			self.board[(prePiecePos[0], 0)].pop()
			self.moveRecorder.append(move)
			return True

		else:	
			if self.board[newPiecePos][0] == '先手':
				self.board[gotegomaT].append(('後手', denarigoma[self.board[newPiecePos][1]]))
			if self.board[newPiecePos][0] == '後手':
				self.board[sentegomaT].append(('先手', denarigoma[self.board[newPiecePos][1]]))

			if nari is True:
				self.board[newPiecePos] = (self.board[prePiecePos][0], narigoma[self.board[prePiecePos][1]])
			else:
				self.board[newPiecePos] = self.board[prePiecePos]
			self.board[prePiecePos] = ('', '  ')
			self.round += 1
			self.chesser = '後手' if self.chesser == '先手' else '先手'
			self.moveRecorder.append(move)
	def easyBoardPrint(self):
		if self.cameraAngle == '先手':
			for dan in range(9, 0, -1):
				if dan == 9:
					print('   ', end='')
					for suji in range(1, 10, 1):
						print(suji, end='  ')
					print('')
				print(dan, ':', end='')
				for suji in range(1, 10, 1):
					pos = (suji, dan)
					if self.board[pos][0] == '先手':
						print(self.board[pos][1], end=' ')
					elif self.board[pos][0] == '後手':
						print(self.board[pos][1], end='|')
					else:
						print('. ', end=' ')
				print('')	
		else:
			for dan in range(1, 10, 1):
				
				if dan == 1:
					print('   ', end='')
					for suji in range(9, 0, -1):
						print(suji, end='  ')
					print('')
				print(dan, ':', end='')
				for suji in range(9, 0, -1):
					pos = (suji, dan)
					if self.board[pos][0] == '先手':
						print(self.board[pos][1], end='|')
					elif self.board[pos][0] == '後手':
						print(self.board[pos][1], end=' ')
					else:
						print('. ', end=' ')
				print('')
		print('先手持駒：', end='')
		for goma in self.board[sentegomaT]:
			print(goma[1], end=',')
		print('')
		print('後手持駒：', end='')
		for goma in self.board[gotegomaT]:
			print(goma[1], end=',')
		print('')

		
#	def revertMove(self):		todo function

		