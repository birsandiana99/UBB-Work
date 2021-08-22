from Repo.Repository import Repository
from Repo.TextRepo import TextFilesRepo
from Domain.Assignment import Assignment
from Contr.Controller import Controller

'''
repo = TextFilesRepo("assignments.txt")
for obj in repo.getAll():
    print(str(obj))
'''


'''
repo1 = Repository()
repo1.add(Assignment(1,"asd","afdasds"))
repo1.add(Assignment(2,"asd","afdasds"))
repo1.add(Assignment(3,"asd","afdasds"))
repo1.add(Assignment(4,"asd","afdasds"))
repo1.add(Assignment(5,"asd","afdasds"))
for obj in repo1.getAll():
    print(str(obj))
    
'''
    
class UI():
    def __init__(self):
        pass
    
    
    def Menu(self):
        print("Press 1. to add an assignment.")
        print("Press 2. to display all the assignments.")
        print("Press 3. for dishonesty check.")
        print("Press 0. to exit.")
    
    def addAssignment(self, listt):
        try:
            idd = int(input("ID: "))
            name = input("Name: ")
            solution = input("Solution: ")
            listt.add(Assignment(idd,name,solution))
        except IndexError as ie:
            print(ie)
        except ValueError:
            print("Id must be an integer!")
        except SyntaxError as se:
            print(se)
    
    def showAssignments(self,repo):
        for obj in repo.getAll():
            print(str(obj))
            
            
    def dishonestyCheck(self,contr):
        l = contr.dishonestyCheck() 
        for o in l:
            print(o)
    
    
def main():
    ui = UI()
    repo = TextFilesRepo("assignments.txt")
    contr = Controller(repo)
    ui.Menu()
    n = -1
    while n is not 0:
        n = int(input())
        if n == 1:
            ui.addAssignment(contr)
        elif n == 2:
            ui.showAssignments(repo)
        elif n == 3:
            ui.dishonestyCheck(contr)


main()
    
    
    
    