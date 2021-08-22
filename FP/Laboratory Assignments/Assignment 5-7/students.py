'''

A faculty stores information about:
 Student: <studentID>, <name>.
 Student: <Student>, <name>.
 Grade: <Student>, <studentID>, <grade_value>.
Create an application which allows to:
1. Manage the list of students and available disciplines. The application must allow the user to add, remove, update, and list both students and disciplines.
2. Grade students at a given discipline. Any student may receive one or several grades at any of the disciplines. Deleting a student also removes their grades. 
Deleting a discipline deletes all grades at that discipline for all students.


'''
from grades import Grade

class Student():
    def __init__(self, studentId, name):
        try:
            self._id = int(studentId)
        except ValueError:
            raise SyntaxError("A student's id cannot be a string!")
        
        if type(name)!=str:
            raise SyntaxError("A student name has to be a string!")
        
        self._name = name
    
    def getID(self):
        return self._id
    
    def getName(self):
        return self._name
    
   
    def __eq__(self, o):
        if self._name == o.getName() and self._id == o.getID():
            return True
        return False
    
    
    def add(self, studList):
        ok=0
        for stud in studList:
            if stud.getID()==self._id:
                ok=1
                raise IndexError("There is already a student with this name")
        if ok==0:
            studList.append(self)
     
    def remove(self, idd, studList, gradesList=[]):
        #if self == 0:
        i = 0
        while i < len(studList):
            if studList[i].getID() == idd:
                del studList[i]
            else:
                i=i+1
        
        i = 0
        while i < len(gradesList):
            if idd == gradesList[i].getStudentID():
                del gradesList[i]
            else:
                i=i+1
        '''
        elif idd == 0: 
            i = 0
            while i < len(studList):
                if studList[i] == self:
                    del studList[i]
                else:
                    i=i+1
            
            i = 0
            while i < len(gradesList):
                if self._id == gradesList[i].getStudentID():
                    del gradesList[i]
                else:
                    i=i+1
        '''
      
    '''            
    def updateID(self,id1):
        self._id=id1
    '''
    def setID(self, idd):
        self._id = idd
    
    def setName(self, name):
        self._name = name 
    
                        
    
        
    def __str__(self):
        return "ID: "+str(self._id)+" / "+"Name: "+str(self._name)
    

def test_students():
    student1 = Student(23,"Pop Daniel")
    student2=Student(12,"Boeriu Maria")
    student3=Student(67,"Mihaiu Elena")
    
    try:
        Student("asde","Pop Daniel")
        assert False
    except SyntaxError:
        pass
    
    
    studList=[]
    studList.append(student1)
    studList.append(student2)
    student3.add(studList)
    assert student3 in studList
    student2.remove(student2.getID(), studList)
    assert student2 not in studList 
    
    #student1.updateID(23)
    assert student1.getID() == 23
    student1.updateName("Papara")
    
    assert student1 == Student(23,"Papara")
    
    assert str(student1) == "ID: 23 / Name: Papara"
    try:
        Student(67,"fsdfs").add(studList)
        assert False
    except IndexError:
        pass
    
    stud99=Student(1,"Andreea")
    stud99.add(studList)
    gradesList=[Grade(21,1,9),Grade(2,4,3),Grade(8,7,5)]
    stud99.remove(1,studList, gradesList)
    assert Grade(21,1,9) not in gradesList
    
#test_students()
