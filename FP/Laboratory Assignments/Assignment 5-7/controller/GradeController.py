from Repo.GradeRepository import GradeRepository
from Repo.StudentRepository import StudentRepository
from Repo.DisciplineRepository import DisciplineRepository
from domain.Studentdto import Student_avg
from Repo.StudentdtoRepo import StudentdtoRepo
from domain.Disciplinedto import Discipline_avg
from Repo.DisciplinedtoRepo import DisciplinedtoRepo
from domain.Undo import *



class Controller:
    def __init__(self, StudentRepository, DisciplineRepository, GradeRepository, undoController):
        '''
        Initializes the class Controller
        Input: StudentRepository, DisciplineRepository - lists of objects from Repo class
               GradeRepository - list of objects from GradeRepository class
        Output: Creates an object of controller class
        '''
        
        self._StudentRepository = StudentRepository
        self._DisciplineRepository = DisciplineRepository
        self._GradeRepository = GradeRepository
        self._undoController = undoController
    
    def add(self,grade):
        '''
        Adds an object to the GradeRepository
        Input: grade - an object from the Grade class
        Output: Adds a grade to the list represented by the GradeRepository or raises an error
        '''
        if grade.getValue() < 1 or grade.getValue() > 10:
            raise IndexError("Grade must be between 1 and 10")
        self._GradeRepository.add(grade)
        
        undo = FunctionCall(self.delete,grade)
        redo = FunctionCall(self.add,grade)
        oper = Operation(undo,redo)
        self._undoController.addOperation(oper)
        
        
    
    def delete(self,grade):
        for g in self._GradeRepository.getAll():
            if g == grade:
                self._GradeRepository.removeByDisciplineID(g.getDisciplineID())
            
    def students_sorted_by_name(self, discipline):
        '''
        Returns a list of objects representing students being graded at a given discipline, sorted alphabetically
        Input: discipline - a Discipline object's id field
        Output: a list of Student type objects which can be found in the GradeRepository with the value of discipline 
        '''
        l=[]
        
        for grade in self._GradeRepository.getAll():
            if grade.getDisciplineID() == discipline: #and find_stud(grade.getStudentID()) == False:
                if grade.getStudentID() not in l:
                    l.append(grade.getStudentID())
        
        
        l1 = []
        
        for idd in l:
            l1.append(self._StudentRepository.find(idd))
        
        l2 = []
        for obj in l1:
            l2.append(obj.getName())
        
        #print(l2)    
        
        
        #print(l2)
        
        self.combSort(l2,"cresc")
        
        #print(l2)
        
        '''
        for idd in l:
            l1.append(self._StudentRepository.find(idd))
        '''
        
        
        '''    
        for i in range (0,len(l1)-1):
            for j in range (i+1,len(l1)):
                if l1[i].getName()>l1[j].getName():
                    l1[i], l1[j] = l1[j], l1[i]  
        '''
        
        return l2
    
    def average(self,studentID,disc):
        '''
        Returns the average of a student at a certain discipline if it exists, 0 otherwise
        Input: studentID - an in , disc - a Discipline type object
        Output: Calculates and returns the average of a student at a certain discipline or 0 if they haven't been noted yet
        
        '''
        s=0
        ct=0
        for grade in self._GradeRepository.getAll():
            if grade.getStudentID() == studentID and grade.getDisciplineID() == disc:
                s = s + grade.getValue()
                ct = ct + 1
       
        
        if ct == 0:
            return 0
        else:
            s = s / ct
            return s
    
    
    
    def getNextGap(self,gap):  
        # Shrink gap by Shrink factor 
        gap = (gap*10)//13 
  
        if gap < 1:
            return 1 
        
        return gap 
    
    def combSort(self,a,mode):  
        # Initialize gap 
        
        
        n = len(a)
        gap = n
        # Initialize swapped as true to make sure that 
        # loop runs 
        swapped = True 
      
        # Keep running while gap is more than 1 and last 
        # iteration caused a swap 
        while gap != 1 or swapped == True:
            # Find next gap 
            gap = self.getNextGap(gap) 
      
            # Initialize swapped as false so that we can 
            # check if swap happened or not 
            swapped = False 
      
            # Compare all elements with current gap 
            for i in range(0,n-gap):
                '''
                if mode(a[i],a[j] == True):
                    a[i], a[i+gap] = a[i+gap], a[i]
                    swapped = True
                '''    
                
                if mode == "cresc":
                    if (a[i] > a[i+gap]): #ai-ai+1 >0 
                        a[i], a[i+gap] = a[i+gap], a[i]
                        swapped = True 
                elif mode =="descresc":
                    if (a[i] < a[i+gap]): #ai-ai+1 >0 
                        a[i], a[i+gap] = a[i+gap], a[i]
                        swapped = True 
        
    
    def students_sorted_by_avg(self, discipline):
        '''
        Returns a list of students sorted by their average at a certain discipline)
        Input: discipline - an integer
        Output: a list of students sorted descending by their average at the discipline having the id discipline
        '''
        
        l=[]
        for grade in self._GradeRepository.getAll():
            if grade.getDisciplineID() == discipline:
                if self.average(grade.getStudentID(),discipline):
                        if grade.getStudentID() not in l:
                            l.append(grade.getStudentID())
        
        l1 = []
        
        #print(l)
        
        
        #l1.append((idd,self.average(idd,discipline)))
        for idd in l:
            #stud_avg = Student_avg(self._StudentRepository.find(idd), self.average(idd, discipline))
            #l1.add(stud_avg)
            l1.append((idd,self.average(idd,discipline)))
        
        
        for i in range (0,len(l1)):
            for j in range (i+1,len(l1)):
                if l1[i][1] < l1[j][1]:
                #if l1[i].getAvg() < l1[j].getAvg():
                    l1[i], l1[j] = l1[j], l1[i]  
        
        
        l2 = StudentdtoRepo() 
        
        for i in range(0,len(l1)):
            stud_avg = Student_avg(self._StudentRepository.find(l1[i][0]), self.average(l1[i][0], discipline))
            l2.add(stud_avg)
            #l2.add(self._StudentRepository.find(l1[i][0]))   
        
        return l2
    
    def students_failing(self):
        '''
        Returns a list of students failing at a certain discipline (average<5)
        Input: - 
        Output: a list of all the students failing at one or more disciplines
        
        '''
        l1 = []
        for disc in self._DisciplineRepository.getAll():
            for stud in self._StudentRepository.getAll():
                if self.average(stud.getID(),disc.getID()):
                    if self.average(stud.getID(),disc.getID()) < 5:
                            l1.append((stud, disc))
                    
        return l1
     
    
    def functi(self,a,b):
        if a < b:
            return True
        else:
            return False
    
    

             
    
    def best_students(self):
        '''
        Returns a list with students sorted descending by their general average (average of averages at every discipline they have been noted at)
        Input: -
        Output: a list with students sorted descending by their average 
        
        
        '''
        l1 = []
        for stud in self._StudentRepository.getAll():
            ct = 0
            s = 0
            for disc in self._DisciplineRepository.getAll():
                if self.average(stud.getID(), disc.getID()):
                    s = s + self.average(stud.getID(), disc.getID())
                    ct = ct + 1
            l1.append((stud.getID(),s/ct))
            
        '''
        for i in range (0,len(l1)):
            for j in range (i+1,len(l1)):  
                if l1[i][1] < l1[j][1]:
                    l1[i], l1[j] = l1[j], l1[i]    
        '''
        
        
        self.combSort(l1,self.functi)
        
                    
        
        l2 = StudentdtoRepo() 
        
        for i in range(0,5):
            stud_avg = Student_avg(self._StudentRepository.find(l1[i][0]), l1[i][1])
            l2.add(stud_avg)
                
        return l2
        
    #clasa cu disc si media
    
    def find_disc(self, id_disc):
        '''
        Finds if a discipline has any noted 
        Input: id_disc - an integer
        Output: returns True if they are any marks at the discipline having the id equal to id_disc
                returns False otherwise
        '''
        for grade in self._GradeRepository.getAll():
            if grade.getDisciplineID() == id_disc:
                return True
        return False
    
    def avg_grade_disc(self,id_disc):
        '''
        Returns the average of all students at a certain discipline
        Input: id_disc - an integer
        Output: returns an integer representing the average of a certain discipline
        
        '''
        s=0
        ct=0
        for student in self._StudentRepository.getAll():  
            if self.average(student.getID(), id_disc):
                s=s+self.average(student.getID(),id_disc)
                #print (s)
                ct=ct+1
        if ct == 0:
            return 0
        else:
            #print(s/ct)
            return s/ct    
        
            
        
    def disc_one_grade(self):
        '''
        Returns a list with disciplines sorted descending by their average
        Input: -
        Output: a list with all disciplines sorted descending by the averages of the students average at that discipline
        '''
        l1 = []
        for disc in self._DisciplineRepository.getAll():
            if self.find_disc(disc.getID()):
                l1.append(disc)
                
             
        for i in range (0,len(l1)):
            for j in range (i+1,len(l1)):  
                if self.avg_grade_disc(l1[i].getID()) and self.avg_grade_disc(l1[j].getID()):
                    if self.avg_grade_disc(l1[i].getID()) < self.avg_grade_disc(l1[j].getID()):
                        l1[i], l1[j] = l1[j], l1[i] 
        #print(l1)
        l2 = DisciplinedtoRepo()
        
        for i in range(0,len(l1)):
            disc_avg = Discipline_avg(l1[i], self.avg_grade_disc(l1[i].getID()))
            l2.add(disc_avg)
        
        return l2
    
    
    
    
            
    def deleteStudent(self, idd):
        '''
        Deletes a student 
        Input: idd - an integer
        Output: Deletes from the StudentRepository the student having the id field equal to idd and from the GradesRepository
               all marks belonging to that student
        '''
        co = CascadedOperation()
        
        #list = self._GradeRepository.search_stud(idd)
        
        for grade in self._GradeRepository.getAll():
            if idd == grade.getStudentID():
                undo = FunctionCall(self.add,grade)
                redo = FunctionCall(self.delete,grade)
                oper = Operation(undo,redo) 
                co.add(oper)
                    
        
        undo = FunctionCall(self._StudentRepository.add,self._StudentRepository.find(idd).getID(),self._StudentRepository.find(idd).getName())
        redo = FunctionCall(self._StudentRepository.delete,idd)
        
        oper = Operation(undo,redo)
        co.add(oper)
        
        self._undoController.addOperation(co)
        
        
        self._StudentRepository.delete(idd)
        self._GradeRepository.removeByStudentID(idd)
        
    def deleteDiscipline(self, idd):
        '''
        Deletes a discipline 
        Input: idd - an integer
        Output: Deletes from the DisciplineRepository the discipline having the id field equal to idd and from the GradesRepository
               all marks belonging to that discipline
        '''
        co = CascadedOperation()
        
        for grade in self._GradeRepository.getAll():
            if idd == grade.getDisciplineID():
                undo = FunctionCall(self.add,grade)
                redo = FunctionCall(self.delete,grade)
                oper = Operation(undo,redo) 
                co.add(oper)
                    
        
        undo = FunctionCall(self._DisciplineRepository.add,self._DisciplineRepository.find(idd).getID(),self._DisciplineRepository.find(idd).getName())
        redo = FunctionCall(self._DisciplineRepository.delete,idd)
        
        oper = Operation(undo,redo)
        co.add(oper)
        
        self._undoController.addOperation(co)
        
        self._DisciplineRepository.delete(idd)
        self._GradeRepository.removeByDisciplineID(idd)
        
