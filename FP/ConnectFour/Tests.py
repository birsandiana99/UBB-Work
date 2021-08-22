import unittest
from program import *
class GameTests(unittest.TestCase):
    def setUp(self):
        self._board = Board()
        self._game = Game(self._board)
    
    def testCheckLine(self):
        self._board.move(1,'1')
        self._board.move(2,'1')
        self._board.move(3,'1')
        self._board.move(4,'1')
        
        
        self.assertTrue(self._board.isWon() == 1)
    
    def testCheckColum(self):
        self._board.move(1,'2')
        self._board.move(1,'2')
        self._board.move(1,'2')
        self._board.move(2,'1')
        self._board.move(2,'1')
        self._board.move(1,'2')
        
        self.assertTrue(self._board.isWon() == -1)
        
        
    def testCheckDiagonals(self):
        self._board.move(1,'1')
        self._board.move(2,'2')
        self._board.move(2,'1')
        self._board.move(3,'2')
        self._board.move(3,'2')
        self._board.move(3,'1')
        self._board.move(4,'1')
        self._board.move(4,'2')
        self._board.move(4,'2')
        self._board.move(4,'1')
        
        self.assertTrue(self._board.isWon() == 1)