from Repo.GradeRepository import GradeRepository
from domain.Grade import Grade

class GradesTextFileRepo(GradeRepository):
    def __init__(self,fileName):
        GradeRepository.__init__(self)
        self._fileName = fileName
        print(self._fileName)
        self._loadFile()
    
    def _saveFile(self):    
        try:
            f = open(self._fileName,"w")
            for c in self.getAll():
                f.write(str(c.getDisciplineID())+","+str(c.getStudentID())+","+str(c.getValue())+"\n")    
            f.close()    
        except IOError as e:
            raise IOError("Cannot write to file "+str(e))
        finally:
            f.close()
    
        
    def add(self,obj):
        GradeRepository.add(self,obj)
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
                obj = Grade(int(tok[0]),int(tok[1]),int(tok[2]))
                GradeRepository.add(self, obj)
               
        except IOError as e:
            print(e) 
            raise IOError("Cannot load file")
        finally: 
            f.close()