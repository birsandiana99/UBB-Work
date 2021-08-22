from domain.Discipline import Discipline
from domain.Undo import *
from domain.ValidatorException import ValidatorException
#from domain.ValidatorException import ValidatorException
class DisciplineController:
    def __init__(self, validator, repository,undoCrontroller):
        self.__validator = validator
        self.__repository = repository
        self._undoController = undoCrontroller
        
    def add(self, idd, name):
        discipline = Discipline(idd, name)
        try:
            self.__validator.validate(discipline)
        except ValidatorException as ve:
            raise SyntaxError(ve)
        self.__repository.add(discipline)
        
        
        undo = FunctionCall(self.delete,idd)
        redo = FunctionCall(self.add,idd,name)
        oper = Operation(undo,redo)
        self._undoController.addOperation(oper)
        
        return discipline

    def delete(self, idd):
        '''
        redo = FunctionCall(self.delete,idd)
        undo = FunctionCall(self.add,self.__repository.find(idd).getID(),self.__repository.find(idd).getName())
        oper = Operation(undo,redo)
        self._undoController.addOperation(oper)
        '''
        return self.__repository.delete(idd)
        
        
        
        
    def find(self, idd):
        return self.__repository.find(idd)
    
    def search_name(self,name):
        return self.__repository.search_name(name)
       
    def update(self, disciplineID, new_name):
        redo = FunctionCall(self.update,disciplineID,new_name)
        undo = FunctionCall(self.update,disciplineID,self.__repository.find(disciplineID).getName())
        oper = Operation(undo,redo)
        self._undoController.addOperation(oper)
        self.__repository.update(disciplineID,new_name)
        
        self.__repository.update(disciplineID, new_name)
        
    def getDisciplineCount(self):
        return len(self.__repository)
        
    def getAll(self):
        return self.__repository.getAll()
    