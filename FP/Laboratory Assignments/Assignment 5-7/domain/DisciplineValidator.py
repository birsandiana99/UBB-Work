from domain.Discipline import Discipline
from domain.ValidatorException import ValidatorException

class Discipline_Validator:
    def validate(self, discipline):
        if type(discipline) != Discipline:
            raise TypeError("Not a discipline!")
        
        _errors = []

        if type(discipline.getID()) != int:
            _errors.append("ID must be an int!")
            
        if len(discipline.getName()) == 0:
            _errors.append("Empty ~name~ field!")
            
        if type(discipline.getName()) != str:
            _errors.append("Name must be a string")
            
        if len(_errors) != 0:
            raise ValidatorException(_errors)