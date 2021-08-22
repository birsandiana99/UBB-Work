from domain.Student import Student
from domain.StudentValidator import Student_Validator

from domain.Discipline import Discipline
from domain.DisciplineValidator import Discipline_Validator

#from domain.Studentdto import Student_avg

from domain.Grade import Grade

from Repo.Repository import Repository
from Repo.RepositoryException import RepositoryError
from Repo.GradeRepository import GradeRepository

from Repo.StudentRepositoryTextFile import StudentTextFileRepo
from Repo.DisciplineRepositoryTextFile import DisciplineTextFileRepo
from Repo.GradesRepositoryTextFile import GradesTextFileRepo

from controller.GradeController import Controller

from controller.DisciplineController import DisciplineController

from controller.StudentController import StudentController

from Iterable.Iterable_class import Iter

from domain.Undo import *
from Repo.DisciplineRepository import DisciplineRepository
from Repo import StudentRepository
from Repo.PickleRepository import PickleRepo
from Repo.GradePickleRepo import GradePickleRepo

class UI:
    def __init__(self):
        pass
    
    def Print_Menu(self):
        #print("Press * for showing the menu again")
        print("Press 1. for adding a student.")
        print("Press 2. for removing a student.")
        print("Press 3. for updating a student.")
        print("Press 4. for listing the students.")
        print("\n")
        print("Press 5. for adding a discipline.")
        print("Press 6. for removing a discipline.")
        print("Press 7. for updating a discipline.")
        print("Press 8. for listing the disciplines.")
        print("\n")
        print("Press 9. for grading a student.")
        print("Press 10. for viewing the grades list.")
        print("\n")
        print("Press 11. for searching a student by ID.")
        print("Press 12. for searching a student by name.")
        print("Press 13. for searching a discipline by ID.")
        print("Press 14. for searching a discipline by name.")
        print("\n")
        print("Press 15. for viewing all students enrolled at a given discipline, sorted alphabetically")
        print("Press 16. for viewing all students enrolled at a given discipline  by descending average grade")  
        print("Press 17. for viewing a list with students failing at one or more disciplines.")
        print("Press 18. for viewing the best students.")
        print("Press 19. for viewing all disciplines at which there is at least one grade, sorted in descending order of the average grade received by all students enrolled at that discipline.")
        #print("Press 20. for searching a discipline by name.")
        print("\n")
        print("Press u for undo.")
        print("Press r for redo.")
        print("\n")
        print("Press 0. for exiting the program.")
            
    def addStudentUI(self,studList):
        '''  idd = 0
        
        try:
            idd = int(str(input("ID: ")))
        except ValueError:
            print("A student's id must be an integer")
        
       
        
        name = input("Name: ")
        if idd!=0:
            try:
                studList.add(idd,name)
                #undoController.addOperation()
            except IndexError as se:
                print(se)
                
                
        '''
        
        try:
            idd = int(str(input("ID: ")))
            name = input("Name: ")
            studList.add(idd,name)
        except SyntaxError as se:
            print(se)
        
        '''
        idd = input("ID: ")
        name = input("Name: ")
        try:
            studList.add(idd,name)
        except IndexError as ie:
            print(ie)
        except SyntaxError as se:
            print(se) 
        except ValueError:
            print("A student's id must be an int!")
        
        '''
            
    def removeStudentUI(self,gradeController):
        try:
            idd = int(input("ID: "))
            gradeController.deleteStudent(idd)    
        except ValueError:
            print("A student's id must be an integer")
        
        #studList.delete(idd)
    
    def updateStudentNameUI(self, studList):
        id1=0
        try:
            id1 = int(input("ID: "))
        except ValueError:
            print("A student's id must be an integer")
            
        if id1!=0:
            name=input("New name:")
            for stud in studList.getAll():
                if stud.getID() == id1:
                    studList.update(id1,name)
                    
    def listStudentsUI(self, studList):
        for stud in studList.getAll():
            print(str(stud)) 
        
    def addDisciplineUI(self, discList):
       
        idd = 0
        try:
            idd = int(input("ID: "))
        except ValueError:
            print("ID must be an integer")
            
        if idd != 0:
            name = input("Name: ")
            try:
                discList.add(idd,name)
            except IndexError as se:
                print(se)
        '''
        idd = input("ID: ")
        name = input("Name: ")
        try:
            discList.add(idd,name)
        except IndexError as ie:
            print(ie)
        except SyntaxError as se:
            print(se) 
        except ValueError:
            print("A discipline's id must be an integer!")   
        
        '''    
    def removeDisciplineUI(self, gradeController):
        try:
            idd = int(input("ID: "))
            gradeController.deleteDiscipline(idd)
        except ValueError:
            print("A discipline's id must be an integer!")
    
    def listDisciplinesUI(self, discList):
        for disc in discList.getAll():
            print(str(disc)) 
            
     
    
                
    def updateDisciplineName_UI(self, discList):
        try:
            id1 = int(input("ID: "))
        except ValueError:
            print("A discipline's id must be an integer")
        name=input("New name:")
        for disc in discList.getAll():
            if disc.getID() == id1:
                discList.update(id1,name)   
    
    def gradeStudentUI(self, gradesList):
        idStudent = 0 
        idDiscipline = 0
        value = 0
        try:
            idDiscipline = int(input("ID discipline: "))
            idStudent = int(input("ID student: "))
            value = int(input("Value: "))
        except ValueError:
            print("All datas must be integers!")
            
        if idStudent!=0 and idDiscipline!=0 and value!=0:    
            try:
                try:
                    gradesList.add(Grade(idDiscipline,idStudent,value))
                except SyntaxError as se:
                    print(se)
            except IndexError as ie:
                print(ie)
            
                
    def students_disc_sort_by_name(self, gradeController):  
        discipline = int(input("Discipline ID: "))
        l = gradeController.students_sorted_by_name(discipline)
        for obj in l:
            print(str(obj))  
            
    def students_disc_sort_by_avg(self, gradeController):
        discipline = int(input("Discipline ID: "))
        l = gradeController.students_sorted_by_avg(discipline)
        #print(len(l))
        for obj in l.getAll():
            print(str(obj))
    
    def students_failing(self, gradeController):
        l = gradeController.students_failing()
        for i in range(0,len(l)):
            print("Student: " + str(l[i][0])+"/// is failing at: "+l[i][1].getName())
    
    
    def gradelistUI(self, gradeList):
        for grade in gradeList.getAll():
            print(str(grade))  
    
    def best_students(self, gradeController):
        #clasa cu student si media
        l = gradeController.best_students()
        for obj in l.getAll():
            print(str(obj))
    
    
    def search_id(self,l):
        idd = input("ID:")
        try:
            idd = int(idd)
            
            obj = l.find(idd)
            print(str(obj))
        except ValueError:
            print("ID must be an integer!")
    
    def search_name(self,l):
        name = input("Name: ")
        name = name.lower()
        
        l1=l.search_name(name)
        
        if len(name) == 1:
            for o in l1:
                print(str(o))
        else:
            print (str(l1))
        
    
    def disc_one_grade(self, gradeController):
        l = gradeController.disc_one_grade()
        for disc in l.getAll():
            print(str(disc))
    
    
    def initStudents(self,l):
        
        l.add(Student(1, "Povara Daniel"))
        l.add(Student(2, "Racoti Andreea"))
        l.add(Student(3, "Pop Alexandra"))
        l.add(Student(4, "Glogovetan Anton"))
        l.add(Student(5, "Moromete Gabriela"))
        l.add(Student(6, "Cantemir Andrei"))
        l.add(Student(7, "Calburean Simona"))
        l.add(Student(8, "Deac Cosmin"))
        l.add(Student(9, "Cretu Alexandru"))
        l.add(Student(10, "Zidaru Anca"))  
        
        '''
        prenume = ["Mihai","Gheoghe","Ionut","Gelu","Octavian","Miruna","Laura","Andreea","Maria","Traian"]
        nume_fam = ["Popescu ","Munteanu ","Brunea ","Stark ","Brumbea ","Corbu ","Stanciu ","Ursu ","Teodor ","Andrasi "]
        ct = 0
        for i in nume_fam:
            for j in prenume:
                idd = ct+1 
                l.add(Student(idd,i+j))
                ct=ct+1
        '''
        
        
    
    def initDisciplines(self,l):
        l.add(Discipline(1, "Algebra"))
        l.add(Discipline(2, "Informatica"))
        l.add(Discipline(3, "Geografie"))
        l.add(Discipline(4, "Istorie"))
        l.add(Discipline(5, "Literatura"))
        l.add(Discipline(6, "Gramatica"))
        l.add(Discipline(7, "Teoria muzicii"))
        l.add(Discipline(8, "Logica computationala"))
        l.add(Discipline(9, "Analiza"))
        l.add(Discipline(10, "Geometrie"))
        
        
        
    
    def initGrades(self,l):
        l.add(Grade(1,10,10))
        l.add(Grade(1,10,8))
        l.add(Grade(1,10,7))
        l.add(Grade(1,1,10))
        l.add(Grade(1,2,8))
        l.add(Grade(2,1,5))
        l.add(Grade(3,9,4))
        l.add(Grade(4,8,1))
        l.add(Grade(5,7,3))
        l.add(Grade(6,6,2))
        l.add(Grade(7,5,7))
        l.add(Grade(8,4,10))
        l.add(Grade(9,3,9))
        l.add(Grade(10,2,8))
        
        l.add(Grade(4,3,1))
        l.add(Grade(4,3,5))
        l.add(Grade(7,3,1))
        l.add(Grade(10,2,1))
        
        '''
        from random import randint
        for i in range (1,100):
            l.add(Grade(randint(1,10),i,randint(1,10)))
        
        
        '''
