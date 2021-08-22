import unittest
from domain.Student import Student
from domain.StudentValidator import Student_Validator
from domain.ValidatorException import ValidatorException

class StudentTestCase(unittest.TestCase):
    def setUp(self):
        self.validator = Student_Validator()
        self.student = Student(1,"Andrasi Daniela")
        
    def testStudent(self):
        self.assertTrue(self.student == Student(1,"Andrasi Daniela"))
        self.assertTrue(self.student.getID() == 1)
        self.assertTrue( str(self.student) == "ID: 1 / Name: Andrasi Daniela")

        self.assertTrue(self.student.getName() == "Andrasi Daniela")
        
        self.student.setName("FSJ")
        self.assertTrue(self.student.getName() == "FSJ")
        
        self.assertTrue(self.validator.validate, self.student)
        self.student.setName("")
        self.assertRaises(ValidatorException, self.validator.validate, self.student)
        