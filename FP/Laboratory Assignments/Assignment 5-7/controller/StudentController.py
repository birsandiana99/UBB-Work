from domain.Student import Student
from domain.Undo import *
from domain.ValidatorException import ValidatorException
class StudentController:
    def __init__(self, validator, repository,undoController):
        self.__validator = validator
        self.__repository = repository
        self._undoController = undoController
        
    def add(self, idd, name):
        try: 
            self.__validator.validate(Student(idd,name))
        except ValidatorException as ve:
            raise SyntaxError(ve)
        
        
        student = Student(idd, name)
        self.__validator.validate(student)
        self.__repository.add(student)
        
        undo = FunctionCall(self.delete,idd)
        redo = FunctionCall(self.add,idd,name)
        oper = Operation(undo,redo)
        self._undoController.addOperation(oper)
        return student
       

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
          
    def update(self, studentID,new_name):
        redo = FunctionCall(self.update,studentID,new_name)
        undo = FunctionCall(self.update,studentID,self.__repository.find(studentID).getName())
        oper = Operation(undo,redo)
        self._undoController.addOperation(oper)
        self.__repository.update(studentID,new_name)
        
    def getRepoCount(self):
        return len(self.__repository)
    
    def getAll(self):
        return self.__repository.getAll()
        
    
        
            
        