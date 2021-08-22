from disciplines import Discipline

class DisciplineRepository: #obiect care inauntru contine o lista
    def __init__(self):
        self._l = []
        
    def add(self, discipline):
        for disc in self._l:
            if disc.getID() == discipline.getID():
                raise IndexError("There can't be two students with the same id!")
        self._l.append(discipline)

    def getAll(self):
        return self._l
    
    def remove(self,discipline):
        i = 0
        while i < len(self._l):
            if self._l[i] == discipline:
                del self._l[i]
            else:
                i=i+1
    
    def updateID(self,discipline,idd):
        for disc in self._l:
            if disc.getID() == idd:
                raise IndexError("There can't be two students with the same id!")
        for disc in self._l:
            if disc == discipline: 
                discipline.setID(idd)
     
    def updateName(self,discipline,name):
        for disc in self._l:
            if disc == discipline:
                discipline.setName(name)
                
    def initStudents(self):
        self._l.append(Discipline(1, "Algebra"))
        self._l.append(Discipline(2, "Informatica"))
        self._l.append(Discipline(3, "Geografie"))
        self._l.append(Discipline(4, "Istorie"))
        self._l.append(Discipline(5, "Literatura"))
        self._l.append(Discipline(6, "Gramatica"))
        self._l.append(Discipline(7, "Teoria muzicii"))
        self._l.append(Discipline(8, "Logica computationala"))
        self._l.append(Discipline(9, "Analiza"))
        self._l.append(Discipline(10, "Geometrie"))
    
def test_add():
    repo = DisciplineRepository()
    discipline = Discipline(1,"Maria")
    repo.add(discipline)
    assert len(repo.getAll()) == 1
    assert repo.getAll()[0].getName() == "Maria"
    
def test_getAll():
    repo = DisciplineRepository()
    discipline = Discipline(1,"Maria")
    repo.add(discipline)
    assert repo.getAll() == [Discipline(1,"Maria")]
    
    discipline1 = Discipline(1,"Anca")
    try:
        repo.add(discipline1)
        assert False
    except IndexError:
        pass
    
def test_remove():
    repo = DisciplineRepository()
    discipline = Discipline(1,"Maria")
    repo.add(discipline)
    repo.remove(discipline)
    assert len(repo.getAll()) == 0

def test_update():
    repo = DisciplineRepository()
    
    discipline1 = Discipline(2,"Anca")
    repo.add(discipline1)
    
    discipline2 = Discipline(1,"Maria")
    repo.add(discipline2)
    
    repo.updateID(discipline1, 3)
    assert discipline1.getID() == 3
    
    try:
        repo.updateID(discipline1, 1)
        assert False
    except IndexError:
        pass
    
    repo.updateName(discipline1, "Maruta")
    assert discipline1.getName() == "Maruta"
    
    
test_add()
test_getAll()
test_remove()
test_update()
    