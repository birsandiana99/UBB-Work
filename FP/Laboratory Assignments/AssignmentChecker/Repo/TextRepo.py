from Repo.Repository import Repository
from Domain.Assignment import Assignment
class TextFilesRepo(Repository):
    def __init__(self,name):
        print(name)
        self._fileName = name
        Repository.__init__(self)
        self._loadFile()
        
        
    def _loadFile(self):
       
        f = open(self._fileName)
        text = f.read()
        lines = text.split("\n")
        for line in lines:
            tok = line.split(",")
            Repository.add(self, Assignment(int(tok[0]),tok[1],tok[2]))
        f.close()
        
    def __len__(self):
        return Repository.__len__(self)
    
    '''
    def add(self,obj):
        self.add(obj)
    '''