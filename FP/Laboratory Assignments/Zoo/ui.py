from operations import *

def printMenu():
    print("Press 1. to add an animal.")
    print("Press 2. to modify the type of a given animal.")
    print("Press 3. to change the type of a whole species.")
    print("Press 4. to show all animals with a given type.")
    print("Press 5. to show the list of the animals.")
    print("Press 0. to exit.")

def startapp():
    print("Welcome to our ZOO!")
    print("Press * to show the menu!")
    ok=1
    animalsList=[]
    set_up(animalsList)
    while ok==1:
        #printMenu()
        n=input()
        if n == "*":
            printMenu()
        else:
            try:
                n=int(n)
                if n==1:
                    print("Enter the animal's code: ")
                    code = input()
                    print("Enter the animal's name: ")
                    name = input()
                    print("Enter the animal's type: ")
                    a_type = input()
                    print("Enter the animal's species: ")
                    species = input()
                    try:
                        add(code,name,a_type,species,animalsList)
                    except ValueError as ve:
                        print(ve)
                   
                elif n==2:
                    print("Enter the animal's code: ")
                    code = input()
                    print("Enter the animal's new type: ")
                    new_type = input()
                    modify_type(code, new_type, animalsList)
                    
                elif n==3:
                    print("Enter the animal's species: ")
                    species = input()
                    print("Enter the animal's new type: ")
                    new_type = input()
                    try: 
                        modify_species_type(species, new_type, animalsList)
                    except ValueError as ve:
                        print(ve)
                    
                elif n==4:
                    print("Enter the type: ")
                    a_type=input()
                    newList=show_animals(a_type, animalsList)
                    print_list(newList)
                    
                elif n==5:
                    print_list(animalsList)
                elif n==0:
                    ok=0
            except ValueError:
                print("Invalid command!")
    print("Thank you!")
startapp()