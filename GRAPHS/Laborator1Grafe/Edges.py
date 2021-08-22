class Edge:
    def __init__(self, start, end, cost):
        self._start = start
        self._end = end
        self._cost = cost
        
    def EdgeTuple(self):
        return (self._start, self._end)
    
    def getStart(self):
        return self._start
    
    def getEnd(self):
        return self._end
    
    def getCost(self):
        return self._cost 
       
    def __equ__(self, secondEdge):
        if self._start == secondEdge.getStart() and self._end == secondEdge.getEnd():
            return 1
        return 0
    
    def setCost(self, newCost):
        self._cost = newCost
    