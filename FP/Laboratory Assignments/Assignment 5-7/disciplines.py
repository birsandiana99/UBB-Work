from grades import Grade

class Discipline():
    def __init__(self, disciplineID, name):
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
        return self._id
    
    def getName(self):
        return self._name
    
    def setID(self,idd):
        self._id = idd
        
    def setName(self,name):
        self._name = name    
        
    def __eq__(self, o):
        if self._name == o.getName() and self._id == o.getID():
            return True
        return False
        
    def __str__(self):
        return "ID: "+str(self._id)+" / "+"Name: "+str(self._name)
    
    def initDisciplines(self,discList):
        Discipline(1, "Algebra").add(discList)
        Discipline(2, "Informatica").add(discList)
        Discipline(3, "Geografie").add(discList)
        Discipline(4, "Istorie").add(discList)
        Discipline(5, "Literatura").add(discList)
        Discipline(6, "Gramatica").add(discList)
        Discipline(7, "Teoria muzicii").add(discList)
        Discipline(8, "Logica computationala").add(discList)
        Discipline(9, "Analiza").add(discList)
        Discipline(10, "Geometrie").add(discList)
    

def test_disciplines():
    disc1 = Discipline(23,"Geometrie")
    disc2 = Discipline(12,"Matematica analitica")
    disc3 = Discipline(67,"Romana")
    
    try:
        Discipline("asde","Geometrie")
        assert False
    except SyntaxError:
        pass
    
    
    discList=[]
    discList.append(disc1)
    discList.append(disc2)
    disc3.add(discList)
    assert disc3 in discList
    disc2.remove(12,discList)
    assert disc2 not in discList 
    
    #disc1.updateID(23)
    assert disc1.getID() == 23
    disc1.updateName("Analiza")
    
    assert disc1 == Discipline(23,"Analiza")
    
    assert str(disc1) == "ID: 23 / Name: Analiza"
    
    try:
        Discipline(67,"fsdfs").add(discList)
        assert False
    except IndexError:
        pass
    
    disc4=Discipline(11,"disc1")
    disc4.add(discList)
    gradesList=[Grade(1,11,9),Grade(2,4,3),Grade(8,7,5)]
    disc4.remove(11,discList, gradesList)
    assert Grade(1,11,9) not in gradesList
    
#test_students()