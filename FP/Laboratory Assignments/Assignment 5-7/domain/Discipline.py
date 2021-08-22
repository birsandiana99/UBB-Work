class Discipline():
    def __init__(self, disciplineID, name):
        '''
        Initiates the Discipline class
        Input: disciplineID - an integer , name - a string
        Output: creates an object having the fields id = disciplineID, name = name or raises an error 
        '''
        
        try:
            '''
            for discipline in discList:
                if discipline._id==disciplineID:
                    raise AttributeError("There already exists a discipline with that id")
            '''
            self._id = int(disciplineID)
        except ValueError:
            raise SyntaxError("A discipline's id cannot be a string!")
        
        if type(name)!=str:
            raise SyntaxError("A discipline's name has to be a string!")
        
        self._name = name
    
    def getID(self):
        '''
        Returns the id field value of an object with the Discipline type
        Input: -
        Output: the id field of the Discipline object
        '''
        return self._id
    
    def getName(self):
        '''
        Returns the name field value of an object with the Discipline type
        Input: -
        Output: the name field of the Discipline object
        '''
        return self._name
    
    def setID(self,idd):
        '''
        Sets the id of an object from the Student class to a given value
        Input: idd - an integer
        Output: modifies the id field of the object to idd
        '''
        self._id = idd
        
    def setName(self,name):
        '''
        Sets the name of an object from the Student class to a given value
        Input: name - a string
        Output: modifies the name field of the object to name
        '''
        self._name = name    
        
    def __eq__(self, o):
        '''
        Verifies if an object from the Discipline class is equal to another
        Input: grade - object from the Discipline class
        Output: true - if the objects are equal; false - if the objects are not equal   
        '''
        if self._name == o.getName() and self._id == o.getID():
            return True
        return False
        
    def __str__(self):
        '''
        Returns an object in its string form
        Input: -
        Output: The string form of an object in the class
        '''
        return "ID: "+str(self._id)+" / "+"Name: "+str(self._name)
    
    
def test_discipline():
    disc1 = Discipline(23,"Geometrie")
    disc2 = Discipline(12,"Matematica analitica")
    disc3 = Discipline(67,"Romana")
    
    try:
        Discipline("asde","Geometrie")
        assert False
    except SyntaxError:
        pass
    
    
    disc1 = Discipline(23,"Geometrie")
    disc2 = Discipline(12,"Matematica analitica")
    disc3 = Discipline(67,"Romana")
    
    try:
        Discipline("asde","Geometrie")
        assert False
    except SyntaxError:
        pass
    
    assert disc1.getID() == 23
    disc1.getName == "Geometrie"
    
    assert disc1 == Discipline(23,"Geometrie")
    
    
    
    assert str(disc1) == "ID: 23 / Name: Geometrie"

    disc1.setName("FSJ")
    assert disc1.getName() == "FSJ"
    
    
test_discipline()
    
    