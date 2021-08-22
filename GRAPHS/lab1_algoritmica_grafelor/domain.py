class Graph:
    def __init__(self, n):
        self.__listIn = {}
        self.__listOut = {}
        self._size = n-1
        self.__costs = {}
        
        
        for v in range(n):
            self.__listIn[v] = []
            self.__listOut[v] = [] 
            
        for v1 in range(n):
            for v2 in range(n):
                self.__costs[(v1,v2)] = 0 
            
    def getSize(self):
        return self._size
    
    
    def addEdge(self, v1, v2, cost):
        self.__costs[(v1,v2)] = self.__costs[(v2,v1)] = cost
        self.__listIn[v2].append(v1)
        self.__listOut[v1].append(v2)
        
    def iteratorIn(self, v):
        it = GraphIteratorIn(self,v)
        return it
    
    
    def iteratorOut(self, v):
        pass
        
class Edge():
    def __init__(self,source,target,cost):
        self._source = source
        self._target = target
        self._cost = cost
                
        
class GraphIteratorIn:
    def __init__(self, graph, vert):
        self._v = vert
        self._list = graph._Graph__listIn()[self._v]
        self._current = 0
        
    def first(self):
        return self._list[0]
    
    def valid(self):
        return  self._current < len(self._list)
    
    def current(self):
        return self._list[self._current]
    
    def next(self):
        if self.valid() == True:
            
            
    
            
            
            
            
            
            
            
            