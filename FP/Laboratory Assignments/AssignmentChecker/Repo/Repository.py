class Repository:
    def __init__(self):
        self._objects = []
        
    def add(self,obj):
        for ob in self._objects:
            if ob.getID() == obj.getID():
                raise IndexError("There can't be two students with the same id!") 
        self._objects.append(obj)
    
    def getAll(self):
        return self._objects
    
    def __len__(self):
        return len(self._objects)
    