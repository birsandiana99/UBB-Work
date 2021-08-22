class Controller:
    def __init__(self, repo):
        self._repository = repo
        
    def add(self,obj):
        '''
        adds an object to the repository of the controller
        input: an object (type = Assignment)
        output: the object is added to the repository
        '''
        self._repository.add(obj)
    
    def dishonestyCheck(self):
        '''
        checks for assignment pairs which have more than 20% of the words in common
        input: - 
        output: listt -  a list of tupels of this form: (student_name1,student_name2,percentage)
         which represents the pairs of students who failed the dishonesty check

        '''
        lst = []
        listt = []
        for obj1 in self._repository.getAll():
            for obj2 in self._repository.getAll():
                    if obj1.getID() != obj2.getID():
                        #print(str(obj1),str(obj2))
                        sol1 = obj1.getSolution().split(" ")
                        sol2 = obj2.getSolution().split(" ")
                        #print(sol1,sol2)
                        if len(sol1) > len(sol2):
                            sol1,sol2 = sol2,sol1
                        #sol 1 e cel mai mic
                        ct = 0
                        for cuv in sol1:
                            if cuv in sol2:
                                ct += 1
                        procentaj = ct/len(sol1) * 100
                        if procentaj > 20:
                            if (obj1.getID(),obj2.getID()) not in lst and (obj2.getID(),obj1.getID()) not in lst:
                                lst.append((obj1.getID(),obj2.getID()))
                                listt.append((obj1.getName(),obj2.getName(),procentaj))
        return listt
        
        