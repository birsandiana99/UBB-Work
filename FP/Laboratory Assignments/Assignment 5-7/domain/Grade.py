class Grade():
    def __init__(self, disciplineID, studentID, value):
        '''
        Initiates the Grade class
        Input: disciplineID, studentID, value - integers
        Output: creates an object having the fields discID = disciplineID, studID = studentID, value = value or raises an error 
        '''
        
        try:
            self._discID = int(disciplineID)
            self._studID = int(studentID)
            self._value = int(value)
            if value <= 0 or value >10:
                raise SyntaxError("A student's grade cannot be greater than 10!")
        except ValueError:
            raise SyntaxError("All fields of a grade must be integers!")
        
        
        
    
    def getStudentID(self):
        '''
        Returns the studID field value of an object with the Grade type
        Input: -
        Output: the studID field of the Grade object
        '''
        return self._studID
    
    def getDisciplineID(self):
        '''
        Returns the discID field value of an object with the Grade type
        Input: -
        Output: the discID field of the Grade object
        '''
        return self._discID
    
    def getValue(self):
        '''
        Returns the value field value of an object with the Grade type
        Input: -
        Output: the value field of the Grade object
        '''
        return self._value
    
    def __eq__(self,grade):
        '''
        Verifies if an object from the Grade class is equal to another
        Input: grade - object from the Grade class
        Output: true - if the objects are equal; false - if the objects are not equal   
        '''
        if self._discID==grade.getDisciplineID() and self._studID==grade.getStudentID() and self._value==grade.getValue():
            return True
        return False
    
    def __str__(self):
        '''
        Returns an object in its string form
        Input: -
        Output: The string form of an object in the class
        '''
        return "Discipline ID: "+str(self._discID)+" / "+"Student ID: "+str(self._studID)+" / "+"Grade: "+str(self._value)


def test_grade():
    
    
    grade1 = Grade(1,2,10)
    assert grade1 == Grade(1,2,10)
    
    grade2 = Grade(3,4,9)
    
    try:
        Grade(2,"adasd",3)
        assert False
    except SyntaxError:
        pass
    
    try:
        Grade(3,4,"fsa")
        assert False
    except SyntaxError:
        pass
    
    try:
        Grade("asd",2,3)
        assert False
    except SyntaxError:
        pass
    
test_grade()