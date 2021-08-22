from disciplines import Discipline
from students import Student
from grades import Grade 

class GradeRepository:
    def __init__(self):
        self._l = []
        self._index = 0
        
    def add(self,grade):    
        self._l.append(grade)
                
    def removeByDisciplineID(self,idd):
        i = 0
        while i < len(self._l):
            if self._l[i].getDisciplineID() == idd:
                del self._l[i]
            else:
                i=i+1
    
    def getAll(self):
        return self._l
    
    def search_stud(self, idd):
        list = []
        for grade in self._l:
            if idd == grade.getStudentID():
                list.append(idd)
        return list        
        
    
            
    def removeByStudentID(self,idd):
        i = 0
        while i < len(self._l):
            if self._l[i].getStudentID() == idd:
                del self._l[i]
            else:
                i=i+1
                
    def __len__(self):
        return len(self._l)
         
    '''
    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        #print(len(self._objects))
        n = self._index
        self._index = self._index + 1
        
        if n >= len(self._l):
            #print("da")
            raise StopIteration
        return self._l[n]
    '''      
          
                
def test_grade_repo():
    l=GradeRepository()
    l.add(Grade(1,10,10))
    l.add(Grade(1,10,8))
    l.add(Grade(1,10,7))
    l.add(Grade(1,1,10))
    l.add(Grade(1,2,8))
    l.add(Grade(2,1,5))
    l.add(Grade(3,9,4))
    l.add(Grade(4,8,1))
    l.add(Grade(5,7,3))
    l.add(Grade(6,6,2))
    l.add(Grade(7,5,7))
    l.add(Grade(8,4,10))
    l.add(Grade(9,3,9))
    l.add(Grade(10,2,8))
    l.add(Grade(4,3,1))
    l.add(Grade(4,3,5))
    l.add(Grade(7,3,1))
    l.add(Grade(10,2,1))
    
    assert len(l.getAll()) == 18
    l.removeByDisciplineID(1)
    assert len(l.getAll()) == 13
    l.removeByStudentID(3)
    assert len(l.getAll()) == 9
    
    
test_grade_repo()
    