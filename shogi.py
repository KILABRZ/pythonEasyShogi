from board import *    	# board method
from goma import *		# goma method

fourdirection = [(0, 1), (1, 0), (0, -1), (-1, 0)]
fourdignodirection = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
class shogi:
	def __init__(self):
		self.board = initialBoard
		self.chesser = '先手'
		self.moveRecorder = list()
		self.possibleMoveList = list()
		self.round = 1
		self.cameraAngle = '先手'
		self.stimulateFlag = False
	def posIsUnderAttack(self, pos):
		suji, dan = pos
		chesserDierction = -1 if self.chesser == '後手' else 1
		another = '後手' if self.chesser == '先手' else '先手'
		if legalPos((suji-1, dan+2*chesserDierction)):
			if self.board[(suji-1, dan+2*chesserDierction)] == (another, '桂'):
				return True
		if legalPos((suji+1, dan+2*chesserDierction)):
			if self.board[(suji+1, dan+2*chesserDierction)] == (another, '桂'):
				return True
		if legalPos((suji, dan+1*chesserDierction)):
			if self.board[(suji, dan+1*chesserDierction)] in ((another, '步'), (another, '金'), (another, '銀'), (another, '圭'), (another, '杏'), (another, '全'), (another, 'と')):
				return True
		if legalPos((suji-1, dan+1*chesserDierction)):
			if self.board[(suji-1, dan+1*chesserDierction)] in ((another, '金'), (another, '銀'), (another, '圭'), (another, '杏'), (another, '全'), (another, 'と')):
				return True
		if legalPos((suji+1, dan+1*chesserDierction)):
			if self.board[(suji+1, dan+1*chesserDierction)] in ((another, '金'), (another, '銀'), (another, '圭'), (another, '杏'), (another, '全'), (another, 'と')):
				return True
		if legalPos((suji-1, dan)):
			if self.board[(suji-1, dan)] in ((another, '金'), (another, '圭'), (another, '杏'), (another, '全'), (another, 'と')):
				return True
		if legalPos((suji+1, dan)):
			if self.board[(suji+1, dan)] in ((another, '金'), (another, '圭'), (another, '杏'), (another, '全'), (another, 'と')):
				return True
		if legalPos((suji-1, dan-1*chesserDierction)):
			if self.board[(suji-1, dan-1*chesserDierction)] == (another, '銀'):
				return True
		if legalPos((suji+1, dan-1*chesserDierction)):
			if self.board[(suji+1, dan-1*chesserDierction)] == (another, '銀'):
				return True
		if legalPos((suji, dan-1*chesserDierction)):
			if self.board[(suji, dan-1*chesserDierction)] in ((another, '金'), (another, '圭'), (another, '杏'), (another, '全'), (another, 'と')):
				return True
		for i in range(1, 10, 1):
			if not legalPos((suji, dan+i*chesserDierction)): break
			if self.board[(suji, dan+i*chesserDierction)] == (another, '香'): return True
			if self.board[(suji, dan+i*chesserDierction)][0] != '': break

		for d in fourdirection:
			for i in range(1, 10, 1):
				checksuji = suji+d[0]*i
				checkdan = dan+d[1]*i
				if not legalPos((checksuji, checkdan)): break
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
				if not legalPos((checksuji, checkdan)): break
				if self.board[(checksuji, checkdan)][0] == self.chesser: break
				if self.board[(checksuji, checkdan)] == (another, '角'): return True
				if self.board[(checksuji, checkdan)] == (another, '馬'): return True
				if i == 1:
					if self.board[(checksuji, checkdan)] == (another, '竜'): return True
					if self.board[(checksuji, checkdan)] == (another, '王'): return True
				if self.board[(checksuji, checkdan)][0] != '': break
		return False
	def posIsUnderDefense(self, pos):
		suji, dan = pos
		chesserDierction = 1 if self.chesser == '後手' else -1
		if legalPos((suji-1, dan+2*chesserDierction)):
			if self.board[(suji-1, dan+2*chesserDierction)] == (self.chesser, '桂'):
				return True
		if legalPos((suji+1, dan+2*chesserDierction)):
			if self.board[(suji+1, dan+2*chesserDierction)] == (self.chesser, '桂'):
				return True
		if legalPos((suji, dan+1*chesserDierction)):
			if self.board[(suji, dan+1*chesserDierction)] in ((self.chesser, '步'), (self.chesser, '金'), (self.chesser, '銀'), (self.chesser, '圭'), (self.chesser, '杏'), (self.chesser, '全'), (self.chesser, 'と')):
				return True
		if legalPos((suji-1, dan+1*chesserDierction)):
			if self.board[(suji-1, dan+1*chesserDierction)] in ((self.chesser, '金'), (self.chesser, '銀'), (self.chesser, '圭'), (self.chesser, '杏'), (self.chesser, '全'), (self.chesser, 'と')):
				return True
		if legalPos((suji+1, dan+1*chesserDierction)):
			if self.board[(suji+1, dan+1*chesserDierction)] in ((self.chesser, '金'), (self.chesser, '銀'), (self.chesser, '圭'), (self.chesser, '杏'), (self.chesser, '全'), (self.chesser, 'と')):
				return True
		if legalPos((suji-1, dan)):
			if self.board[(suji-1, dan)] in ((self.chesser, '金'), (self.chesser, '圭'), (self.chesser, '杏'), (self.chesser, '全'), (self.chesser, 'と')):
				return True
		if legalPos((suji+1, dan)):
			if self.board[(suji+1, dan)] in ((self.chesser, '金'), (self.chesser, '圭'), (self.chesser, '杏'), (self.chesser, '全'), (self.chesser, 'と')):
				return True
		if legalPos((suji-1, dan-1*chesserDierction)):
			if self.board[(suji-1, dan-1*chesserDierction)] == (self.chesser, '銀'):
				return True
		if legalPos((suji+1, dan-1*chesserDierction)):
			if self.board[(suji+1, dan-1*chesserDierction)] == (self.chesser, '銀'):
				return True
		if legalPos((suji, dan-1*chesserDierction)):
			if self.board[(suji, dan-1*chesserDierction)] in ((self.chesser, '金'), (self.chesser, '圭'), (self.chesser, '杏'), (self.chesser, '全'), (self.chesser, 'と')):
				return True
		for i in range(1, 10, 1):
			if not legalPos((suji, dan+i*chesserDierction)): break
			if self.board[(suji, dan+i*chesserDierction)] == (self.chesser, '香'): return True
			if self.board[(suji, dan+i*chesserDierction)][0] != '': break

		for d in fourdirection:
			for i in range(1, 10, 1):
				checksuji = suji+d[0]*i
				checkdan = dan+d[1]*i
				if not legalPos((checksuji, checkdan)): break
				if self.board[(checksuji, checkdan)] == (self.chesser, '飛'): return True
				if self.board[(checksuji, checkdan)] == (self.chesser, '竜'): return True
				if i == 1:
					if self.board[(checksuji, checkdan)] == (self.chesser, '馬'): return True
					if self.board[(checksuji, checkdan)] == (self.chesser, '王'): return True
				if self.board[(checksuji, checkdan)][0] != '': break
		for d in fourdignodirection:
			for i in range(1, 10, 1):
				checksuji = suji+d[0]*i
				checkdan = dan+d[1]*i
				if not legalPos((checksuji, checkdan)): break
				if self.board[(checksuji, checkdan)][0] == self.chesser: break
				if self.board[(checksuji, checkdan)] == (self.chesser, '角'): return True
				if self.board[(checksuji, checkdan)] == (self.chesser, '馬'): return True
				if i == 1:
					if self.board[(checksuji, checkdan)] == (self.chesser, '竜'): return True
					if self.board[(checksuji, checkdan)] == (self.chesser, '王'): return True
				if self.board[(checksuji, checkdan)][0] != '': break
		return False
	def isUnderOte(self):
		suji = 1
		dan = 1
		for i in range(1, 10):
			for j in range(1, 10):
				if self.board[(i, j)] == (self.chesser, '王'):
					suji = i
					dan = j
					break
		return self.posIsUnderAttack((suji, dan))

	

	def isLegalMove(self, move):
		underOteFlag = self.isUnderOte()
		prePiecePos, newPiecePos, nari = move
		if prePiecePos[0] < 0 or prePiecePos[0] > 10 or prePiecePos[1] < 0 or prePiecePos[1] > 10:
			return False
		if not legalPos(newPiecePos):
			return False
		if self.board[newPiecePos][0] == self.chesser:
			return False
		if prePiecePos[0] == 0:
			if self.board[sentegomaT][prePiecePos[1]][1] == '步' or self.board[sentegomaT][prePiecePos[1]][1] == '香':
				if newPiecePos[1] == 9: return False
			if self.board[sentegomaT][prePiecePos[1]][1] == '桂':
				if newPiecePos[1] >= 8: return False
			if self.board[sentegomaT][prePiecePos[1]][1] == '步':
				for dan in range(1, 10):
					if self.board[(newPiecePos[0], dan)] == ('先手', '步'): return False
			if underOteFlag:
				self.board[newPiecePos] = self.board[sentegomaT][prePiecePos[1]]
				if self.isUnderOte():
					self.board[newPiecePos] = ('', '  ')
					return False
				else:
					self.board[newPiecePos] = ('', '  ')
			if self.board[sentegomaT][prePiecePos[1]][1] == '步':
				self.board[newPiecePos] = ('先手', '步')
				self.chesser = '後手'
				if self.isUnderOte():
					self.stimulateFlag = True
					if self.getPML() == False:
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
			if self.board[gotegomaT][prePiecePos[1]][1] == '步' or self.board[gotegomaT][prePiecePos[1]][1] == '香':
				if newPiecePos[1] == 1: return False
			if self.board[gotegomaT][prePiecePos[1]][1] == '桂':
				if newPiecePos[1] <= 2: return False
			if self.board[gotegomaT][prePiecePos[1]][1] == '步':
				for dan in range(1, 10):
					if self.board[(newPiecePos[0], dan)] == ('後手', '步'): return False
			if underOteFlag:
				self.board[newPiecePos] = self.board[gotegomaT][prePiecePos[1]]
				if self.isUnderOte():
					self.board[newPiecePos] = ('', '  ')
					return False
				else:
					self.board[newPiecePos] = ('', '  ')
			if self.board[gotegomaT][prePiecePos[1]][1] == '步':
				self.board[newPiecePos] = ('後手', '步')
				self.chesser = '先手'
				if self.isUnderOte():
					self.stimulateFlag = True
					if self.getPML() == False:
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
	def getPML(self):
		underOteFlag = self.isUnderOte()
		if not self.stimulateFlag:
			self.possibleMoveList.clear()

		chesserDierction = -1 if self.chesser == '後手' else 1

		gomaT = sentegomaT if self.chesser == '先手' else gotegomaT		
		pregoma = ''
		for mochigoma in self.board[gomaT]:
			if pregoma == mochigoma:
				continue
			else:
				pregoma = mochigoma
			for suji in range(1, 10, 1):
				for dan in range(1, 10, 1):
					if self.board[(suji, dan)][0] == '':
						move = ((gomaT[0], self.board[gomaT].index(mochigoma)), (suji, dan), False)
						if self.isLegalMove(move):
							self.possibleMoveList.append(move)
							if self.stimulateFlag: 
								return True

		for pos in self.board.keys():
			suji, dan = pos
			returnvalue = getGomaPossibleMove(pos, self.board, self.board[pos])
			if returnvalue is False:
				continue
			for move in returnvalue:
				if self.isLegalMove(move):
					self.possibleMoveList.append(move)
					if self.stimulateFlag: 
						return True
		if self.stimulateFlag:
			return False
		if len(self.possibleMoveList) == 0:
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
			self.chesser = '後手' if self.chesser == '先手' else '先手'
			self.moveRecorder.append(move)
			self.board[(prePiecePos[0], 0)].sort(key=lambda val: gomaOrder[val[1]])
			return True

		else:	
			if self.board[newPiecePos][0] == '先手':
				self.board[gotegomaT].append(('後手', gomaDePromote[self.board[newPiecePos][1]]))
				self.board[gotegomaT].sort(key=lambda val: gomaOrder[val[1]])
			if self.board[newPiecePos][0] == '後手':
				self.board[sentegomaT].append(('先手', gomaDePromote[self.board[newPiecePos][1]]))
				self.board[sentegomaT].sort(key=lambda val: gomaOrder[val[1]])

			if nari is True:
				self.board[newPiecePos] = (self.board[prePiecePos][0], gomaPromote[self.board[prePiecePos][1]])
			else:
				self.board[newPiecePos] = self.board[prePiecePos]
			self.board[prePiecePos] = ('', '  ')
			self.round += 1
			self.chesser = '後手' if self.chesser == '先手' else '先手'
			self.moveRecorder.append(move)
			return True
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
	def printDefenseState(self):
		for dan in range(1, 10):
			for suji in range(9, 0, -1):
				pos = (suji, dan)
				if self.posIsUnderDefense(pos):
					print('x', end='')
				else:
					print('.', end='')
			print('')
		print('')
		
#	def revertMove(self):		todo function

