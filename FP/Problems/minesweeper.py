from texttable import Texttable
from random import choice
class Board:
    def __init__(self, size, mines):
        self._size = size
        self._mines = mines
        
        self._data = []
        self._revelead = []
        for i in range(self.size):
            self._data.append([' '] * self.size)
            self._revelead.append([False] * self.size)
            
        self._addMines()
        self._markMines()
    
    def _setMine(self,x,y):
        self._data[x][y] = 'X'
        
    def isMine(self,x,y):
        return self._data[x][y] == 'X'
    
    def _neighbours(self,x,y):
        neigh = [(x-1,y-1),(x+1,y+1),(x-1,y),(x-1,y+1),(x+1,y),(x+1,y-1),(x,y-1),(x,y+1)]
        i = 0
        while i < len(neigh):
            loc = neigh[i]
            if loc[0] not in list(range(self.size)):
                neigh.pop(i)
                continue
            if loc[1] not in list(range(self.size)):
                neigh.pop(i)
                continue
            
            i += 1
        return neigh
    
    def _markLocation(self,x,y):
        count = 0
        for l in self._neighbours(x, y):
            if self.isMine(l[0], l[1]):
                count += 1
        self._data[x][y] = count
    
    def _markMines(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.isMine(i, j) == False:
                    self._markLocation(i,j)
        
    
    def _addMines(self):
        locations = list(range(self.size ** 2))
        
        i = self._mines
        while i > 0:
            loc = choice(locations)
            locations.pop(locations.index(loc))
            
            self._setMine(loc // self.size, loc % self.size)
            
            i -= 1
    
    @property
    def size(self):
        return self._size
    
    def step(self,x,y):
        '''
        Step on <X,Y>
        Return:
            - False is stepped on mine
            - True otherwise
        '''
        if self.isMine(x, y):
            self._revelead[x][y] = True
            return False
        if self._data[x][y] != 0:
            self._revelead[x][y] = True
            return True
        
        q = []
        q.append((x,y))
        while len(q) > 0:
            loc = q.pop(0)
            self._revelead[loc[0]][loc[1]] = True
            
            if self._data[loc[0]][loc[1]] == 0:
                nextlocs = self._neighbours(loc[0], loc[1])
                for loc in nextlocs:
                    if self._data[loc[0]][loc[1]] != 'X' and self._revelead[loc[0]][loc[1]] == False:
                        q.append(loc)
            
        return True
            
    
    def str(self):
        t = Texttable()
        
        '''
        1. Build raw header
        '''
        res = [' ','A']
        i = self.size - 1
        while i > 0:
            res.append(chr(ord(res[-1]) + 1))
            i -= 1
            
        t.header(res)
        for i in range(self.size):
            res = []
            for j in range(self.size):
                res.append(self._data[i][j])
            t.add_row([i] + res)
        return t.draw()
    
    def __str__(self):
        t = Texttable()
        
        '''
        1. Build raw header
        '''
        res = [' ','A']
        i = self.size - 1
        while i > 0:
            res.append(chr(ord(res[-1]) + 1))
            i -= 1
            
        t.header(res)
        for i in range(self.size):
            res = []
            for j in range(self.size):
                if self._revelead[i][j] == True:
                    res.append(self._data[i][j])
                else:
                    res.append('?')
            t.add_row([i] + res)
        return t.draw()
    
class Game:
    pass

    
b = Board(8,10)
print(b)
flag = True
while flag:
    step = input(">")
    step = step.split(" ")
    flag = b.step(int(step[0]),int(step[1]))
    print(b)
