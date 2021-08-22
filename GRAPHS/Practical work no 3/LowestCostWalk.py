from Domain import *
inf = 20000000000

def mini(x, y):
    if x < y:
        return x
    else:
        return y
    
def checkNegativeCycle(d,n):
    #check if there exists a negative cycle
    for i in range(0,n):
        if d[n*n-1][i]!=d[n*n-2][i]:
            return True
        return False
    
#pt fiecare elem de pe linia n trb sa nu fie < minimul de pe col
def printPath(path,current,stop):
    if path[current] == -1 or path[current] == current:
        print(current,'->')
        return
    
    printPath(path, path[current], stop)
    print(current)
    if current!=stop:
        print('->')
        
        
def lowestCostWalk(graph,start,stop):
    n=graph.getSize()
    #print(n)
    #d=[[inf for x in range((n-1)*(n-1)+1)] for y in range(n)]
    '''
    d=[]  
    for i in range((n-2)*(n-2)+1):
        d.append([])
        for j in range(n):
            d[i].append(inf)
            
    print(d[0][0])
    print(d[6][4])
    '''
    #5/4
    
    d=[]
    for i in range(n+1):
        d.append([])
        
    for i in range(n+1):
        d[0].append(inf)
        
    d[0][start]=0 
    #  print("d[0]:",d[0])
    # print(d[0][1])
    path=[0 for x in range(n)]
    print(d)
    print(path)
    # d[x,k]=the cost of the lowest cost walk from s to x and of length equal to k, where s is the starting vertex.
    
    #print(d[5][0])
    
    
    #for i in range(n):
    #   d[0].append(inf)
    
   
    
    #print(d)
    # print(d[n-1])
    
    for k in range(1,n+1):
        #k=k+1
       
        for x in range(0,n):
            d[k].append(inf)
            print("\n\nk: ",k,"x: ",x,"\n")
            #print("k:",k," x:",x) 
            #print("\n","list in for x:",graph.getListIn()[x],"\n")
            bestFromOutside=inf
            for y in graph.getListIn()[x]:
                print("y:",y)
                if graph.isEdge(y,x):
                    if bestFromOutside>d[k-1][y]+graph.findCost(y,x):
                        bestFromOutside=d[k-1][y]+graph.findCost(y,x)
                        path[x]=y
            if bestFromOutside>d[k-1][x]:
                print("for k, x: path[x]=x",k,x)
                path[x]=x
                #print("best from outside:",bestFromOutside)   
                #  d[k][x]=mini(d[k-1][x],bestFromOutside)
            #print("mini(d[k-1][x],bestFromOutside)",mini(d[k-1][x],bestFromOutside))
            d[k][x]=bestFromOutside
            print(d)
            
    #print(d[0],"\n",d[1],"\n",d[2],"\n",d[3])  
    if checkNegativeCycle(d, n-2):
        print("Negative cycle!")
    
    print("\n",d[0],d[1],d[2],d[3])
    
    if d[(n-2) * (n-2)-1][stop] == inf:
        print("No path from start to stop!")
    #   return
    
    if d[n-1][stop] < 0:
        print("Negative cycle!")
    else: 
        print("the cost is: ",d[n-1][stop])
        print(path)
    
    #print("\n",d)
    
    #print("\n")
    #printPath(path, stop, stop)
    #print("\n")   
    
    