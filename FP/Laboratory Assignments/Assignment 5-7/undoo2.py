#client controller
'''
def create(self, clientID,clientCNP,clientName):
    client = client(clientID,clientCNP,clientName)
    self._validator = validator.validate(client)
    self._repository = Repo.store(client)
    
    
    undo = FunctionCall(self.delete,clientID)
    redo = FunctionCall(self.create,clientID,clientCNP,clientName)
    oper = Operation(undo,redo)
    self._undoController.addOperation(oper)
    
'''    
    
'''
    cand undo apeleaza functiile din program, inregistrarea operatiilor pt undo trb sa fie suspendata
    
    pt delete:
    
    redo = FunctionCall(self.delete,clientID)
    undo = FunctionCall(self.create,client.ID,client.CNP,client.Name)
    oper = Operation(undo,redo)
    
    co = CascadedOperation()
    co.add(oper)
    
    for r in rentals: 
        redo = FunctionCall(self._rentalController.deleteRental,r.id)
        undo = FunctionCall(self._rentalController.createRental,'rental params')
        oper = Operation(undo,redo) 
        co.add(oper)
    
    
    
    self._undoController.addOperation(oper)
    
    --> lista de operation
        

'''