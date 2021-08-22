import unittest
from Domain.Assignment import Assignment
from Repo.Repository import Repository
from Contr.Controller import Controller

class ContrTest(unittest.TestCase):
    def setUp(self):
        self._repository = Repository()
        self._controller = Controller(self._repository)
        
    def testAdd(self):
        self._repository.add(Assignment(1,"Maria","Idk"))
        self.assertTrue(len(self._repository) == 1)
        self.assertRaises(IndexError,self._repository.add,Assignment(1,"dsda","nu"))
        
        self._controller.add(Assignment(2,"Mariaa","Idkkk"))
        self.assertTrue(len(self._repository) == 2)
        self.assertRaises(IndexError,self._controller.add,Assignment(2,"dsddsfa","nudsf"))
        
    def testDishonesty(self):
        self._repository.add(Assignment(1,"Anna","I will make sure to implement a layered architecture solution"))
        self._repository.add(Assignment(2,"John","The program is layered"))
        l = self._controller.dishonestyCheck()
        self.assertTrue(len(l) == 1)
        
        self._repository.add(Assignment(3,"Betty", "I did not understand layered architecture"))
        l1 = self._controller.dishonestyCheck()
        self.assertFalse(len(l1) == 1)
        self.assertTrue(len(l1) == 3)