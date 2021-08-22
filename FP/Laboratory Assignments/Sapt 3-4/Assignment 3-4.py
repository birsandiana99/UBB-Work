'''

GETTERS

'''

from copy import deepcopy

def get_day(trans):
    return trans["day"]

def get_value(trans):
    return int(trans["value"])

def get_type(trans):
    return trans["type"]

def get_description(trans):
    return trans["description"]



'''

SETTERS

'''
def set_day(day):
    trans["day"]=day

def set_value(value):
    trans["value"]=value

def set_type(t_type):
    trans["type"]=t_type

def set_description(description):
     trans["description"]=description


'''

Creating the transaction

'''
def create_trans(day,value,t_type,description):
    '''
    Creates a dictionary which represents a transaction
    Input: day, value- integers which will represent the day and the value of the transaction
           t_type, description- strings which will represent the type and the description of the transaction
    Output: a dictionary having the specified properties
    '''
    return {"day":day,"value":value,"type":t_type,"description":description}



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

def printMenu():
    print(">>> add <value> <type> <description> \n eg. add 100 out pizza– adds to the current day an out transaction of 100 RON with the “pizza” description.")
    print(">>> insert <day> <value> <type> <description> \n eg. insert 25 100 in salary– insert to day 25 an in transaction of 100 RON with the “salary” description.")
    print(">>> remove <day> \n eg. remove 15– remove all transactions from day 15.")
    print(">>> remove <start day> to <end day> \n eg. remove 5 to 10– removes all transactions between day 5 and day 10.")
    print(">>> remove <type> \n eg. remove in– remove all the in transactions from the current month")
    print(">>> replace <day> <type> <description> with <value> \n eg. replace 12 in salary with 2000– replace the amount for the in transaction having the “salary” description from day 12 with 2000 RON")
    print(">>> list \n eg. list – write the entire list of transactions.")
    print(">>> list <type> \n eg. list in – write all the in transactions.")
    print(">>> list [ < | = | > ] <value> \n eg. list > 100 - writes all transactions having an amount of money > 100.")
    print(">>> list balance <day> \n eg. list balance 10 – computes the account’s balance on day 10. This is the sum of all in transactions, from which we subtract out transactions occurring before or on day 10.")
    print(">>> sum <type> \n eg. sum in– write the total amount from in transactions")
    print(">>> max <type> <day> \n eg. max out 15 – write the maximum out transaction on day 15.")
    print(">>> filter <type> \n eg. filter in – keep only in transactions.")
    print(">>> filter <type> <value> \n eg. filter in 100 – keep only in transactions having an amount of money smaller than 100 RON.")
    print(">>> undo \n eg. undo – the last operation that has modified program data will be reversed. The user has to be able to undo all operations performed since program start by repeatedly calling this function.")
    print(">>> exit for exiting the programm")


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

MAIN FUNCTION

