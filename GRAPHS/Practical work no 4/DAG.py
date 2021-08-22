from Domain import *
def TopoSortDFS(graph,x,listsorted,fullyProcessed,inProcess):
    inProcess.add(x)
    for y in graph.getListIn()[x]:
        if y in inProcess:
            return False
        elif y not in fullyProcessed:
                ok = TopoSortDFS(graph, y, listsorted, fullyProcessed, inProcess)
                if not ok:
                    return False
    
    inProcess.remove(x)
    if x not in listsorted:
        listsorted.append(x)
    
    #print("x:",x,"   listsorted: ",listsorted)
    fullyProcessed.add(x)
    return True

def maxi(x,y):
    if x>y:
        return x
    else:
        return y
    
def timeForVertex(graph,toposort):
    #ET
    print(toposort)
    et={}
    et[toposort[0]]=0
    
    
    #print(type(et))
    
    '''
    for i in range(1,graph.getSize()):
        maximum=0
        print("i is now: ",i)
        for y in graph.getListIn()[i]:
            #print("y is now: ",y)
            #print("toposort y is: ",et[toposort[y]])
            if et[toposort[i-1]]+graph.findCost(y,i)>=maximum:
                maximum=et[toposort[i-1]]+graph.findCost(y,i)
        #print(maximum)
        et[toposort[i]]=maximum


    print(et)
    '''
    for i in range(1,len(toposort)):
        maximum=0
        x=toposort[i]
        #print("x is now: ",x)
        for y in graph.getListIn()[x]:
            #print("y:",y)
            if et[y]+graph.findCost(y,x)>=maximum:
                maximum=et[y]+graph.findCost(y,x)
        #print(maximum)
        et[x]=maximum
    
    
    
    print(et)
    print("\n\n\n")
    lt = {}
    lt[toposort[len(toposort)-1]]=et[toposort[len(toposort)-1]]
    print(lt)
    
    for i in range(len(toposort)-2,-1,-1):
        print(i)
        minimum=999999
        x=toposort[i]
        print("x is now: ",x)
        for y in graph.getListOut()[x]:
            print("y:",y)
            print("Lt for y",lt[y])
            print("et for y",et[y])
            if lt[y]-graph.findCost(x,y)<=minimum:
                minimum=lt[y]-graph.findCost(x,y)
                #print(minimum)
        #print(maximum)
        lt[x]=minimum
    
        
    print(lt)    
    
    return((et,lt))
    
'''
def iterative_topological_sort(graph, start):
    seen = set()
    stack = []    # path variable is gone, stack and order are new
    order = []    # order will be in reverse order at first
    q = [start]
    while q:
        v = q.pop()
        if v not in seen:
            seen.add(v) # no need to append to path any more
            q.extend(graph[v])

            while stack and v not in graph[stack[-1]]: # new stuff here!
                order.append(stack.pop())
            stack.append(v)

    return stack + order[::-1]   # new return value!


def recursive_topological_sort(graph, node):
    result = []
    seen = set()

    def recursive_helper(node):
        for neighbor in graph.getListIn()[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                recursive_helper(neighbor)
        result.insert(0, node)              # this line replaces the result.append line

    recursive_helper(node)
    return result
    
'''    
    
