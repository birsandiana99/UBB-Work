import unittest
from domain.Grade import Grade
from domain.GradeValidator import Grade_Validator
from domain.ValidatorException import ValidatorException

class GradeTestCase(unittest.TestCase):
    def setUp(self):
        self.validator = Grade_Validator()
        self.grade = Grade(1,1,10)
        
    def testGrade(self):
        self.assertTrue(self.grade == Grade(1,1,10))
        self.assertTrue(self.grade.getDisciplineID() == 1)
        self.assertTrue(self.grade.getStudentID() == 1)
        self.assertTrue(self.grade.getValue() == 10)
        
        
        self.assertRaises(ValidatorException,self.validator.validate,Grade(1,0,1))  
        self.assertRaises(ValidatorException,self.validator.validate,Grade(2,"adasd",3)
        
    