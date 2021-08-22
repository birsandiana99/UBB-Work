'''
whenever you do an operation in one of the controllers you have to tell the undo controller
and you also have to tell it how to undo it and redo it
'''

class UndoCrontroller:
    def __init__(self):
        #a list of what happened in the program ----> behaves like a stack
        self._operations = []
        #undo - move to the list, redo - move to the right 
        self._index = -1
        self._duringUndo = False
    
    
    def addOperation(self, operation):  
        if self._duringUndo == True: #nu mai intra in undo daca e in alt undo!!!
            return
          
        #we only keep the operations between 0 and the current index-1
        self._index += 1
        self._operations = self._operations[:self._index]
        
        self._operations.append(operation)
        #when you make another operation you only get undos
        
        
    
        
    def undo(self):
        '''
        first it checks the index
        when we want to undo, we take the operation at index 0 then we decrease the index
    
        '''
        self._duringUndo = True
        if self._index == -1:
            return False #no more undos
        
        self._operations[self._index].undo()
        self._duringUndo = False
        self._index = self._index - 1
        
        return True
        
        
    def redo(self):
        if self._index>= len(self._operations) or self._index == -1:
            return False
        #if you only have one operations and the lenght is 1 than the lenght is 
        self._index += 1
        self._duringUndo = True
        self._operations(self._index).redo()
        self._duringUndo = False
      

class CascadedOperation:
    def __init__(self):
        self._operations = []
        
    def add(self, oper):
        self._operations.append(oper)
        
    def undo(self):
        for o in self._operations:
            o.undo()
            
    
    def redo(self):
        for o in self._operations:
            o.redo()


class Operation:
    '''
    2 lucruri: - undo
               - redo
    
    '''
    def __init__(self,undoFunction,redoFunction):
        self._undoFunction = undoFunction
        self._redoFunction = redoFunction
        
        
    def undo(self):
        self._undoFunction.call()
    
    
    def redo(self):
        self._redoFunction.call()
    
    
    
class FunctionCall:
    def __init__(self, func, *params):
        self._function = func
        self._params = params
        
    def call(self):
        self._function(*self._params)
        
        
        

        
        
        
        
        
          