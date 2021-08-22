def create(code, name, type, species):
    return {"code":code,"name":name,"type":type,"species":species}

def getType(animal):
    return animal["type"]

def getName(animal):
    return animal["name"]

def getSpecies(animal):
    return animal["species"]

def getCode(animal):
    return animal["code"]


def setType(animal,new_type):
    animal["type"]=new_type
