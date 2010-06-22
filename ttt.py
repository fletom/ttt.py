#!/usr/bin/env python
#
#  ttt.py
#  
#
#  Created by Fletcher Tomalty on 02/11/08.
#


from random import choice
from sys import stdout

class ttt:
	def __init__(self):
		self.game = None
		self.gameExists = False
		self.tokens = range(0,9)
		for x in xrange(0,9):
			self.tokens[x] = 0
				#Define orks.
		self.forks = []
			#Triangle Shape
				#Play centre
		self.forks.extend([[[0,2],[6,8,1],4], [[2,8],[0,6,5],4], [[8,6],[2,0,7],4], [[6,0],[8,2,3],4]])
				#Play left corner
		self.forks.extend([[[4,2],[6,8,1],0], [[4,8],[0,6,5],2], [[4,6],[2,0,7],8], [[4,0],[8,2,3],6]])
				#Play right corner
		self.forks.extend([[[4,0],[6,8,1],2], [[4,2],[0,6,5],8], [[4,8],[2,0,7],6], [[4,6],[8,2,3],0]])
			#Three Corners
				#Play bottom corner
		self.forks.extend([[[0,2],[1,5,4],8], [[2,8],[5,7,4],6], [[8,6],[7,3,4],0], [[6,0],[3,1,4],2]])
				#Play top right corner
		self.forks.extend([[[0,8],[1,5,4],2], [[2,6],[5,7,4],8], [[8,0],[7,3,4],6], [[6,2],[3,1,4],0]])
				#Play top left corner
		self.forks.extend([[[2,8],[1,5,4],0], [[8,6],[5,7,4],2], [[6,0],[7,3,4],8], [[0,2],[3,1,4],6]])
			#Knight's Move A
				#Play top right corner
		self.forks.extend([[[1,8],[0,5,1],2], [[5,6],[2,7,5],8], [[7,0],[8,3,7],6], [[3,2],[6,1,3],0]])
			#Knight's Move B
				#Play top right corner
		self.forks.extend([[[0,5],[1,8,0],2], [[2,7],[5,6,2],8], [[8,3],[7,0,8],6], [[6,1],[3,2,6],0]])
			#L A
		self.forks.extend([[[1,5],[0,8,1],2], [[5,7],[2,6,5],8], [[7,3],[8,0,7],6], [[3,1],[6,2,3],0]])
			#L B
		self.forks.extend([])
			#Spread A
		self.forks.extend([[[1,8],[2,4,1],0], [[5,6],[8,4,5],2], [[7,0],[6,4,7],8], [[3,2],[0,4,3],6]])
			#Spread B
		self.forks.extend([[[1,6],[0,4,1],2], [[5,0],[2,4,5],8], [[7,2],[8,4,7],6], [[3,8],[6,4,3],0]])

	def setToken(self,tokenPos,tokenVal):
		if (tokenPos < 0) or (tokenPos > 8): return ValueError, 'Token position must be no less than 0 and no greater than 8.'
		if (tokenVal < 0) or (tokenVal > 2): return ValueError, 'Token position must be no less than 0 and no greater than 2.'
		self.tokens[tokenPos] = tokenVal

	def setRandomToken(self,tokenVal,iterations=1):
			listEmpty = self.listEmptyTokens()
			if len(listEmpty) > iterations: raise ValueError
			for _ in xrange(iterations):
				randomEmpty = choice(listEmpty)
				if tokenVal == 3: self.setToken(randomEmpty,choice([1,2]))
				else: self.setToken(randomEmpty,tokenVal)
				listEmpty.remove(randomEmpty)
				
	def listEmptyTokens(self):
		listEmpty = []
		for x in xrange(0,9):
			if self.tokens[x] == 0: listEmpty.append(x)
		return listEmpty

	def clearAllTokens(self):
		for x in xrange(0,9):
			self.tokens[x] = 0

	def clearToken(self,tokenPos):
		self.tokens[tokenPos] = 0
		
	def bPrint(self):
		print self.tokens

	def getLetter(self,tokenPos):
		return self.letterValue(self.tokens[tokenPos])

	def letterValue(self,intValue):
		if intValue == 0: return " "
		elif intValue == 1: return "X"
		elif intValue == 2: return "O"
		else: raise ValueError

	def checkToken(self,tokenVal,tokenPos):
		if tokens[tokenPos] == tokenVal: return True
		else: return False
	
	def startGame(self): #0: human, 1: AI
		self.gameExists = True
		self.clearAllTokens()
		self.gameTurn = 1 #which piece will be played next (1: X, 2: O), is also playerx-1
		
	def stopGame(self):
		self.gameTurn = None
		self.gameExists = False

	def playRandom(self):
		if self.gameExists:
			self.setToken(choice(self.listEmptyTokens()),self.gameTurn)
		if self.gameTurn == 1: self.gameTurn = 2
		elif self.gameTurn == 2: self.gameTurn = 1
		else: raise ValueError

	def playHuman(self,tokenPos):
		if self.gameExists and self.tokens[tokenPos] == 0:
			self.setToken(tokenPos,self.gameTurn)
			if self.gameTurn == 1: self.gameTurn = 2
			elif self.gameTurn == 2: self.gameTurn = 1
		else: raise ValueError

	def playComputer(self):
		computerMove = None
		if self.gameTurn == 1: opponentPiece = 2
		elif self.gameTurn == 2: opponentPiece = 1
		else: raise ValueError
		
		#If is first move.
		if len(self.listEmptyTokens()) == 9 and computerMove == None: computerMove = choice([0,2,6,8,4])
		
		#Play winning piece if possible.
			#Find two vertical tokens of value self.gameTurn and play a third to win.
		for x in [0,1,2]:
			if (computerMove == None) and (self.gameTurn == self.tokens[x] == self.tokens[x+3]) and (self.tokens[x+6] == 0): computerMove = x+6
		for x in [3,4,5]:
			if (computerMove == None) and (self.gameTurn == self.tokens[x] == self.tokens[x+3]) and (self.tokens[x-3] == 0): computerMove = x-3
		for x in [6,7,8]:
			if (computerMove == None) and (self.gameTurn == self.tokens[x] == self.tokens[x-6]) and (self.tokens[x-3] == 0): computerMove = x-3
				
			#Find two horizontal tokens of value self.gameTurn and play a third to win.
		for x in [0,3,6]:
			if (computerMove == None) and (self.gameTurn == self.tokens[x] == self.tokens[x+1]) and (self.tokens[x+2] == 0): computerMove = x+2
		for x in [1,4,7]:
			if (computerMove == None) and (self.gameTurn == self.tokens[x] == self.tokens[x+1]) and (self.tokens[x-1] == 0): computerMove = x-1
		for x in [2,5,8]:
			if (computerMove == None) and (self.gameTurn == self.tokens[x] == self.tokens[x-2]) and (self.tokens[x-1] == 0): computerMove = x-1
		
			#Check diagonals for two tokens of value self.gameTurn and play the third to win.
				#From top right to bottom left.
		if (computerMove == None) and (self.gameTurn == self.tokens[0] == self.tokens[4]) and (self.tokens[8] == 0): computerMove = 8
		if (computerMove == None) and (self.gameTurn == self.tokens[4] == self.tokens[8]) and (self.tokens[0] == 0): computerMove = 0
		if (computerMove == None) and (self.gameTurn == self.tokens[8] == self.tokens[0]) and (self.tokens[4] == 0): computerMove = 4
				#From top left to bottom right.
		if (computerMove == None) and (self.gameTurn == self.tokens[2] == self.tokens[4]) and (self.tokens[6] == 0): computerMove = 6
		if (computerMove == None) and (self.gameTurn == self.tokens[4] == self.tokens[6]) and (self.tokens[2] == 0): computerMove = 2
		if (computerMove == None) and (self.gameTurn == self.tokens[6] == self.tokens[2]) and (self.tokens[4] == 0): computerMove = 4
		
		#Block opponent from winning if applicable.
				#Vertical streaks of two.
		for x in [0,1,2]:
			if (computerMove == None) and (opponentPiece == self.tokens[x] == self.tokens[x+3]) and (self.tokens[x+6] == 0): computerMove = x+6
		for x in [3,4,5]:
			if (computerMove == None) and (opponentPiece == self.tokens[x] == self.tokens[x+3]) and (self.tokens[x-3] == 0): computerMove = x-3
		for x in [6,7,8]:
			if (computerMove == None) and (opponentPiece == self.tokens[x] == self.tokens[x-6]) and (self.tokens[x-3] == 0): computerMove = x-3
				
			#Horizontal streaks of two opponent tokens.
		for x in [0,3,6]:
			if (computerMove == None) and (opponentPiece == self.tokens[x] == self.tokens[x+1]) and (self.tokens[x+2] == 0): computerMove = x+2
		for x in [1,4,7]:
			if (computerMove == None) and (opponentPiece == self.tokens[x] == self.tokens[x+1]) and (self.tokens[x-1] == 0): computerMove = x-1
		for x in [2,5,8]:
			if (computerMove == None) and (opponentPiece == self.tokens[x] == self.tokens[x-2]) and (self.tokens[x-1] == 0): computerMove = x-1
		
			#Diagonal streaks of two opponent tokens.
				#From top right to bottom left.
		if (computerMove == None) and (opponentPiece == self.tokens[0] == self.tokens[4]) and (self.tokens[8] == 0): computerMove = 8
		if (computerMove == None) and (opponentPiece == self.tokens[4] == self.tokens[8]) and (self.tokens[0] == 0): computerMove = 0
		if (computerMove == None) and (opponentPiece == self.tokens[8] == self.tokens[0]) and (self.tokens[4] == 0): computerMove = 4
				#From top left to bottom right.
		if (computerMove == None) and (opponentPiece == self.tokens[2] == self.tokens[4]) and (self.tokens[6] == 0): computerMove = 6
		if (computerMove == None) and (opponentPiece == self.tokens[4] == self.tokens[6]) and (self.tokens[2] == 0): computerMove = 2
		if (computerMove == None) and (opponentPiece == self.tokens[6] == self.tokens[2]) and (self.tokens[4] == 0): computerMove = 4	
		
		
		#Attempt to make a fork.
		if computerMove == None:
			for fork in self.forks:
				if (computerMove == None) and (self.gameTurn == self.tokens[fork[0][0]] == self.tokens[fork[0][1]]) and (self.tokens[fork[2]] == 0) and (sum(1 if x else 0 for x in [self.tokens[fork[1][0]] == 0,self.tokens[fork[1][1]] == 0, self.tokens[fork[1][2]] == 0]) >= 2): computerMove = fork[2]
		
		#Attempt to block a double fork.
		if (computerMove == None) and (self.tokens == [0,0,opponentPiece,0,self.gameTurn,0,opponentPiece,0,0] or self.tokens == [opponentPiece,0,0,0,self.gameTurn,0,0,0,opponentPiece]) and len(self.listEmptyTokens()) == 6: computerMove = choice([1,3,5,7])
		#Attempt to block a fork.
		if computerMove == None:
			for fork in self.forks:
				if (computerMove == None) and (opponentPiece == self.tokens[fork[0][0]] == self.tokens[fork[0][1]]) and (self.tokens[fork[2]] == 0) and (sum(1 if x else 0 for x in [self.tokens[fork[1][0]] == 0,self.tokens[fork[1][1]] == 0, self.tokens[fork[1][2]] == 0]) >= 2): computerMove = fork[2]


		#If centre is empty, play a token there.
		if (computerMove == None and self.tokens[4] == 0): computerMove = 4
		
		#If any corners are empty, play a token in any random one.
		if computerMove == None:
			emptyCorners = list(set(self.listEmptyTokens()) & set([0,2,6,8]))
			if emptyCorners != []:
				computerMove = choice(emptyCorners)
		
		#If no move has been determined, play a random piece.
		if (computerMove == None): computerMove = choice(self.listEmptyTokens())
			
		#Execute determined move.
		self.setToken(computerMove,self.gameTurn)
		if self.gameTurn == 1: self.gameTurn = 2
		elif self.gameTurn == 2: self.gameTurn = 1
		

	def checkWin(self):
		wins = []
		for x in [0,1,2]:
			if self.tokens[x] != 0 and (self.tokens[x] == self.tokens[x+3] == self.tokens[x+6]):
				wins.append([self.tokens[x],x,x+3,x+6])
		for x in [0,3,6]:
			if self.tokens[x] != 0 and (self.tokens[x] == self.tokens[x+1] == self.tokens[x+2]):
				wins.append([self.tokens[x],x,x+1,x+2])
		if self.tokens[0] != 0 and (self.tokens[0] == self.tokens[4] == self.tokens[8]):
			wins.append([self.tokens[0],0,4,8])
		if self.tokens[2] != 0 and (self.tokens[2] == self.tokens[4] == self.tokens[6]):
			wins.append([self.tokens[2],2,4,6])
		return wins

	def bRotate(self,direction='r'):
		if (direction == 'right' or direction == 'r'): self.tokens = [self.tokens[6], self.tokens[3], self.tokens[0], self.tokens[7], self.tokens[4], self.tokens[1], self.tokens[8], self.tokens[5], self.tokens[2]]
		elif (direction == 'left' or direction == 'l'): self.tokens = [self.tokens[2], self.tokens[5], self.tokens[8], self.tokens[1], self.tokens[4], self.tokens[7], self.tokens[0], self.tokens[3], self.tokens[6]]
		else: raise ValueError

	def bDisplay(self):
		print """
	 _________________
	|     |     |     |
	|  %s  |  %s  |  %s  |
	|_____|_____|_____|
	|     |     |     |
	|  %s  |  %s  |  %s  |
	|_____|_____|_____|
	|     |     |     |
	|  %s  |  %s  |  %s  |
	|_____|_____|_____|

""" %(self.getLetter(0), self.getLetter(1), self.getLetter(2), self.getLetter(3), self.getLetter(4), self.getLetter(5), self.getLetter(6), self.getLetter(7), self.getLetter(8))
		
		if self.gameExists: print '\tIt\'s player %i\'s turn.\n' %(self.gameTurn)
		if self.checkWin() != []:
			print
			for win in self.checkWin():
				print '%s\'s have won with tokens %i, %i, and %i.' %(self.letterValue(win[0]),win[1]+1,win[2]+1,win[3]+1)

	def runInterface(self):
		import re
		
		invalid = 'invalid'
		invalidargs = 'invalid arguments'
		error = 'unknown error'
		welcome = 'Welcome to the Tic-Tac-Toe CLI written by Fletcher Tomalty in Python. Type "help" for more information.'
		manual = """
		
LAYOUT:
	 _________________
	|     |     |     |
	|  1  |  2  |  3  |
	|_____|_____|_____|
	|     |     |     |
	|  4  |  5  |  6  |
	|_____|_____|_____|
	|     |     |     |
	|  7  |  8  |  9  |
	|_____|_____|_____|

INPUT:
	Input should be separated by " " (a space), but commas, periods and tabs will also work.
		
COMMANDS:
	'exit' - exits the CLI
	'man' or 'manual' or 'help' or '?' - displays this manual
	'set x y' or 's x y' - sets value x (1-9) to square y (1=x=X or 2=o=O)
	'setdisplay x y' or 'sd x y' - sets square x (1-9) to value y (1=x=X or 2=o=O) and then displays the Tic-Tac-Toe board in ASCII
	'setrand x y' or 'sr x y' - sets y (1-9) tokens of value x (1=x=X or 2=o=O or r=R=random) to a random empty square
	'display' or 'd' - displays the Tic-Tac-Toe board in ASCII
	'clear x' or 'c x' clears square x (0-9 or all=a)
	'rotate direction' or 'r direction' - rotates the entire board 90 degrees to the specified direction (r=right or l=left)
	'game x' or 'g x' - starts (s), restarts (rs), or stops (sp or end or e) a game
	'play x' or 'p x' - lets the player who's turn it is play a token at position x (1-9)
	'playrandom' or 'pr' - plays a random token for the current player
	'playcomputer' or 'pc' - lets the computer play a token at a position determined through an AI system

		
"""
		print '\n' + welcome + '\n'
		
		while True:
			try:
				cont = True
				command = str(raw_input('> '))
				command = command.lower()
				command = command.strip()
				command = re.sub(',|\.|\(|\)|\t|:|/',' ',command)
				command = re.sub('  *',' ',command)
				if command == '' or command == ' ':
					cont = False
				if cont:
					command = re.split(' ',command)
				if cont and (command[0] == 'exit' or command[0] == 'x'):
					print
					print 'Goodbye.'
					print
					break
				elif cont and (command[0] == 'man' or command[0] == 'manual' or command[0] == 'help' or command[0] == '?'):
					print manual
					cont = False
				elif cont and (command[0] == 'set' or command[0] == 's' or command[0] == 'setdisplay' or command[0] == 'sd'):
					if command[2] == 'X' or command[2] == 'x' or command[2] == '1': setVal = 1
					elif command[2] == 'O' or command[2] == 'o' or command[2] == '2': setVal = 2
					else: raise ValueError
					self.setToken(int(command[1])-1,setVal)
					if (command[0] == 'setdisplay' or command[0] == 'sd'): self.bDisplay()
					cont = False
				elif cont and (command[0] == 'display' or command[0] == 'd'):
					self.bDisplay()
					cont = False
				elif cont and (command[0] == 'clear' or command[0] == 'c'):
					if command[1] == 'all' or command[1] == 'a': self.clearAllTokens()
					else: self.clearToken(int(command[1])-1)
				elif cont and (command[0] == 'setrand' or command[0] == 'sr'):
					if len(command) == 2: command.append(1)
					if command[1] == 'X' or command[1] == 'x' or command[1] == '1': self.setRandomToken(1,int(command[2]))
					elif command[1] == 'O' or command[1] == 'o' or command[1] == '2': self.setRandomToken(2,int(command[2]))
					elif command[1] == 'r' or command[1] == 'R' or command[1] == 'random': self.setRandomToken(3,int(command[2]))
					else: raise ValueError
					cont = False
				elif cont and (command[0] == 'rotate' or command[0] == 'r'):
					self.bRotate(command[1])
					cont = False
				elif cont and (command[0] == 'game' or command[0] == 'g'):
					if (command[1] == 'start' or command[1] == 's'): self.startGame()
					if (command[1] == 'restart' or command[1] == 'rs'): self.startGame()
					if (command[1] == 'stop' or command[1] == 'sp' or command[1] == 'end' or command[1] == 'e'): self.stopGame()
					cont = False
				elif cont and (command[0] == 'play' or command[0] == 'p'):
					self.playHuman(int(command[1])-1)
					self.bDisplay()
					cont = False
				elif cont and (command[0] == 'playrandom' or command[0] == 'pr'):
					self.playRandom()
					self.bDisplay()
					cont = False
				elif cont and (command[0] == 'playcomputer' or command[0] == 'pc'):
					self.playComputer()
					self.bDisplay()
					cont = False
				elif cont and (command[0] == 'teststrategy' or command[0] == 'ts'):
					if command[2] == 'r' or command[2] == 'random' or command[2] == '0': command[2] = 0
					if command[2] == 'c' or command[2] == 'computer' or command[2] == '1': command[2] = 1
					if command[3] == 'true' or command[3] == 'yes' or command[3] == 'y' or command[3] == '1': command[3] = True
					if command[3] == 'false' or command[3] == 'no' or command[3] == 'n' or command[3] == '0': command[3] = False
					self.testStrategy(int(command[1]), int(command[2]),bool(command[3]))
					cont = False

				elif cont and command[0] == 'pass': cont = False
				elif cont: print invalid
			except (ValueError, IndexError, AttributeError): print invalidargs
			#except: print error
	
	
	def testStrategy(self,iterations,startingPlayer,display): #0==Random 1==Computer
		xwins = 0
		owins = 0
		print "\nProcessing..."
		print '\t',
		for _ in xrange(iterations):
			self.startGame()
			if display: print '\n\n---------------------------------------------------------------------------------------------\n\n'
			i = startingPlayer
			while (x.checkWin() == [] and i < 9+startingPlayer):
				if i % 2 == 0: self.playRandom()
				else: self.playComputer()
				i += 1
				if display: self.bDisplay()
			if self.checkWin() != []:
				if self.checkWin()[0][0] == 1:
					xwins += 1
				if self.checkWin()[0][0] == 2:
					owins += 1
				if display: self.bDisplay()
			if (iterations > 1000) and (_ % int(iterations/100.0) == 0) and (display == False): stdout.write("%i%% " %((_/float(iterations))*100)); stdout.flush()
		self.stopGame()
		if startingPlayer == 0: xPlayer, oPlayer = 'Random', 'Computer'
		if startingPlayer == 1: xPlayer, oPlayer = 'Computer', 'Random'
		print """\n\n
		%s won: %i - %.2f%%
		%s won: %i - %.2f%%
		Tied: %i - %.2f%%
		Total: %i - %.2f%%
				
		""" %(xPlayer, xwins, (float(xwins)/float(iterations))*100, oPlayer, owins, (float(owins)/float(iterations))*100,(iterations-(xwins+owins)), (float((iterations-(xwins+owins))))/float(iterations)*100,iterations,100.00)
		
		




x = ttt()
x.runInterface()

#END PROGRAM