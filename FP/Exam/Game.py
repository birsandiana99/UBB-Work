from Board import Board
from random import choice

class Game():
    def __init__(self,board = Board()):
        self._board = board
        
    
    def moveHuman(self,i,j,symbol):
        d = {"X":1,"O":-1}
        if symbol not in d.keys():
            raise ValueError("Symbol not correct!")
        
        if i >= 7 or j >=7 or i <= 0 or j <= 0:
            raise ValueError("Move is outside board!") 
        
        l = self._board.getData()
        if l[(i-1)*6+j-1] != 0:
            raise ValueError("Field already played!")
        
        
        self._board.move(i, j, symbol)
    
    def board(self):
        return self._board
       
    def moveComputer(self):
        '''
        Input: - 
        Output: computer moves on the board
        With the function getEmptySquares we find all the possible places where we can put X or O which are not used
        Moreover, in the function we check if there are already 4 elements of the same kind on a line/on a colum and if the answer is true, we block the move
    
        
        
        '''
        emptysquares = self._board.getEmptySquares()
        
        goodsquares = []
        listX = [1,1,1,1]
        listO = [-1,-1,-1,-1]
        l = self._board.getData()
        
        
        for i in range(6):
            for j in range(3):
                #print(i,j,l[i*6+j:i*6+j+4])
                if l[i*6+j:i*6+j+4] == listX:
                    if (i,j-1) in emptysquares:
                            goodsquares.append((i,j-1,"O"))
                
                    if (i,j+4) in emptysquares:
                            goodsquares.append((i,j+4,"O"))
                            
                if l[i*6+j:i*6+j+4] == listO:
                    if (i,j-1) in emptysquares:
                            goodsquares.append((i,j-1,"X"))
                
                    if (i,j+4) in emptysquares:
                            goodsquares.append((i,j+4,"X"))
                        
        for j in range(6):
            for i in range(3):
                if l[i*6+j:(i+3)*6+j+1:6] == listX:
                    print(emptysquares)
                    if (i-1,j) in emptysquares:
                        goodsquares.append((i-1,j,"O"))
                    if (i+4,j) in emptysquares:
                        goodsquares.append((i+4,j,"O"))
        
                if l[i*6+j:(i+3)*6+j+1:6] == listO:
                    if (i-1,j) in emptysquares:
                        goodsquares.append((i-1,j,"X"))
                    if (i+4,j) in emptysquares:
                        goodsquares.append((i+4,j,"X"))
        
        
        
        if goodsquares == []:
            print("es")
            c = choice(emptysquares)
            i = c[0]
            j = c[1]
            #d = {1:"X",-1:"O"}
            symbol = choice(["X","O"])
            self._board.move(i,j,symbol)
        else:
            print("Gs")
            #print(goodsquares)
            c = choice(goodsquares)
            #print(c)
            
            self._board.move(c[0]+1,c[1]+1,c[2])
    
    
    def isWon(self):
        '''
        1> pe linie
        2> pe coloana
        3> pe diagonala
        '''
        l = self._board.getData()
        listX = [1,1,1,1,1]
        listO = [-1,-1,-1,-1,-1]
        #1> pe linie
        for i in range(6):
            if l[i*6:i*6+5] == listX or l[i*6:i*6+5] == listO or l[i*6+1:i*6+6] == listX or l[i*6+1:i*6+6] == listO:
                return True 
        
        #2> pe coloana
        for j in range(6):
            if l[j:25+j:6]== listX or l[j:25+j:6]==listO or l[j+6:31+j:6]==listX or l[j+6:31+j:6] == listO:
                return True
            
          
        #3> pe diagonala CazI
        if l[0:29:7] == listX or l[0:29:7] == listO or l[7:36:7] == listX or l[7:36:7] == listO or l[1:30:7] == listX or l[1:30:7] == listO or l[6:35:7] == listX or l[6:35:7] == listO:
            return True
        
        
              
        #3> pe diagonala CazII
        if l[5:26:5] == listX or l[5:26:5] == listO or l[10:31:5]== listX or l[10:31:5]==listO or l[11:32:5] == listX or l[11:32:5] == listO or l[4:25:5] == listX or l[4:25:5] == listO :
            return True
        
        return False
    
    def isTie(self):
        if len(self._board.getEmptySquares()) == 0:
            return True
        return False
    
g = Game()


'''
#--ai--
g.moveHuman(1,1,"X")    
g.moveHuman(1,2,"X")    
g.moveHuman(1,3,"X")    
g.moveHuman(1,4,"X")   
print(g.board())   
g.moveComputer() 
print(g.board())



g.moveHuman(1,1,"X")    
g.moveHuman(2,1,"X")    
g.moveHuman(3,1,"X")    
g.moveHuman(4,1,"X")   
print(g.board())   
g.moveComputer() 
print(g.board())

diag2
g.moveHuman(1,6,"X")    
g.moveHuman(2,5,"X")    
g.moveHuman(3,4,"X")    
g.moveHuman(4,3,"X")    
g.moveHuman(5,2,"X") 

print(g.board())   
print(g.isWon())

g.moveHuman(2,5,"X")    
g.moveHuman(3,4,"X")    
g.moveHuman(4,3,"X")    
g.moveHuman(5,2,"X") 
g.moveHuman(6,1,"X")
print(g.board())   
print(g.isWon())

g.moveHuman(2,6,"X")    
g.moveHuman(3,5,"X")    
g.moveHuman(4,4,"X")    
g.moveHuman(5,3,"X") 
g.moveHuman(6,2,"X")
print(g.board())   
print(g.isWon())

g.moveHuman(1,5,"X")    
g.moveHuman(2,4,"X")    
g.moveHuman(3,3,"X")    
g.moveHuman(4,2,"X") 
g.moveHuman(5,1,"X")
print(g.board())   
print(g.isWon())



---
g.moveHuman(1,2,"X")    
g.moveHuman(1,3,"X")    
g.moveHuman(1,4,"X")    
g.moveHuman(1,5,"X")    
g.moveHuman(1,6,"X") 

print(g.board())   
print(g.isWon())

g.moveHuman(1,1,"X")    
g.moveHuman(1,2,"X")    
g.moveHuman(1,3,"X")    
g.moveHuman(1,4,"X")    
g.moveHuman(1,5,"X") 

print(g.board())   
print(g.isWon())

  
g.moveHuman(1,1,"X")    
g.moveHuman(2,1,"X")    
g.moveHuman(3,1,"X")    
g.moveHuman(4,1,"X") 
g.moveHuman(5,1,"X")    

print(g.board())   
print(g.isWon())

    
g.moveHuman(2,4,"X")    
g.moveHuman(3,5,"X")    
g.moveHuman(4,6,"X") 
g.moveHuman(5,4,"X")    
g.moveHuman(6,5,"X")    

print(g.board())   
print(g.isWon())


diag

g.moveHuman(1,1,"X")    
g.moveHuman(2,2,"X")    
g.moveHuman(3,3,"X")    
g.moveHuman(4,4,"X")    
g.moveHuman(5,5,"X") 

print(g.board())   
print(g.isWon())


g.moveHuman(2,2,"O")    
g.moveHuman(3,3,"O")    
g.moveHuman(4,4,"O")    
g.moveHuman(5,5,"O")    
g.moveHuman(6,6,"O") 

print(g.board())   
print(g.isWon())


'''
        
        
        
        
        
        