import unittest
from Repo.Repository import Repository
from Repo import RepositoryException
from domain.Student import Student
class RepositoryTest(unittest.TestCase):
    def setUp(self):
        self._repo = Repository()
        
    
    def testRepo(self):
    
        self._repo.add(Student(1, "Povara Daniel"))
        self._repo.add(Student(2, "Racoti Andreea"))
        self._repo.add(Student(3, "Pop Alexandra"))
        self._repo.add(Student(4, "Glogovetan Anton"))
    
        self.assertTrue(len(self._repo) == 4)
        self.assertTrue( self._repo.find(1) == Student(1,"Povara Daniel"))
        self._repo.update(1,"FSJ")
        self.assertTrue (self._repo.find(1) == Student(1,"FSJ"))
        self._repo.delete(1)
        s= Student(1,"Povara Daniel")
        self.assertTrue(s not in self._repo.getAll())
        self.assertTrue( len(self._repo) == 3)
        self.assertRaises(IndexError, self._repo.add,Student(2,"Silvia"))
    