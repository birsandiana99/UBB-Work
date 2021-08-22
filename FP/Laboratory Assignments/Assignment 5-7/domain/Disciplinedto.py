class Discipline_avg:
    def __init__(self, discipline, avg):
        self._discipline = discipline
        self._avg = avg
        
    def getAvg(self):
        return self._avg
    
    def __str__(self):
        return self._discipline.getName() + " has an average of: "+ str(self._avg)