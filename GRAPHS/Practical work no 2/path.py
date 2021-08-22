from roottree import RootedTree

def bfs(g, startVertex):
    '''Returns the tree corresponding to the BFS from the start vertex
    '''
    queue = [ startVertex ]
    tree = RootedTree(startVertex)
    
    while queue != []:
        currVertex = queue.pop(0)
        children = g.parse_outbound(currVertex)
        for vertex in children:
            if not tree.is_vertex(vertex):
                tree.add_child(currVertex, vertex)
                queue.append(vertex)
    
    return tree
    
def getPath(tree, endVertex):
    ''' Returns the list of vertices from the root of a tree to the `targetVertex` 
        Returns None if the targetVertex is not in the tree
    '''
    if not tree.is_vertex(endVertex):
        return None
    startVertex = tree.get_root()
    path = [ ]
    #currVertex = targetVertex
    while endVertex != startVertex:
        path.append(endVertex)
        parent = tree.get_parent(endVertex)
        endVertex = parent
    
    path.reverse()
    
    return path

