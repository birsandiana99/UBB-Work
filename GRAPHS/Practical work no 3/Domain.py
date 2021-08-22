class Graph:
    def __init__(self, n):
        self.__listIn = [[] for i in range(n)] #lista de liste self._listIn = []
        self.__listOut = [[] for i in range(n)]
        self.__size = n
        
        for i in range(0,n):
            #print(i)
            self.__listIn[i] = []
            self.__listOut[i] = []
        self.__edges = {} #dictionar in care cheia este perechea
        
    
    def getSize(self):
        '''
        Returns the size of the graph
        '''
        return self.__size
        
    def addEdge(self, start, end, cost):
        '''
        Adds an edge to the graph
        Input: start, end, cost - integers
        Output: add an edge represented by (start, end) and cost cost
        
        '''
        self.__listIn[end].append(start)
        self.__listOut[start].append(end)
        
        self.__edges[(start,end)]=cost   
        
        
    def removeEdge(self, start, end):
        '''
        Removes an edge specified by its start vertex(start) and end vertex(end)
        Input: start, end - integers
        Output: the edge start, end is removed
        
        '''
        #for i in range(0,len(self._edges)-1):
        #   if self._edges[i].key() == (start,end):
                #self._edges.pop(i)
        
        self.__edges.pop((start,end))
                
        #self._listIn[end].pop(start)
        #self._listOut[start].pop(end)
        
        #del self._listOut[start][end]
        #del self._listIn[end][start]
        
        '''
        for i in range(len(self._listOut[start])):
            if self._listOut[start][i] == end:
                self._listOut[start].pop(i)
                
            
        for j in range(len(self._listIn[end])):
            if self._listIn[end][j] == start:
                self._listIn[end].pop(j)
        
        '''
        
        self.__listOut[start].remove(end)
        self.__listIn[end].remove(start)
            #stergere si din in si din out
    
    def addVertex(self):
        '''
        adds a new vertex to the graph
        Input: - 
        Output: a new list is created in listIn and listOut and the size is increased        
        '''
        self.__size += 1
        self.__listIn.append([])
        self.__listOut.append([])
    
    def parse_outbound(self, x):
        #this function returns an enumerable containing all the outbound
        #neighbours of x.
        #x must be an existing vertex
        return self.__listOut[x]
        
    
    def createDemoGraph(self):
        graph = Graph(6)
        graph.addEdge(0,1,5)
        graph.addEdge(0,2,6)
        graph.addEdge(1,3,7)
        graph.addEdge(3,2,8)
        graph.addEdge(2,4,9)
        graph.addEdge(3,5,10)

        return graph
    
    def removeVertex(self, vertex):
        '''
        removes a given vertex (vertex) from the graph
        Input: vertex  - an integer
        Output: the given vertex is removed and all vertices are modified (the last one becomes the removed)
        
        '''
        self.__listIn[vertex]=[] #pt toate varfurile va trb sa verific daca e implicat
        self.__listOut[vertex]=[] #inainte sterg si apoi renumerotez
        
        new_edges={}
        for i in self.__edges.keys():
            if i[0] != vertex and i[1] != vertex:
                #if i == self.__size-1: new_edges[vertex]=self.__edges[i]
                new_edges[i]=self.__edges[i]
                
        self.__edges = new_edges
        #print(self._edges,"\n")
        
        for nod in range(self.__size-1):
            if vertex in self.__listIn[nod]:
                self.__listIn[nod].remove(vertex)
            
            if vertex in self.__listOut[nod]:    
                self.__listOut[nod].remove(vertex)
                
            #print("List in: ",nod,": ",self._listIn[nod])
            #print("List out: ",nod,": ",self._listOut[nod])
                
        if vertex == self.__size - 1:
            self.__size = self.__size - 1
        else:
            n = self.__size - 1 
            for nod in range(self.__size):
                if n in self.__listIn[nod]:
                    self.__listIn[nod].remove(n)
                    self.__listIn[nod].append(vertex)
                
                if n in self.__listOut[nod]:    
                    self.__listOut[nod].remove(n)
                    self.__listOut[nod].append(vertex)
                    
                    
                #print("List in: nod",nod,":", self.__listIn[nod])        
                #print("List out: nod",nod,":", self.__listOut[nod])   
            
            for i in range(len(self.__listIn[n])):
                if self.__listIn[n][i] != vertex:
                    self.__listIn[vertex].append(self.__listIn[n][i])
            for i in range(len(self.__listOut[n])):
                if self.__listOut[n][i] != vertex:
                    self.__listOut[vertex].append(self.__listOut[n][i])
                    
            for k in self.__edges.keys():
                if k[0] == self.__size - 1:
                    x = k[1]
                    value = self.__edges[k]
                    self.__edges.pop(k)
                    self.__edges[(vertex,x)] = value
                if k[1] == self.__size - 1:
                    x = k[0]
                    value = self.__edges[k]
                    self.__edges.pop(k)
                    self.__edges[(x,vertex)] = value
             
            self.__size = self.__size - 1
        
        #renumerotare
        
    def isEdge(self, start, end):
        '''
        Verifies if a certain tuple is an edge

        Input: start, end - integers representing the ending points of the edge to be verified
        Output: 1 if is edge, 0 otherwise
        
        '''
        if (start,end) in self.__edges.keys():
            return 1;
        return 0
    
    def findCost(self,start,end):
        if self.isEdge(start,end):
            return self.__edges[(start,end)]
        return -1
    
    def inDegree(self, vertex):
        '''
        Returns the in degree of a given vertex
        Input: vertex - an integer
        Output: the in degree of the vertex
        
        '''
        return len(self.__listIn[vertex])
    
    def outDegree(self, vertex):
        '''
        Returns the out degree of a given vertex
        Input: vertex - an integer
        Output: the out degree of the vertex
        
        '''
        return len(self.__listOut[vertex])
        
    def modifyCost(self, start, end, newCost):
        
        '''
        Modifies the cost of a certain edge given by its ending points
        Input: start, end - the ending points(integer), newCost- integer representing the new cost
        Output: the cost is modified
        '''
        
        '''
        for i in range(len(self._edges)):
            if self._edges[i].key() == (start, end):
                self._edges[i] = newCost
        '''
        if (start,end) not in self.__edges.keys():
            return -1
        self.__edges[(start,end)] = newCost      
        #sa verifici daca nu exista 
        # self._edges[(start,end)]
        return 1
    
    def toString(self):
        s1 = "List out: \n"
        for vertice in range(0,self.__size):
            s1 += str(vertice) + ": "
            for v in self.__listOut[vertice]:
                s1+= str(v) + " "
            s1+="\n"
        
        s2 = "\nList in: \n"
        for vertice in range(0,self.__size):
            s2 += str(vertice) + ": "
            for v in self.__listIn[vertice]:
                s2+= str(v) + " "
            s2+="\n"
            
        
            
        return s1+s2
    
    def setListIn(self,l):
        self.__listIn = l
    
    def setListOut(self,l):
        self.__listOut = l
    
    def setEdges(self,l):
        self.__edges = l
        
    def getListIn(self):
        return self.__listIn
    
    def getListOut(self):
        return self.__listOut
    
    def getEdges(self):
        return self.__edges
    
    def copyGraph(self):
        '''
        Copies the graph 
        Input: - 
        Output: returns another graph identical with the original one
        '''
        g1 = Graph(self.__size)
        g1.setListIn(self.__listIn)
        g1.setListOut(self.__listOut)
        g1.setEdges(self.__edges)
        
        return g1
            
    
    
    def bfs(self, start, end):
        '''
        Input: 
        Output: 
        '''
        
        if start < 0 or start >= self.__size or end < 0 or end >= self.__size:
            return "Invalid values for start and end"
        
       
        queue = []
        visited = set()
       
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            elif node not in visited:
                for adjacent in self.__listOut[node]:
                    new_path = list(path)
                    new_path.append(adjacent)
                    queue.append(new_path)
                    
                visited.add(node)
        
        return "No path found"
    
    


    
    
    
    