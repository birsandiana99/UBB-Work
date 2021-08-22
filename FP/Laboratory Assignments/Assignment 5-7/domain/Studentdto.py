class Student_avg:
    def __init__(self,student,avg):
        self._student = student
        self._avg = avg
        
    def getAvg(self):
        return self._avg
    
    def __str__(self):
        return str(self._student) + " has an average of: "+ str(self._avg)