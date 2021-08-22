from Game import Game
from Board import Board
class UI:
    def __init__(self):
        self._board = Board()
        self._game = Game(self._board)
    
    def start(self):
        #f = open("file.txt","w")
        playerTurn = True
        notDone = True
        while notDone == True:
            print(self._board)
            if playerTurn == True:
                print("Give the coordinates:")
                ok = 1
                try:
                    i = int(input())
                except ValueError as ve:
                    print(ve)
                    ok = 0
                
                try:
                    j = int(input())
                except ValueError as ve:
                    print(ve)
                    ok = 0
                
                
                print("Give the symbol")
                symbol = input()
                
                try:
                    self._game.moveHuman(i, j, symbol)
                except ValueError as ve:
                    print(ve)
                    ok = 0
                if ok == 1:
                    playerTurn = False
            else:
                self._game.moveComputer()
                playerTurn = True
            
            if self._game.isWon() == True:
                notDone = False
                print("Player won")
                print(self._board)
            elif self._game.isTie() == True:
                notDone = False
                print("Computer won")
                print(self._board)
                
            




        
   
ui = UI()
ui.start()
