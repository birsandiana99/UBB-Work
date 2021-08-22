from Repo.Repository import Repository
from domain.Discipline import Discipline

class DisciplineTextFileRepo(Repository):
    def __init__(self,fileName):
        Repository.__init__(self)
        self._fileName = fileName
        print(self._fileName)
        self._loadFile()
    
    def _saveFile(self):    
        try:
            f = open(self._fileName,"w")
            for c in self.getAll():
                f.write(str(c.getID())+", "+c.getName()+"\n")    
            f.close()    
        except IOError as e:
            raise IOError("Cannot write to file "+str(e))
        finally:
            f.close()
    
        
    def add(self,obj):
        Repository.add(self,obj)
        self._saveFile()
    
        
    
    
    def update(self,objID,new_name):
        Repository.update(self, objID, new_name)
        self._saveFile()
        
    def delete(self,objID):
        Repository.delete(self,objID)
        self._saveFile()
            
    def _loadFile(self):
        try:
            f = open(self._fileName,"r")
            '''
            line = f.readLine()
            while len(line) > 2:
                tok = line.split(",")
                obj = Student(int(tok[0]),tok[1].split())
                Repo.add(self, obj)
                line = f.readLine()
            '''
            for line in f:
                line = line.strip()
                tok = line.split(",")
                obj = Discipline(int(tok[0]),tok[1])
                Repository.add(self, obj)
               
        except IOError as e:
            print(e) 
            raise IOError("Cannot load file")
        finally: 
            f.close()