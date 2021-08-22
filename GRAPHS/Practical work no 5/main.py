from Domain import Graph



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
    #ui = UI()
    
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

    
    graph = readFile("file.txt")
    #print(ui.printGraph(graph))
    #g1 = graph.copyGraph()
    #print(ui.printGraph(g1))
    
    graph.BellmanFord(0,3)
    
    print(graph.bellman(0,3))
   
main()
      
    