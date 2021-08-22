from Repo.Repository import Repository
import pickle

class PickleRepo(Repository):
    def __init__(self,fileName):
        Repository.__init__(self)
        self._fileName = fileName
        print(self._fileName)
        self._loadFile()
    
    def _saveFile(self):    
        f = open(self._fileName,"wb")
        pickle.dump(self.getAll(),f)
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
            f = open(self._fileName,"rb")
            lst = pickle.load(f)
            self._objects = lst
        except IOError as e:
            print(e) 
            raise IOError("Cannot load file")
        finally: 
            f.close()