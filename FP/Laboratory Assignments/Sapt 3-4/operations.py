def readCommand():
    """
    Read and parse user commands
    input: -
    output: (command, params) tuple, where
            command is user command
            params is the parameters list
    """
    raw_input = input()
    command = raw_input.split(' ')[0]
    params = raw_input.split(' ')[1:]
    return (command, params)

def set_up(transList):
    transList.append({'day':24,'value':40,'type':'in','description':'salary'})
    transList.append({'day':12,'value':204,'type':'in','description':'bonus'})
    transList.append({'day':25,'value':100,'type':'out','description':'expenses'})
    transList.append({'day':30,'value':500,'type':'out','description':'pizza'})
    transList.append({'day':10,'value':10,'type':'out','description':'gift'})
    transList.append({'day':1,'value':44,'type':'out','description':'debt'})
    transList.append({'day':2,'value':900,'type':'in','description':'grandma'})
    transList.append({'day':11,'value':100,'type':'in','description':'friend'})
    transList.append({'day':4,'value':245,'type':'out','description':'food'})
    transList.append({'day':24,'value':130,'type':'in','description':'sales'})
    transList.append({'day':23,'value':12,'type':'in','description':'salary'})
    transList.append({'day':22,'value':10,'type':'in','description':'salary'})
    transList.append({'day':20,'value':134,'type':'in','description':'bonuses'})
    transList.append({'day':19,'value':97,'type':'out','description':'car'})
    transList.append({'day':15,'value':24,'type':'out','description':'dog'})
    sort_day(transList)

'''

UNDO COMMAND

'''
def record_undo(transList, undoList):
    undoList.clear()
    undoList.extend(deepcopy(transList))

def copy_list(transList):
    newList=deepcopy(transList)
    return newList

def undo(transList,undoList):
    if len(undoList)==0:
        raise ValueError("No more undos") 
    #prodList[:]=undo_list.pop()

    transList.clear()
    transList[:]=undoList[-1] 
    del undoList[-1]

'''

ADD COMMAND

'''
def add(transList,value,t_type,description,undoList):
    '''
    Adds a new transaction to the list, for the current day
    Input: tranList- the list of the transactions, value- the value of the new transaction, description- the description of the new transaction
    Output:-
    '''
    undoList.append(copy_list(transList))
    from datetime import datetime
    value=int(value)
    now=datetime.now()
    trans=create_trans(now.day,value,t_type,description)
    transList.append(trans)
    

'''

INSERT COMMAND

'''

def insert(transList,day,value,t_type,description,undoList):
    '''
    Inserts a new transaction at a specified day
    Input: transList- the list of the transactions, day- the day of the new transaction, value- the value of the new transaction,
           t_type- the type of the new transaction, description- the description of the new transaction
    Output: -
    '''
    undoList.append(copy_list(transList))
    trans=create_trans(day,value,t_type,description)
    transList.append(trans)
    
            

'''

REMOVE COMMAND

'''

def removeDay(transList,day,undoList):
    '''
    Removes the transaction with a specified from the transaction list
    Input: transList- the list of the transactions, day- an int representing the day specified by the user
    Output: -
    '''
    undoList.append(copy_list(transList))
    i=0
    while i<len(transList):
        if get_day(transList[i])==day:
            del transList[i]
        else:
            i=i+1
        
            

def removeBetween(transList,day,end_day,undoList):
    '''
    Removes all the transactions between two days
    Input: transList- the list of the transactions, day- and int representing the first day specified by the user, end_day- and int representing the end day specified by the user
    Output: -
    
    '''
    undoList.append(copy_list(transList))
    i=0
    while i<len(transList):
        if get_day(transList[i])>=day and get_day(transList[i])<=end_day:
            del transList[i]
        else:
            i=i+1

def removeType(transList,t_type,undoList):
    '''
    Removes all the transactions of a type
    Input: transList- the list of the transactions, t_type- a string representing the type specified by the user
    Output: -
    '''
    undoList.append(copy_list(transList))
    i=0
    while i<len(transList):
        if get_type(transList[i])==t_type:
            del transList[i]
        else:
            i=i+1




