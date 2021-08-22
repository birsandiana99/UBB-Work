from Repo.GradeRepository import GradeRepository
import pickle

class GradePickleRepo(GradeRepository):
    def __init__(self,fileName):
        GradeRepository.__init__(self)
        self._fileName = fileName
        print(self._fileName)
        self._loadFile()
    
    def _saveFile(self):    
        f = open(self._fileName,"wb")
        pickle.dump(self.getAll(),f)
        f.close()
    
        
    def add(self,obj):
        GradeRepository.add(self,obj)
        self._saveFile()
    
            
    def _loadFile(self):
        try:
            f = open(self._fileName,"rb")
            lst = pickle.load(f)
            print(lst)
            self._l = lst
        except IOError as e:
            print(e) 
            raise IOError("Cannot load file")
        finally: 
            f.close()