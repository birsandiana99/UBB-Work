from Domain import Graph
from UI import *
from LowestCostWalk import *
#from path import *
def readFile(fileName):
    with open(fileName, 'r') as f:
            line = f.readline().split()
            #print(line)
            n = int(line[0]) # vertices
            #m = int(line[1]) # edges
            graph = Graph(n)
 
       
            #print(f.readlines())
            for line in f.readlines():
                line = line.split()
                graph.addEdge(int(line[0]), int(line[1]),int(line[2]))
 
            return graph
 
    return False



def main():
    ui = UI()
    
    #print("Enter the size of the graph")
    '''graph = Graph(5)
    
    graph.addEdge(1, 2, 3)
    graph.addEdge(2, 3, 7)
    graph.addEdge(4, 2, 8)
    graph.addEdge(2, 1, 9)
    graph.addEdge(4, 1, 3)
    '''
    #print(graph.getSize())
    #ui.printMenu()
    
    command = -1
    
    graph = readFile("file.txt")
    #print(ui.printGraph(graph))
    #g1 = graph.copyGraph()
    #print(ui.printGraph(g1))
     
    lowestCostWalk(graph, 0, 3)
    
    
    ''' 
    while command != 0:
        print("Enter a command...")
        command = int(input()) 
        if command == 1:
            print(ui.getNrVertices(graph))
        elif command == 2:
            print("Start edge: ")
            start = int(input())
            
            print("End edge: ")
            end = int(input())
            
            if ui.isEdge(graph,start,end) == 1:
                print("It exists!")
            else:
                print("It doesn't exist!")
            
        elif command == 3:
            print("Give the vertex: ")
            vertex = int(input())
            print("The in degree is: ",ui.inDegree(graph,vertex))
        elif command == 4:
            print("Give the vertex: ")
            vertex = int(input())
            print("The out degree is: ",ui.outDegree(graph, vertex))
        elif command == 5:
            print("Start edge: ")
            start = int(input())
            
            print("End edge: ")
            end = int(input())
            
            print("New cost: ")
            newCost = int(input())
            ui.modifyCost(graph,start,end,newCost)
            
            print(graph._edges[(start,end)])
                
        elif command == 6:
            print("Start edge: ")
            start = int(input())
            
            print("End edge: ")
            end = int(input())
            
            print("Cost: ")
            cost = int(input())
            ui.addEdge(graph,start,end,cost)
            
        elif command == 7:
            print("Start edge: ")
            start = int(input())
            
            print("End edge: ")
            end = int(input())
            ui.removeEdge(graph,start,end)
            
        elif command == 8:
            ui.addVertex(graph) 
            
        elif command == 9:
            print("Give the vertex: ")
            vertex = int(input())
            ui.removeVertex(graph,vertex)
        elif command == 10:
            print(ui.printGraph(graph)) 
        elif command == 11:
            print("Give the vertex: ")
            vertex = int(input())
            ui.printIn(graph, vertex) 
        elif command == 12:
            print("Give the vertex: ")
            vertex = int(input())
            ui.printOut(graph, vertex) 
        elif command == 13:
            ui.printVertices(graph)
        elif command == 14:
            ui.printEdges(graph)
        elif command == 15:
            #start =int(input("start: "))
            #end = int(input("end: "))
            
            print(graph.bfs(1, 4))
            #g = graph.createDemoGraph()
            #tree = bfs(g, 2)
            #tree.printTree()
            #print (getPath(tree, 2))
        else:
            if command != 0:
                print("Invalid command!!")
        
    '''    
main()
      
    