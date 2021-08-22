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

