import unittest 
from Game import Game
from Board import Board
class test(unittest.TestCase):
    def setUp(self):
        self._board = Board()
        self._game = Game(self._board)
    def test_4(self):
        l = self._board.getEmptySquares()
        self.assertTrue(len(l) == 36)
        self._game.moveHuman(3,4,"X")
        l = self._board.getEmptySquares()
        self.assertTrue(len(l) == 35)
        
        self._game.moveHuman(1,1,"X")
        self._game.moveHuman(2,1,"X")
        self._game.moveHuman(3,1,"X")
        self._game.moveHuman(4,1,"X")
        self._game.moveComputer()
        #print(self._board)
        l1 = self._board.getData()
        self.assertTrue(l1[24] == -1)
        
        self._board = Board()
        self._game = Game(self._board)
        #print(self._board)
        self._game.moveHuman(5,1,"X")
        self._game.moveHuman(5,2,"X")
        self._game.moveHuman(5,3,"X")
        self._game.moveHuman(5,4,"X")
        self._game.moveComputer()
        #print(self._board)
        l1 = self._board.getData()
        self.assertTrue(l1[28] == -1)
            
    