'''
    
def start():
    transList=[]
    set_up(transList)
    commands={"add":add_ui,"remove":remove_ui,"list":list_ui}
    ok=1
    undoList = []
    print("Type <help> for a list of the possible commands")
    while ok:
        user_input=readCommand()
        if user_input[0]=='exit':
            #print(transList)
            return
            ok=0
        elif user_input[0]=='help' and user_input[1]==[]:
            printMenu()
        elif user_input[0]=='add':
            add_ui(transList,user_input[1],undoList)
            
        elif user_input[0]=='insert':
            insert_ui(transList,user_input[1],undoList)
            
        elif user_input[0]=='remove':
            remove_ui(transList,user_input[1],undoList)
            
        elif user_input[0]=='replace':
            replace_ui(transList,user_input[1],undoList)
            
        elif user_input[0]=='list':
            list_ui(transList,user_input[1])

        elif user_input[0]=='sum':
            sum_ui(transList,user_input[1])

        elif user_input[0]=='max':
            max_ui(transList,user_input[1])
        elif user_input[0]=='filter':
            filter_ui(transList,user_input[1],undoList)
        elif user_input[0]=='undo':
            if user_input[1]!=[]:
                print("Invalid command")
            else:
                undo(transList,undoList)
            
        else:
            print("Invalid command")

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
    
def add_ui(transList,param,undoList):
    if len(param)!=3:
        print("Invalid syntax")
    else:
        try:
            param[0]=int(param[0])
            if param[1]!="out" and param[1]!="in":
                print("Invalid command")
            elif type(param[2])is not str:
                print("Invalid command")
            else:    
                add(transList,param[0],param[1],param[2],undoList)
        except ValueError:
            print("Invalid command.")


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
    
def insert_ui(transList,param):
    if len(param)!=4:
            print("Invalid syntax.")
    else:
        try:
            param[0]=int(param[0])
            param[1]=int(param[1])

            if param[2]!="out" and param[2]!="in":
                print("Invalid command.")
            elif type(param[3]) is not str:
                print("Invalid command.")
            else:    
                insert(transList,param[0],param[1],param[2],param[3],undoList)
        except ValueError:
            print("Invalid command.")

            

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

def remove_ui(transList,param,undoList):
    if len(param)>3:
            print("Invalid syntax.")
    elif len(param)==3:
        if param[1]!="to":
            print("Invalid command")
        else:
            try:
                param[0]=int(param[0])
                param[2]=int(param[2])
                removeBetween(transList,param[0],param[2],undoList)
            except ValueError:
                print("Invalid command.")
    elif param[0]=="in" or param[0]=="out":
        removeType(transList,param[0],undoList)
    elif len(param)==1:
        try:
            param[0]=int(param[0])
            removeDay(transList,param[0],undoList)
        except ValueError:
            print("Invalid command.")


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
    
def replace_ui(transList,param,undoList):
    if len(param)!=5:
        print("Invalid syntax")
    elif param[3]!="with" and (param[1]!="in" or param[1]!="out"):
        print("Invalid command")
    else:
        try:
            param[0]=int(param[0])
            param[4]=int(param[4])
            replace(transList,param[0],param[1],param[2],param[4],undoList)
        except ValueError:
            print("Invalid command.")



'''

LIST COMMAND

'''
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

def listt(transList):
    print(transList)

def list_ui(transList,param):
    if len(param)>2:
        print("Invalid command")
    elif len(param)==0:
        listt(transList)
    elif len(param)==1:
        if param[0]!='in' and param[0]!='out':
            print("Invalid command")
        else:
            print(list_type(transList,param[0]))
    elif len(param)==2:
        if param[0]=="balance":
            try:
                param[1]=int(param[1])
                print(list_balance(transList,param[1]))
            except ValueError:
                print("Invalid command")
                
        elif param[0]==">":
            try:
                param[1]=int(param[1])
                print(list_value_greater(transList,param[1]))
            except ValueError:
                print("Invalid command")
                
        elif param[0]=="<":
            try:
                param[1]=int(param[1])
                print(list_value_smaller(transList,param[1]))
            except ValueError:
                print("Invalid command")

        elif param[0]=="=":
            try:
                param[1]=int(param[1])
                print(list_value_equal(transList,param[1]))
            except ValueError:
                print("Invalid command")
        else:
            print("Invalid command")

'''

SUM COMMAND

'''
def sum_ui(transList,param):
    if len(param)>1:
        print("Invalid command.")
    elif param[0]=="in" or param[0]=="out":
            print(summ(transList,param[0]))
    else:
        print("Invalid command.")


'''

MAX COMMAND

'''

def maxx(transList,t_type,day):
    maxi=0
    for trans in transList:
        if get_day(trans)==day and get_type(trans)==t_type:
            if get_value(trans)>maxi:
                maxi=get_value(trans)
    return maxi

def max_ui(transList,param):
    if len(param)>2:
        print("Invalid command.")
    elif param[0]=="in" or param[0]=="out":
        try:
            param[1]=int(param[1])
            print(maxx(transList,param[0],param[1]))
        except ValueError:
            print("Invalid command")
    else:
        print("Invalid command")


'''

FILTER COMMAND


'''
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

def filter_ui(transList,param,undoList):
    undoList.append(copy_list(transList))
    if len(param)>2:
        print("Invalid command")
    elif param[0]=='in' or param[0]=='out':
        if len(param)==1:
            filter_type(transList,param[0],undoList)
        else:
            try:
                param[1]=int(param[1])
                filter_type_day(transList,param[0],param[1],undoList)
            except ValueError:
                print("Invalid command")
    else:
        print("Invalid command")
    



start()
        
    
            
