class Assignment:
    def __init__(self, idd, stud_name, solution):
        
        if len(stud_name) < 3:
            raise SyntaxError("Student name must contain at least 3 characters!")
        self._id = idd
        self._name = stud_name
        self._solution = solution
        
    def getSolution(self):
        return self._solution
    
    def getID(self):
        return self._id
    
    def getName(self):
        return self._name
    
    def __str__(self):
        return "ID: "+str(self._id)+"  Name: "+ self._name+ "  Solution: "+self._solution