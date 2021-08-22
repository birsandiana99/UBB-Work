from domain.Student import Student
from domain.Discipline import Discipline
from Iterable.Iterable_class import Iter
class Repository():
    def __init__(self):
        '''
        Creates a list
        Input: -
        Output: creates a void list
        '''
        #self._objects = Iter()
        self._objects = []
        

    def add(self, obj):
        '''
        Adds an object to the repository
        Input: obj - an object having the fields ID and name
        Output- adds the object to the list or raises an error
        '''
        
        '''
        for ob in self._objects:
            if ob.getID() == obj.getID():
                raise IndexError("There can't be two objects with the same id!")
                
        '''
        if self.find(obj.getID()):
            raise IndexError("There can't be two objects with the same id!")
        self._objects.append(obj)

    def update(self, objectID,new_name):
        '''
        Updates the name of an object in a list
        Input: object_id - an integer,  new_name - a string
        Output: modifies the field 'name' of the objects to the value of the string new_name
        '''
        
        obj = self.find(objectID)
        obj.setName(new_name)

    def find(self, objectID):
        '''
        Finds an object in a list by its "ID" field
        Input: objectID - an integer
        Output: Returns the objects from the list having the ID field equal to objectID
                If there is no item with this property, it returns None
        '''
        for o in self._objects:
            if o.getID() == objectID:
                return o
        return 

    def delete(self, objectID):
        '''
        Deletes an object from a list by its ID field value
        Input: objectID - an integer
        Output: deletes the object having the value of the ID field equal to objectID
        '''
        i = 0
        while i < len(self._objects):
            if self._objects[i].getID() == objectID:
                del self._objects[i]
            else:
                i=i+1
        
        

    
    
    def search_name(self,name):
        '''
        Searches an object in a list by its 'name' field
        Input: name - a string
        Output: searches the object having the 'name' field equal to the variable name
        '''
        l = []
        if len(name) == 1:
            for o in self._objects:
                if name in o.getName().lower():
                    l.append(o)
            return l
        
        else:
            for o in self._objects:
                obj_name = (o.getName()).lower()
                import re
                #m = re.search(obj_name, name)
                result = re.match(obj_name, name)
                if result != None:
                    return o 
            
            
        
    def getAll(self):
        '''
        Returns the whole list of the Repo class
        Input: -
        Output: returns a list of objects
        '''
        return self._objects

    def __len__(self):
        '''
        Returns the length of a list of objects
        Input: -
        Output: returns the length of a list of objects
        '''
        return len(self._objects)

    def __str__(self):
        '''
        Returns a list of objects in string form
        Input: -
        Output: returns a list of objects in their string form
        '''
        r = ""
        for e in self._objects:
            r += str(e)
            r += "\n"
        return r
    '''
    def __iter__(self):
        for obj in self._objects:
            yield obj
    '''
    
    '''
    def __next__(self):
        num = self.num
        self.num += 1
        if num < len(self._objects):
            return self._objects[num]
        else:
            StopIteration
    '''
    '''
    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        #print(len(self._objects))
        n = self._index
        self._index = self._index + 1
        
        if n >= len(self._objects):
            #print("da")
            raise StopIteration
        return self._objects[n]
    '''        
    
'''
def test_repo():
    l = Repo()
    l.add(Student(1, "Povara Daniel"))
    l.add(Student(2, "Racoti Andreea"))
    l.add(Student(3, "Pop Alexandra"))
    l.add(Student(4, "Glogovetan Anton"))
    l.add(Student(5, "Moromete Gabriela"))
    l.add(Student(6, "Cantemir Andrei"))
    l.add(Student(7, "Calburean Simona"))
    l.add(Student(8, "Deac Cosmin"))
    l.add(Student(9, "Cretu Alexandru"))
    l.add(Student(10, "Zidaru Anca")) 
    assert len(l) == 10
    assert l.find(1) == Student(1,"Povara Daniel")
    l.update(1,"FSJ")
    assert l.find(1) == Student(1,"FSJ")
    l.delete(1)
    assert len(l) == 9
    assert l.find(1) == None
    try:
        l.add(Student(2,"Silvia"))
        assert False
    except IndexError:
        pass

test_repo()
'''

    