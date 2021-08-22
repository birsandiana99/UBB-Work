from domain import *

def searchCode(code, animalsList):
    for an in animalsList:
        if getCode(an) == code:
            return an
    return False
    
def add(code, name, a_type, species, animalsList):
    '''
    Adds a dictionary (representing an animal) to a list of dictionaries (representing a list of animals).
    Input: 4 strings: code, name, a_type, species which will represent the fields of the dictionary(in this certain order)
           A list of dictionaries (animalsList) 
    None of the strings can be void
    '''
    if code=="":
        raise ValueError("The code field cannot be void!")
    elif name=="" :
        raise ValueError("The name field cannot be void!")
    elif a_type=="": 
        raise ValueError("The type field cannot be void")
    elif species=="":
        raise ValueError("the species field cannot be void")
    elif searchCode(code,animalsList)!=False:
        raise ValueError("You cannot enter an animal with the same code twice!")
    else:
        animalsList.append(create(code, name, a_type, species))

def set_up(animalsList):
    add("11z","Zeby","herbivore","zebra",animalsList)
    add("12h","Jamal","herbivore","horse",animalsList)
    add("13r","Bunny","herbivore","rabbit",animalsList)
    add("15l","Herald","carnivore","lion",animalsList)
    add("44e","Bloody","carnivore","eagle",animalsList)
    add("45e","Bloody2","carnivore","eagle",animalsList)
    add("46e","Bloody3","carnivore","eagle",animalsList)
    add("55b","Bruno","omnivore","bear",animalsList)
    

def modify_species_type(species,new_type,animalsList):
    if new_type == "":
        raise ValueError("The new type cannot be void")
    for animal in animalsList:
        if getSpecies(animal) == species:
            setType(animal, new_type)


def modify_type(code, new_type,animalsList):
    '''
    Modifies the "type" field of a dictionary from a list of dictionaries with another string: new_type
    Input: two strings: code, new_type
           a list of dictinaries(animalsList) in which we will search using the searchCode function the disctionary having the "code" field equal to our code from the function
          
    '''
    animal=searchCode(code,animalsList)
    setType(animal,new_type)
 
def print_list(animalsList):
    for an in animalsList:
        print(an)


def test_modify():
    animalsList = []
    set_up(animalsList)
    modify_type("11z", "carnivore", animalsList)
    animal = searchCode("11z",animalsList)
    assert getType(animal) == "carnivore"
    

def sort_by_name(animalsList):
    for i in range (0,len(animalsList)-1):
        for j in range (i,len(animalsList)):
            if getName(animalsList[i])>getName(animalsList[j]):
                animalsList[i],animalsList[j]=animalsList[j],animalsList[i]
    
def test_sort():
    animalsList=[]
    set_up(animalsList)
    sort_by_name(animalsList)
    print_list(animalsList)
    
def show_animals(a_type,animalsList):
    newList = []
    for an in animalsList:
        if getType(an) == a_type:
            newList.append(an)
    sort_by_name(newList)
    
    return newList
    
def test_add():
    animalsList=[]
    add("11z","zeby","herbivore","zebra",animalsList)
    add("12z","zebyz","herbivore","zebra",animalsList)
    
    assert len(animalsList) == 2
    
    try:
        add("11z","zeby","herbivore","zebra",animalsList)
        assert False
    except ValueError:
        pass
    
    try:
        add("","","","",animalsList)
        assert False
    except ValueError:
        pass

#test_sort()
test_add()
test_modify()