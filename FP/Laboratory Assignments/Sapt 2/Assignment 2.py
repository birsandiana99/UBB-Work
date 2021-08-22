def print_menu():
    print("Press 1. for adding a number")
    print("Press 2. for printing the list")
    print("Press 3. for printing the longest sequence of numbers with increasing modulus")
    print("Press 4. for printing the longest sequence of consecutive numbers with equal sum")
    print("Press 0. for exitting the program.")

def get_re(number):
    #return number[0]
    return number["Re"]

def get_im(number):
    #return number[1]
    return number["Im"]
    
def set_re(number,re):
    #number[0]=re
    number["Re"]=re
    
def set_im(number,im):
    #number[1]=im
    number["Im"]=im

def create_number(re,im):
    #return (re,im)
    return {"Re":re,"Im":im}

def add_list(re,im,num_list):
    number=create_number(re,im)
    num_list.append(number)
    
def add_ui(num_list):
    re=int(input("Enter the real part of the number: "))
    im=int(input("Enter the imaginary part of the number: "))
    add_list(re,im,num_list)
    
    
def print_list(num_list):
    for number in num_list:
     #   if get_re(number)==0:
      #      if get_im(number)==0:
       #         print("0")
        #    else:
         #       print(get_im(number),"i ")
       # elif get_im(number)==0:
        #    print(get_re(number)," ")
        #elif get_im(number)<0:
         #       print(get_im(number),get_im(number),"i ")
        #else:
            print(get_re(number),"+",get_im(number),"i ")

def list_set_up(num_list):
    num_list.append({"Re":1,"Im":3})
    num_list.append({"Re":1,"Im":-1})
    num_list.append({"Re":1,"Im":3})
    num_list.append({"Re":1,"Im":-1})
    num_list.append({"Re":2,"Im":-1})
    num_list.append({"Re":4,"Im":1})
    num_list.append({"Re":1,"Im":8})
    num_list.append({"Re":9,"Im":3})
    num_list.append({"Re":5,"Im":4})
    num_list.append({"Re":0,"Im":0})

def module(number):
    '''
    computes the modulus of a real number
    input: the real number- a tupel
    output: the modulus of the number
    '''
    return (get_re(number)**2+get_im(number)**2)**0.5

def exercise_4(num_list):
    '''
    Finds the first position and the lenght of the longest sequence of numbers with increasing modulus
    Input: num_list- a list of tupels, each represents a real number
    Output: the longest sequence of numbers with increasing modulus
    '''
    lmax=0
    lcrt=1
    m1=module(num_list[0])
    for i in range (1,len(num_list)):
        m2=module(num_list[i])
        if m1<m2:
            lcrt=lcrt+1
            if lcrt>lmax:
                lmax=lcrt
                j=i-lcrt+1
        else:
            m1=m2
            lcrt=1

    #print(lmax)
    #print(j)
    return j,lmax

def exercise_9(num_list):
    '''
    Finds the first position and the lenght of the longest sequence of numbers with equal sum
    Input: num_list- a list of tupels, each represents a real number
    Output: the longest sequence of numbers with equal sum
    '''
    lmax=0
    lcrt=2
    s_re1=get_re(num_list[0])+get_re(num_list[1])
    s_im1=get_im(num_list[0])+get_im(num_list[1])
    j=0
    ok=1
    for i in range (2,len(num_list)-1):
        s_re2=get_re(num_list[i])+get_re(num_list[i+1])
        s_im2=get_im(num_list[i])+get_im(num_list[i+1])
        if s_re1==s_re2 and s_im1==s_im2:
            lcrt=lcrt+2
            if ok==0:
                j=i
            if lcrt>lmax:
                lmax=lcrt
            ok=1
        else:
            s_re1=s_re2
            s_im1=s_im2
            ok=0
        i=i+1    

    #print(lmax)
    #print(j)
    return j,lmax

def start():
    num_list=[]
    list_set_up(num_list)
    while True:
        print_menu()
        x=int(input())
        if x==1:
            add_ui(num_list)
        elif x==2:
            print_list(num_list)
        elif x==3:
            k=exercise_4(num_list)
            j1=k[0]
            lmax1=k[1]
            for i in range (j1,j1+lmax1):
                print(get_re(num_list[i]),"+",get_im(num_list[i]),"i ")
        elif x==4:
            k=exercise_9(num_list)
            j=k[0]
            lmax=k[1]
            for i in range (j,j+lmax):
                print(get_re(num_list[i]),"+",get_im(num_list[i]),"i ")
        elif x==0:
            return
        else:
            print("Invalid command!")

start()
    

    
