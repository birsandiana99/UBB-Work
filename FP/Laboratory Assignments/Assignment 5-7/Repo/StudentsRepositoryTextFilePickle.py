from Repository.Repository import Repository
import pickle 
class StudentsTextFilePickleRepo(Repository):
    def __init__(self,fileName):
        Repository.__init__(self)
        self._fileName = fileName
        self._loadFile()
        
    
    def add(self,obj):
        Repository.add(self,obj)
        self._saveFile()
        
    def _saveFile(self):    
        try:
            f = open(self._fileName,"wb")
            for c in self.getAll():
                pickle.dump(c,f)
            f.close()    
        except IOError as e:
            raise IOError("Cannot write to file "+str(e))
        finally:
            f.close()
    
    
    def _loadFile(self):
        try:
        
            f = open(self._fileName,"r")
            line = f.readLine()
            while len(line) > 2:
                obj = pickle.load(line)
                Repository.add(self, obj)
                line = f.readLine()
        except IOError as e:
            raise IOError("Cannot load file")
        finally: 
            f.close()
