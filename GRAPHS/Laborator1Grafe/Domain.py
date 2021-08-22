from Edges import Edge
class Graph:
    def __init__(self, n):
        self._listIn = [] #lista de liste self._listIn = []
        self._listOut = []
        self._size = n
        
        for i in range(n):
            self._listIn[i] = []
            self._listOut[i] = []
        self._edges = {} #dictionar in care cheia este perechea
        
    def addEdge(self, start, end, cost):
        self._listIn[end].append(start)
        self._listOut[start].append(end)
        
        self._edges[(start,end)].append(cost)         
        
    def removeEdge(self, start, end):
        for i in range(0,len(self._edges)-1):
            if self._edges[i].key() == (start,end):
                self._edges.pop(i)
                
        del self._listIn[end][start]
        del self._listOut[start][end]
            #stergere si din in si din out
    
    def addVertex(self):
        self._size += 1
        self._listIn[self._size] = []
        self._listOut[self._size] = []
        
    def removeVertex(self, vertex):
        del self._listIn[vertex] #pt toate varfurile va trb sa verific daca e implicat
        del self._listOut[vertex] #inainte sterg si apoi renumerotez
        for i in range(0,len(self._edges)-1):
            x = self._edges[i].EdgeTuple()
            if x[0] == vertex or x[1] == vertex:
                self._edges.pop(i)
        #renumerotare
        
    def isEdge(self, start, end):
        for i in range(len(self._edges)):
            if self._edges[i].EdgeTuple() == (start,end):
                return 1
            
        return 0
    
    def inDegree(self, vertex):
        return len(self._listIn[vertex])
    
    def outDegree(self, vertex):
        return len(self._listOut[vertex])
        
    def modifyCost(self, start, end, newCost):
        for i in range(len(self._edges)):
            if self._edges[i].EdgeTuple() == (start, end):
                self._edges[i].setCost(newCost)
                
        #sa verifici daca nu exista 
        # self._edges[(start,end)]
        
        
        