from texttable import Texttable
class Board:
    def __init__(self,l = [0]*36):
        self._data = l
    
    def __str__(self):
        t = Texttable()
        d = {1:"X",-1:"O",0:" "}
        for i in range(0,6):
            l=[]
            for j in range(0,6):
                #print(i,j)
                #print(i*6+j)
                l.append(d[self._data[i*6+j]])
            t.add_row(l)
        return t.draw()
    
    def move(self,i,j,symbol):
        d = {"X":1,"O":-1}
        self._data[(i-1)*6+j-1] = d[symbol]
    
    def getEmptySquares(self):
        emptysquares = []
        '''
        for i in range(0,6):
            for j in range(0,6):
                if self._data[i*6+j] == 0:
                    emptysquares.append((i,j))
        '''
        for i in range(36):
            if self._data[i] == 0:
                emptysquares.append((i//6,i%6))
                    

        return emptysquares
        
    def getData(self):
        return self._data
    
    

    
    


'''
b = Board()
print(b) 
b.move(3,2,"X")
b.move(3,2,"O")
b.move(2,2,"X")
print(b)  
print(b.getEmptySquares())    
''' 