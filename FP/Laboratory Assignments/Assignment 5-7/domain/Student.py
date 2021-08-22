class Student():
    def __init__(self, studentId, name):
        '''
        Initiates the Student class
        Input: studentId - an integer , name - a string
        Output: creates an object having the fields id = studentId, name = name or raises an error 
        '''
        
        '''
        try:
            self._id = int(studentId)
        except ValueError:
            raise SyntaxError("A student's id cannot be a string!")
        
        if type(name)!=str:
            raise SyntaxError("A student name has to be a string!")
        self._name = name
        '''
        
        self._name = name
        self._id = int(studentId)
        
    
    def getID(self):
        '''
        Returns the id field value of an object with the Student type
        Input: -
        Output: the id field of the Student object
        '''
        return self._id
    
    def getName(self):
        '''
        Returns the name field value of an object with the Student type
        Input: -
        Output: the name field of the Student object
        '''
        return self._name
    
    def __eq__(self, o):
        '''
        Verifies if an object from the Student class is equal to another
        Input: grade - object from the Student class
        Output: true - if the objects are equal; false - if the objects are not equal   
        '''
        if self._name == o.getName() and self._id == o.getID():
            return True
        return False
    
    def setID(self, idd):
        '''
        Sets the id of an object from the Student class to a given value
        Input: idd - an integer
        Output: modifies the id field of the object to idd
        '''
        self._id = idd
    
    def setName(self, name):
        '''
        Sets the name of an object from the Student class to a given value
        Input: name - a string
        Output: modifies the name field of the object to name
        '''
        self._name = name              
        
    def __str__(self):
        '''
        Returns an object in its string form
        Input: -
        Output: The string form of an object in the class
        '''
        return "ID: "+str(self._id)+" / "+"Name: "+str(self._name)


