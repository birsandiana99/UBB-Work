from domain.Grade import Grade
from domain.ValidatorException import ValidatorException

class Grade_Validator:
    def validate(self, grade):
        if type(grade) != Grade:
            raise TypeError("Not a student!")
        
        _errors = []

        if type(grade.getStudentID) != int or grade.getStudentID() < 0:
            _errors.append("Student ID must be an int bigger than 0!")
            
        if type(grade.getDisciplineID()) != int or grade.getDisciplineID() < 0:
            _errors.append("Discipline ID must be an int bigger than 0!")
            
        if type(grade.getValue()) != int or grade.getValue()not in (1,10):
            _errors.append("Value must be an integer between 1 and 10!")
            
        if len(_errors) != 0:
            raise ValidatorException(_errors)
        
        
