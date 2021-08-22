class RootedTree:
    def __init__(self, root):
        self.__root = root
        self.__children = {root:[]}
        self.__parent = {root:None}
        
    def add_child(self, vertex, new_vertex):
        #adds new_vertex as child of vertex
        #precondition: vertex exists, new_vertex does not
        self.__children[vertex].append(new_vertex)
        self.__children[new_vertex] = []
        self.__parent[new_vertex] = vertex
        
    def get_children(self, vertex):
        #returns a generator that enumerates the children of a given vertex
        #precondition: vertex exists
        return self.__children[vertex][:]
        
    def is_vertex(self, vertex):
        #returns True or False, depending on the existence of the vertex
        return vertex in self.__children.keys()
        
    def get_parent(self, vertex):
        #returns the parent vertex of the given vertex
        #if the vertex is the root of the graph, return None
        return self.__parent[vertex]
        
    def get_root(self):
        #returns the root of the graph
        return self.__root
        
    def printSubTree(self, root, spaces):
        print (" " * spaces,root)
        for child in self.__children[root]:
            self.printSubTree(child, spaces + 1)
            
        
    def printTree(self):
        self.printSubTree(self.__root, 0)