'''
method or initial data about goma (piece)
'''


gomaPromote = {
	'步':'と',
	'香':'杏',
	'桂':'圭',
	'銀':'全',
	'角':'馬',
	'飛':'竜'
}
gomaDePromote = {
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

promotedGoma = ['と', '杏', '圭', '全', '竜', '馬', '金', '王']

gomaOrder = {
	'步':0,
	'香':1,
	'桂':2,
	'銀':3,
	'金':4,
	'角':5,
	'飛':6
}

# define how a goma move
# use [movingvector = [move]], if one move in moving vectior is invalid, then check another moving vector
gomaMove = {
	('先手', '步'):[[(0, 1)]],
	('先手', '香'):[[(0, i) for i in range(1, 9, 1)]],
	('先手', '桂'):[[(1, 2)],[(-1, 2)]],
	('先手', '銀'):[[(1, 1)], [(0, 1)], [(-1, 1)], [(1, -1)], [(-1, -1)]],
	('先手', '金'):[[(1, 1)], [(0, 1)], [(-1, 1)], [(1, 0)], [(-1, 0)], [(0, -1)]],
	('先手', '飛'):[[(0, i) for i in range(1, 9, 1)], 
					[(0, -i) for i in range(1, 9, 1)], 
					[(i, 0) for i in range(1, 9, 1)],
					[(-i, 0) for i in range(1, 9, 1)]],
	('先手', '角'):[[(i, i) for i in range(1, 9, 1)], 
					[(i, -i) for i in range(1, 9, 1)], 
					[(-i, i) for i in range(1, 9, 1)],
					[(-i, -i) for i in range(1, 9, 1)]],
	('先手', '王'):[[(1, 1)], [(0, 1)], [(-1, 1)], [(1, 0)], [(-1, 0)], [(0, -1)], [(1, -1)], [(-1, -1)]],
	('先手', 'と'):[[(1, 1)], [(0, 1)], [(-1, 1)], [(1, 0)], [(-1, 0)], [(0, -1)]],
	('先手', '杏'):[[(1, 1)], [(0, 1)], [(-1, 1)], [(1, 0)], [(-1, 0)], [(0, -1)]],
	('先手', '圭'):[[(1, 1)], [(0, 1)], [(-1, 1)], [(1, 0)], [(-1, 0)], [(0, -1)]],
	('先手', '全'):[[(1, 1)], [(0, 1)], [(-1, 1)], [(1, 0)], [(-1, 0)], [(0, -1)]],
	('先手', '竜'):[[(0, i) for i in range(1, 9, 1)], 
					[(0, -i) for i in range(1, 9, 1)], 
					[(i, 0) for i in range(1, 9, 1)],
					[(-i, 0) for i in range(1, 9, 1)],
					[(1, -1)], [(1, 1)], [(-1, -1)], [(-1, 1)]],
	('先手', '馬'):[[(i, i) for i in range(1, 9, 1)], 
					[(i, -i) for i in range(1, 9, 1)], 
					[(-i, i) for i in range(1, 9, 1)],
					[(-i, -i) for i in range(1, 9, 1)],
					[(1, 0)], [(0, 1)], [(0, -1)], [(-1, 0)]],
	('後手', '步'):[[(0, -1)]],
	('後手', '香'):[[(0, -i) for i in range(1, 9, 1)]],
	('後手', '桂'):[[(1, -2)], [(-1, -2)]],
	('後手', '銀'):[[(1, -1)], [(0, -1)], [(-1, -1)], [(1, 1)], [(-1, 1)]],
	('後手', '金'):[[(1, -1)], [(0, -1)], [(-1, -1)], [(1, 0)], [(-1, 0)], [(0, 1)]],
	('後手', '飛'):[[(0, i) for i in range(1, 9, 1)], 
					[(0, -i) for i in range(1, 9, 1)], 
					[(i, 0) for i in range(1, 9, 1)],
					[(-i, 0) for i in range(1, 9, 1)]],
	('後手', '角'):[[(i, i) for i in range(1, 9, 1)], 
					[(i, -i) for i in range(1, 9, 1)], 
					[(-i, i) for i in range(1, 9, 1)],
					[(-i, -i) for i in range(1, 9, 1)]],
	('後手', '王'):[[(1, 1)], [(0, 1)], [(-1, 1)], [(1, 0)], [(-1, 0)], [(0, -1)], [(1, -1)], [(-1, -1)]],
	('後手', 'と'):[[(1, -1)], [(0, -1)], [(-1, -1)], [(1, 0)], [(-1, 0)], [(0, 1)]],
	('後手', '杏'):[[(1, -1)], [(0, -1)], [(-1, -1)], [(1, 0)], [(-1, 0)], [(0, 1)]],
	('後手', '圭'):[[(1, -1)], [(0, -1)], [(-1, -1)], [(1, 0)], [(-1, 0)], [(0, 1)]],
	('後手', '全'):[[(1, -1)], [(0, -1)], [(-1, -1)], [(1, 0)], [(-1, 0)], [(0, 1)]],
	('後手', '竜'):[[(0, i) for i in range(1, 9, 1)], 
					[(0, -i) for i in range(1, 9, 1)], 
					[(i, 0) for i in range(1, 9, 1)],
					[(-i, 0) for i in range(1, 9, 1)],
					[(1, -1)], [(1, 1)], [(-1, -1)], [(-1, 1)]],
	('後手', '馬'):[[(i, i) for i in range(1, 9, 1)], 
					[(i, -i) for i in range(1, 9, 1)], 
					[(-i, i) for i in range(1, 9, 1)],
					[(-i, -i) for i in range(1, 9, 1)],
					[(1, 0)], [(0, 1)], [(0, -1)], [(-1, 0)]],
}

def legalPos(pos):
	suji, dan = pos
	if suji < 1 or suji > 9 or dan < 1 or dan > 9:
		return False
	return True

def getGomaPossibleMove(pos, board, goma):
	if not legalPos(pos):
		return False
	if goma not in gomaMove.keys():
		return False
	suji, dan = pos
	possiblemove = []
	allmoveVec = gomaMove[goma]
	
	for moveVec in allmoveVec:
		for move in moveVec:
			dsuji, ddan = move
			newsuji = suji + dsuji
			newdan = dan + ddan
			newpos = (newsuji, newdan)
			if not legalPos((newsuji, newdan)):
				break
			if board[newpos][0] == goma[0]:
				break
			
			else:
				possiblemove.append((pos, newpos, False))
				if goma[0] == '先手' and (dan >= 7 or newdan >= 7) and (goma[1] not in promotedGoma):
					possiblemove.append((pos, newpos, True))
				elif goma[0] == '後手' and (dan <= 3 or newdan <= 3) and (goma[1] not in promotedGoma):
					possiblemove.append((pos, newpos, True))
			if board[newpos][0] != '':
				break
	return possiblemove



