from Domain import Graph
from Iterator import *
from UI import *

class UI:
    def __init__(self):
        pass
    
    def printMenu(self):
        print("Press 1. to get the number of vertices")
        print("Press 2. to verify if an edge exists")
        print("Press 3. to get the in degree of a vertex")
        print("Press 4. to get the out degree of a vertex")
        print("Press 5. to modify the cost of an edge")
        print("Press 6. to add an edge")
        print("Press 7. to remove an edge")
        print("Press 8. to add a vertex")
        print("Press 9. to remove a vertex")
        print("Press 10. to print the graph (by list in and list out)")
        print("Press 11. to parse in a vertex")
        print("Press 12. to parse out a vertex")
        print("Press 13. to parse the vertices")
        print("Press 14. to print edges")
        print("Press 15. to show the lowest path with BFS")
        
    def getNrVertices(self,graph):
        return graph.getSize()
    
    def isEdge(self, graph, start, end):
        return graph.isEdge(start,end)
    
    def inDegree(self,graph,vertex):
        return graph.inDegree(vertex)
    
    def outDegree(self,graph,vertex):
        return graph.outDegree(vertex)
    
    def modifyCost(self,graph,start,end,newCost):
        graph.modifyCost(start, end, newCost)
    
    def addEdge(self,graph,start,end,cost):
        graph.addEdge(start,end,cost)
    
    def removeEdge(self,graph,start,end):
        graph.removeEdge(start,end)
    
    def addVertex(self,graph):
        graph.addVertex()
    
    def removeVertex(self,graph,vertex):
        graph.removeVertex(vertex)
    
    def printGraph(self,graph):
        return graph.toString()
    
    
    def printIn(self,graph,v):
        it = IteratorIn(graph,v)
        while(it.valid()):
            print(v,"<-",it.getCurrent())
            it.next()
            if len(graph.getListIn()[v]) == 0 and len(graph.getListOut()[v]) == 0:
                print("Isolated")
    
    def printOut(self,graph,v):
        it = IteratorOut(graph,v)
        while(it.valid()):
            print(v,"->",it.getCurrent())
            it.next()
            if len(graph.getListIn()[v]) == 0 and len(graph.getListOut()[v]) == 0:
                print("Isolated")
                
                
    def printVertices(self,graph):
        it = verticesIterator(graph)
        while it.valid():
                print(it.getCurrent())
                it.next()    
                
                
    def printEdges(self,graph):
        print(graph.getEdges())
    
    
    
    
   
        
    
