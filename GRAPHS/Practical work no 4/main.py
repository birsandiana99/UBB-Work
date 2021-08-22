from Domain import Graph
from DAG import *


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
    
   
    listsorted = []
    fullyProcess = set()
    #print(type(fullyProcess))
    inProcess = set()
    for x in range(0,graph.getSize()):
        ok = TopoSortDFS(graph,x,listsorted,fullyProcess,inProcess)
        if not ok:
            listsorted.clear() 
            print("Not a dag")
            return
    print(listsorted)
    
    print(graph.getSize())
    tupleOfDicts = timeForVertex(graph,listsorted)
    
    et = tupleOfDicts[0]
    lt = tupleOfDicts[1]
    criticalPoints = []
    for i in range(0,graph.getSize()):
        if(et[i]==lt[i]):
            criticalPoints.append(i)
            
    print("The critical points are: ",criticalPoints)
    
    '''
    ls=[]
    for x in range(0,graph.getSize()):
        ls[x].append(recursive_topological_sort(graph,x))
        print(ls)
        if ls[x][0]==ls[x][len(ls)-1] and len(ls[x])>1:
            print("Not a dag")
            return
    
    for x in range(0,graph.getSize()):
        min=999
        max=0
        for y in range(0,len(ls[x])):
            if()
    '''
     
   
main()
      
    