'''

REPLACE COMMAND

'''
def replace(transList,day,t_type,description,value,undoList):
    '''
    Replaces a certain transaction's value with another value given by the user
    Input: transList- the list of the transactions, day, value-integers representing the day and the value of the transaction whose value has to be replaced, t_type, description- strings representing the type and the description of the transaction
    Ouput: -
    '''
    undoList.append(copy_list(transList))
    for i in range (0,len(transList)):
        if get_day(transList[i])==day and get_type(transList[i])==t_type and get_description(transList[i])==description:
            transList[i]["value"]=value
    


def sort_day(transList):
    for i in range (0,len(transList)-1):
        for j in range(i+1,len(transList)):
            if get_day(transList[i])>get_day(transList[j]):
                       transList[i],transList[j]=transList[j],transList[i]
        

def list_type(transList,t_type):
    '''
    Prints the transactions with the specified type
    Input: transList- the list of the transactions, t_type- a string representing the type of the transaction, specified by the user 
    Output: the list with the property given
    '''
    newList=[]
    for trans in transList:
        if get_type(trans)==t_type:
            newList.append(trans)
    sort_day(newList)
    return newList

def list_value_greater(transList,value):
    '''
    Prints the transictions with the value greater than a value given by the user
    Input: transList- the list of the transactions, value- a integer representing a value given by the user
    Output: the list with the property given
    '''
    newList=[]
    for trans in transList:
        if get_value(trans)>value:
            newList.append(trans)
    sort_day(newList)
    return newList

def list_value_smaller(transList,value):
    '''
    Prints the transictions with the value smaller than a value given by the user
    Input: transList- the list of the transactions, value- a integer representing a value given by the user
    Output: the list with the property given
    '''
    newList=[]
    for trans in transList:
        if get_value(trans)<value:
            newList.append(trans)
    sort_day(newList)
    return newList

def list_value_equal(transList,value):
    '''
    Prints the transictions with the value equal to a value given by the user
    Input: transList- the list of the transactions, value- a integer representing a value given by the user
    Output: the list with the property given
    '''
    newList=[]
    for trans in transList:
        if get_value(trans)==value:
            newList.append(trans)
            #print(trans,' ')
    sort_day(newList)
    return newList

def summ(transList,t_type):
    '''
    Does the sum of all transactions of a certain type
    Input: transList- the list of transactions, t_type- a string representing the type given by the user
    Output: s- the sum of all transactions with the property given
    '''
    s=0
    for trans in transList:
        if get_type(trans)==t_type:
            s=s+get_value(trans)
    return s

def sum_before(transList,t_type,day):
    '''
    Does the sum of all transactions of a certain type until a day given
    Input: transList- the list of transactions, t_type- a string representing the type given by the user, day- an integer representing a day given by the user
    Output: s- the sum of all transactions with the property given
    '''
    s=0
    for trans in transList:
        if get_type(trans)==t_type and get_day(trans)<=day:
            s=s+get_value(trans)
    return s
    
def list_balance(transList,day):
    '''
    Does the balance on a given day (all the in transactions- all the out transactions occuring before or on the specified day)
    Input: transList- the list of the transactions, day- integer, the day given by the user
    Output: the balance on the given day
    '''
    s1=summ(transList,"in")
    s2=sum_before(transList,"out",day)
    return (s1-s2)


def maxx(transList,t_type,day):
    maxi=0
    for trans in transList:
        if get_day(trans)==day and get_type(trans)==t_type:
            if get_value(trans)>maxi:
                maxi=get_value(trans)
    return maxi


def filter_type(transList,t_type,undoList):
    undoList.append(copy_list(transList))
    i=0
    while i<len(transList):
        if get_type(transList[i])!=t_type:
            del transList[i]
        else:
            i=i+1

def filter_type_day(transList,t_type,value,undoList):
     undoList.append(copy_list(transList))
     i=0
     while i<len(transList):
        if get_type(transList[i])!=t_type:
            del transList[i]
        elif get_type(transList[i])==t_type and get_value(transList[i])>value:
            del transList[i]
        else:
            i=i+1


