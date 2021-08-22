from operations import *
from pip._vendor.msgpack.fallback import newlist_hint

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


def printMenu():
    print(">>> add <value> <type> <description>")
    print(">>> insert <day> <value> <type> <description>")
    print(">>> remove <day>")
    print(">>> remove <start day> to <end day>")
    print(">>> remove <type>")
    print(">>> replace <day> <type> <description> with <value>")
    print(">>> list")
    print(">>> list <type>")
    print(">>> list [ < | = | > ] <value>")
    print(">>> list balance <day>")
    print(">>> sum <type>")
    print(">>> max <type> <day>")
    print(">>> filter <type>")
    print(">>> filter <type> <value>")
    print(">>> undo")
    print(">>> exit for exiting the programm")

def toString(trans):
    return ("day:"+str(get_day(trans))+" value:"+ str(get_value(trans))+ " type:"+get_type(trans)+ " description:"+get_description(trans))

def printt(transList):
    for trans in transList:
        print(toString(trans))
    
def insert_ui(transList,param,undoList):
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

def listt(transList):
    printt(transList)

def list_ui(transList,param):
    if len(param)>2:
        print("Invalid command")
    elif len(param)==0:
        listt(transList)
    elif len(param)==1:
        if param[0]!='in' and param[0]!='out':
            print("Invalid command")
        else:
            newList=list_type(transList,param[0])
            sort_day(newList)
            printt(newList)
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
                newList=list_value_greater(transList,param[1])
                sort_day(newList)
                printt(newList)
            except ValueError:
                print("Invalid command")
                
        elif param[0]=="<":
            try:
                param[1]=int(param[1])
                newList=list_value_smaller(transList,param[1])
                sort_day(newList)
                printt(newList)
            except ValueError:
                print("Invalid command")

        elif param[0]=="=":
            try:
                param[1]=int(param[1])
                newList=list_value_equal(transList,param[1])
                sort_day(newList)
                printt(newList)
            except ValueError:
                print("Invalid command")
        else:
            print("Invalid command")

def sum_ui(transList,param):
    if len(param)>1:
        print("Invalid command.")
    elif param[0]=="in" or param[0]=="out":
            print(summ(transList,param[0]))
    else:
        print("Invalid command.")

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

def filter_ui(transList,param,undoList):
    #undoList.append(copy_list(transList))
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
    
