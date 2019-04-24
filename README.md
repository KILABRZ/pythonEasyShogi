# pythonEasyShogi
shogi is a traditional and popular board game in Japan, kind of a catagory of chess.

this is a python shogi library that made for fun. (there is a more official one in github)

has not fully tested yet, but work well most of the time.

only test under Python 3.7, Windows 10, but should be work on Python 3.6 and other OS that can run Python. 

<h2>about library:</h2>

<h3>Interface:</h3>
	
	.shogi() to start a new game! (get a shogi object to start)
	
	.isUnderOte() check if current chesser is under Ote (checked) return True if yes
    
	.getPML()
		fill possibleMoveList by all possible move, if False, means chesser is 詰み (game over)
    
	.possibleMoveList 
		all possible move, a move is a 3 element tuple, describe like that:
			(oldpos, newpos, nari)
		oldpos is a 2-tuple, means the move is to move the piece on this position
		and newpos is its destination.
		nari is a boolean, true if piece promote after this move.
		position using traditional recording method, suji and dan, from 1 ~ 9
    
	.makeMove(move)
		to make a move, after make a move, chesser will change
		you can only make the move in possibleMoveList   
    
	.moveRecorder
		a list that record all the move in this game
		end with a string that show who is lose
    
	.cameraAngle
		change printout angle of the board, accept '先手' and '後手'
    
	.easyBoardPrint()
		print a board in an easy way
		後手's pieces have a | beside them
    
	.board
		get the current board
		board is a dictionary, key(x, y) correspond to the piece on this position
		all piece is a 2-tuple, like this ('先手', '飛'), or ('後手', '馬')
		key(0, 0) is a list to put mochigoma of sente
		key(10, 0) is a list to put mochigoma of gote
		mochigoma only record the piece style like this '步', '銀', '桂'
    
	.chesser
		get current chesser, has '先手' and '後手'

there is a obvious need of improvment in actual implement, but at least it work.

<h3>about test:</h3>

	test.py is a small test that two chesser will randomly throw possible step till end
