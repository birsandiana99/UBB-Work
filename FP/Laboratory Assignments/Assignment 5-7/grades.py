class Grade():
    def __init__(self, disciplineID, studentID, value):
        try:
            self._discID = int(disciplineID)
            self._studID = int(studentID)
            self._value = int(value)
        except ValueError:
            raise SyntaxError("All fields of a grade must be integers!")
    
    def getStudentID(self):
        return self._studID
    
    def getDisciplineID(self):
        return self._discID
    
    def getValue(self):
        return self._value

    def add(self,gradesList):
        gradesList.append(self)
        
    def remove(self,gradesList):
        i = 0
        while i < len(gradesList):
            if gradesList[i] == self:
                del gradesList[i]
            else:
                i=i+1
    
    def __eq__(self,grade):
        if self._discID==grade.getStudentID() and self._studID==grade.getDisciplineID() and self._value==grade.getValue():
            return True
        return False
    
    def __str__(self):
        return "Student ID: "+str(self._studID)+" / "+"Discipline ID: "+str(self._discID)+" / "+"Grade: "+str(self._value)
    
    def initGrades(self,gradesList):
        Grade(1,2,10).add(gradesList)
        Grade(2,1,3).add(gradesList)
        Grade(3,4,9).add(gradesList)
        Grade(4,3,6).add(gradesList)
        Grade(5,2,7).add(gradesList)
        Grade(6,2,5).add(gradesList)
        Grade(7,1,2).add(gradesList)
        Grade(8,8,10).add(gradesList)
        Grade(9,7,10).add(gradesList)
        Grade(10,5,10).add(gradesList)
        

def test_grades():
    gradesList=[]
    
    grade1 = Grade(1,2,10)
    assert grade1 == Grade(1,2,10)
    
    grade2 = Grade(3,4,9).add(gradesList)
    assert Grade(3,4,9) in gradesList
    
    grade1.add(gradesList)
    grade1.remove(gradesList)
    assert grade1 not in gradesList
    
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
    