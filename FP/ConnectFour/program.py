from texttable import Texttable
from random import choice
from ctypes.test.test_array_in_pointer import Value
import unittest
class GameException(Exception):
    def __init__(self, msg):
        self._msg = msg
        
    @property
    def message(self):
        return self._msg
        
        
'''
    0 - empty square
    1 - X
   -1 - 0
'''

def contains(small, big):
    for i in range(len(big)-len(small)+1):
        for j in range(len(small)):
            if big[i+j] != small[j]:
                break
        else:
            return i, i+len(small)
    return False

class Board:
    def __init__(self):
        self._data = [0] * 42
    
    '''
    square - tuple (row,colum)
    symbol - X or 0
    '''
    def move(self,colum,symbol):
        colum = int(colum)
        if colum<0 or colum>6:
            raise GameException("Move is outside board!")
        if symbol not in ['1','2']:
            raise GameException("Must play 1 or 2!")
        
        ok = 0
        l = 5
        while l >= 0 and ok == 0 :
            if self._data[l*7+colum] != 0:
                l = l - 1
            else: 
                line = l
                ok = 1
        if ok == 0:
            raise GameException("This colum is not available!")
        
        d = {'1':1,'2':-1}
        
        self._data[line * 7+ colum] = d[symbol]
    
    def getEmptySquares(self):
        res = []
        
        for j in range(6,-1,-1):
            ok = 0
            l = 5
            while l >= 0 and ok == 0 :
                if self._data[l*7+j] != 0:
                    l = l - 1
                else: 
                    ok = 1
            if ok == 1:
                res.append(j)   
        
        print(res)
        
        vect = []
        v = [1,1,1]
        v1 = [-1,-1,-1]
        for i in range(5,-1,-1):
            for j in range(5):
                l = self._data[i*7+j : i*7+j+3]    
                #print(i,", ",j,": ",l)           
                if l == v or l == v1:
                    if j-1 in res and self._data[i*7+j-1] == 0 and self._data[i*7+j-2]:
                        vect.append(j-1)
                    if j+3 in res and self._data[i*7+j+3] == 0 and self._data[i*7+j+2]:
                        vect.append(j+3)
                
        
        for j in range(6,-1,-1):
            #print(j)
            for i in range(5,1,-1):
                l = self._data[i*7+j:(i-3)*7+j:-7]
                #print(i,": ",l)           
                if l == v or l == v1:
                    if j in res:
                        vect.append(j)
        
        
        '''
        for i in range(5,1,-1):
            for j in range(6,2,-1):
                l = self._data[i*7+j:(i-2)*7+j:-7]
                #print(i,": ",l)           
                if l == v or l == v1:
                    if j in res:
                        vect.append(j)
        '''
        #for j in range():
        
        if vect != []:
            print(1)
            return vect
        else:
            return res
    
    def isWon(self):
        v = [1,1,1,1]
        v1 = [-1,-1,-1,-1]
        #vertical
        for j in range(6):
            for i in range(3):
                l = self._data[i*7+j : (i+4)*7+j : 7]
                if l == v:
                    return 1
                elif l == v1:
                    return -1
        
        #horizontal
        for i in range(5,-1,-1):
            #print(i,":")
            for j in range(4):
                l = self._data[i*7+j : i*7+j+4]
                #print(l)               
                if l == v:
                    return 1
                elif l == v1:
                    return -1
        
        #diagonals
        for j in range(4): #we check the first 4 colums
            #print(j)
            for i in range(3):
                l = self._data[i*7+j:5*8-i+j+1:8] #i+j
                #l = self._data[i*7+j::8] #i+j
                
                if contains(v1,l):
                    return -1
                elif contains(v,l):
                    return 1
            for i in range(3,6):
                l = self._data[i+j:i*7+j+1:6] #i+j
                
                #print(i,":",i*7+j,",",i+j,":",l)
                #1print(contains(v,l))
                if contains(v1,l):
                    return -1
                elif contains(v,l):
                    return 1
                   
        
        return False
    
    def isTie(self):
        return self.isWon() == False and len(self.getEmptySquares()) == 0 
        
    def __str__(self):
        t = Texttable()   
        
        d = {0:" ",-1:"2",1:"1"}  # 2 for computer; 1 for user
        
        
        for i in range(6):
            lst = self._data[7*i:7*i+7]
            for j in range(len(lst)):
                lst[j] = d[lst[j]]
            t.add_row(lst)
            
        return t.draw()
        
 
class Game:
    def __init__(self, b = 0):
        if b != 0:
            self._board = b
        else:
            self._board = Board()
    
    @property
    def board(self):
        return self._board
    
    def moveHuman(self,colum):
        self._board.move(colum,'1')
    
    def moveComputer(self,colum=-1):
        if colum == -1:
            
            options = self.board.getEmptySquares()
            
            #print(options)
            
            self.board.move(choice(options),'2')
        else:
            self.board.move(colum,'2')

class UI:
    def __init__(self,game):
        self._game = game
    
    def readMove(self):
        while True:
            try:
                hmove = int(input("Enter colum>"))
                return hmove - 1
            except ValueError:
                print("Invalid input!")
        
    def start(self):
        b = self._game.board
        playerTurn = True
        while (b.isWon() == False) or (b.isTie == False):
            if playerTurn:
                print(self._game.board)
                try:
                    hMove = self.readMove()
                    self._game.moveHuman((hMove))
                except GameException as e:
                    print(str(e.message))
                    continue
            else: 
                self._game.moveComputer()
            playerTurn = not playerTurn
            
        print("Game over!")
        print(b)
        
        if b.isWon() == 1:
                print("Player won!")
        elif b.isWon() == -1:
                print("Computer won!")
        elif b.isTie() == True:
            print("Tie")
           
g = Game()
ui = UI(g)
ui.start()