'''
def readSettings():
    f = open("settings.properties","r")
    s = f.read()
    lines = s.split("\n")
    firstLine = lines[1]
    
    #lines[1]
    settings ={}
    for line in lines:
        keyvalue = line.split("=")
        settings[keyvalue[0].strip()] =keyvalue[1].strip  
    print(settings)
    return settings   
'''   



  
# Function to sort a[0..n-1] using Comb Sort 

    
         
def funct(a,b):
    return True     
            
def acceptance_function(x):
    if x.getName() == "Moromete Gabriela":
        #print("aici")
        return False
    return True
        
def filt(l,acceptance_function):
    i = 0
    while i < len(l):
        if acceptance_function(l[i]) == False:
            del l[i]
        else:
            i = i+1

        
def readSettings():
    f = open("settings.properties","r")
    s = f.read()
    lines = s.split("\n")
    settings = {}
    for line in lines:
        keyvalue = line.split("=")
        settings[keyvalue[0].strip()] = keyvalue[1].strip()
    return settings
    
def main():    
    
    ui=UI()
    undoController = UndoCrontroller()
    '''
    settings = readSettings()
    if settings["repo_type"]=="memory":
        studentRepo = Repository()
        disciplineRepo = Repository()
        gradesList = GradeRepository()
        
        
    elif settings["repo_type"]=="textfiles":
        studentRepo = StudentTextFileRepo("Students.txt")
        disciplineRepo = DisciplineTextFileRepo("Disc.txt")
        gradesList = GradesTextFileRepo("Grades.txt")
        
        
    elif settings["repo_type"] == "binaryfiles":
        studentRepo = PickleRepo("studpickle.pickle")
        disciplineRepo = PickleRepo("discpickle.pickle")
        gradesList = GradePickleRepo("gradespickle.pickle")
    
    '''
    
    #studentRepo = Repository()
    #studentRepo = PickleRepo("studpickle.pickle")
    #studentRepo = StudentTextFileRepo("Students.txt")
    
    studentRepo = Repository()
    ui.initStudents(studentRepo)
    studentValidator = Student_Validator()
    studList = StudentController(studentValidator,studentRepo,undoController)
    

    '''
    import pickle
    f1 = open("studpickle.pickle","wb")
    pickle.dump(studentRepo.getAll(),f1)
    f1.close()
    '''
        
    #disciplineRepo = Repository()
    #disciplineRepo = PickleRepo("discpickle.pickle")
    #disciplineRepo = DisciplineTextFileRepo("Disc.txt")
    disciplineRepo = Repository()
    ui.initDisciplines(disciplineRepo)
    disciplineValidator = Discipline_Validator()
    discList = DisciplineController(disciplineValidator,disciplineRepo,undoController)
    
    
    '''
    import pickle
    f2 = open("discpickle.pickle","wb")
    pickle.dump(disciplineRepo.getAll(),f2)
    f2.close()
    '''
    
    
    #gradesList = GradePickleRepo("gradespickle.pickle")
    #gradesList = GradesTextFileRepo("Grades.txt")
    #gradesList = GradeRepository()
    
    gradesList = GradeRepository()
    ui.initGrades(gradesList)
    gradeController = Controller(studList,discList,gradesList,undoController)
    
    
    '''
    import pickle
    f3 = open("gradespickle.pickle","wb")
    pickle.dump(gradesList.getAll(),f3)
    f3.close()
    '''
    

    
    '''
    l = [1,6,-5,3,2,0,11234,4324]
    print(l)
    combSort(l,"cresc")
    print(l)
    '''
   
    
    '''
    
    l2 = [2,3,64,2,3,4,0,2]
    filt(l2,acceptance_function)
    print(l2)
    '''
    '''
    l = Iter(studentRepo)
    for stud in l:
        print(str(stud))
    filt(l,acceptance_function)
    print(len(l))
    for obj in l:
        print(str(obj))
    
    '''
    
    
    '''
    print(len(studentRepo))
    for stud in studentRepo.getAll():
        print(stud)
    
    
    '''
    
    print("Press * to show the menu.")
    #Print_Menu()
    ok = 1
    while ok == 1:
        n = input()
        if n == "*":
            ui.Print_Menu()
            
        elif n == 'r':
            #if undoController.redo() == False:
            #    print("No more redos")
            #else:
            #    undoController.redo()
            try:
                undoController.redo()
            except IndexError as ie:
                print(ie)
            
        elif n == 'u':
            #if undoController.undo() == False:
            #    print("No more undos")
            #else:
            #    undoController.undo()
            try:
                undoController.undo()
            except IndexError as ie:
                print(ie)
        else: 
            try:
                user_input = int(n)
                if user_input == 1:
                    ui.addStudentUI(studList)
                            
                elif user_input == 2:
                    ui.removeStudentUI(gradeController)
                    
                elif user_input == 3:
                    ui.updateStudentNameUI(studList)
                    
                elif user_input == 4:
                    ui.listStudentsUI(studList)
                     
                elif user_input == 5:
                    ui.addDisciplineUI(discList)
                   
                elif user_input == 6:
                    ui.removeDisciplineUI(gradeController)
                    
                elif user_input == 7:
                    ui.updateDisciplineName_UI(discList)
                    
                elif user_input == 8:
                    ui.listDisciplinesUI(discList)
                   
                elif user_input == 9:
                    ui.gradeStudentUI(gradeController)
                
                elif user_input== 10:
                    ui.gradelistUI(gradesList) 
                    
                elif user_input == 11:
                    ui.search_id(studList)
                    
                elif user_input == 12:
                    ui.search_name(studList)
                
                elif user_input == 13:
                    ui.search_id(discList)
                    
                elif user_input == 14:
                    ui.search_name(discList)
                    
                elif user_input == 15:
                    ui.students_disc_sort_by_name(gradeController)
                
                elif user_input == 16:
                    ui.students_disc_sort_by_avg(gradeController)
                
                elif user_input == 17:
                    ui.students_failing(gradeController)
                
                elif user_input == 18:
                    ui.best_students(gradeController)
                
                elif user_input == 19:
                    ui.disc_one_grade(gradeController)
                
                elif user_input == 20:
                    pass
                elif user_input == 0:
                    ok = 0
                else:
                    print("Invalid command!")
            except ValueError:
                print("Invalid command!")
            
main()
