from domain.Student import Student
from domain.ValidatorException import ValidatorException

class Student_Validator:
    def validate(self, student):
        if type(student) != Student:
            raise TypeError("Not a student!")
        
        _errors = []
        
        if type(student.getID()) != int:
            _errors.append("ID must be an int!")
            
        if len(student.getName()) == 0:
            _errors.append("Empty ~name~ field!")
            
        if type(student.getName()) != str:
            _errors.append("Name must be a string")
        if len(_errors) != 0:
            raise ValidatorException(_errors)