class TransferStudentDiscipline:
    def __init__(self, student, discipline, grade):
        self._student = student
        self._grade = grade
        self._discipline = discipline
        
    def getStudent(self):
        return self._student
    
    def getGrade(self):
        return self._grade
    