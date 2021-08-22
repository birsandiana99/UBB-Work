def read_list(l):
    a=-1
    b=-1
    sem=0
    while sem!=1:
        a=int(input("Give me the real part "))
        b=int(input("Give me the immaginary part "))
        if a!=0 or b!=0:
            l.append(a)
            l.append(b)
        else:
            sem=1
       

def print_list(l):
    i=0
    while i<len(l):
        if l[i]==0:
             print(l[i+1],'i',' ')
        else:        
            if l[i+1]==0:
                print(l[i],' ')
            else:
                print(l[i],'+',l[i+1],'i',' ')
        i=i+2
    
    
def list_read_print():
    l=[]
    read_list(l)
    print_list(l)

list_read_print()
    
