from students import Student

class StudentRepository: #obiect care inauntru contine o lista
    def __init__(self):
        self._l = []
        
    def add(self, student):
        for stud in self._l:
            if stud.getID() == student.getID():
                raise IndexError("There can't be two students with the same id!")
        self._l.append(student)

    def getAll(self):
        return self._l
    
    def remove(self,student):
        i = 0
        while i < len(self._l):
            if self._l[i] == student:
                del self._l[i]
            else:
                i=i+1
    
    def updateID(self,student,idd):
        for stud in self._l:
            if stud.getID() == idd:
                raise IndexError("There can't be two students with the same id!")
        for stud in self._l:
            if stud == student: 
                student.setID(idd)
     
    def updateName(self,student,name):
        for stud in self._l:
            if stud == student:
                student.setName(name)
                
    def initStudents(self):
        self._l.append(Student(1, "Povara Daniel"))
        self._l.append(Student(2, "Racoti Andreea"))
        self._l.append(Student(3, "Pop Alexandra"))
        self._l.append(Student(4, "Glogovetan Anton"))
        self._l.append(Student(5, "Moromete Gabriela"))
        self._l.append(Student(6, "Cantemir Andrei"))
        self._l.append(Student(7, "Calburean Simona"))
        self._l.append(Student(8, "Deac Cosmin"))
        self._l.append(Student(9, "Cretu Alexandru"))
        self._l.append(Student(10, "Zidaru Anca"))  
    
def test_add():
    repo = StudentRepository()
    student = Student(1,"Maria")
    repo.add(student)
    assert len(repo.getAll()) == 1
    assert repo.getAll()[0].getName() == "Maria"
    
def test_getAll():
    repo = StudentRepository()
    student = Student(1,"Maria")
    repo.add(student)
    assert repo.getAll() == [Student(1,"Maria")]
    
    student1 = Student(1,"Anca")
    try:
        repo.add(student1)
        assert False
    except IndexError:
        pass
    
def test_remove():
    repo = StudentRepository()
    student = Student(1,"Maria")
    repo.add(student)
    repo.remove(student)
    assert len(repo.getAll()) == 0

def test_update():
    repo = StudentRepository()
    
    student1 = Student(2,"Anca")
    repo.add(student1)
    
    student2 = Student(1,"Maria")
    repo.add(student2)
    
    repo.updateID(student1, 3)
    assert student1.getID() == 3
    
    try:
        repo.updateID(student1, 1)
        assert False
    except IndexError:
        pass
    
    repo.updateName(student1, "Maruta")
    assert student1.getName() == "Maruta"
    
    
test_add()
test_getAll()
test_remove()
test_update()
    