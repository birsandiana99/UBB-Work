def prim(x):
    '''
    Input: x-integer number
    Output: sem (0 if the number is not prime, 1 if the number is prime)
    Determines if the number given is prime or not by verifying if it has any divisors other than itself
    '''
    sem=1
    'special case if the value given is 1 or is a multiple of 2'
    if x==1 or x%2==0: 
        sem=0
    else:
        'special case if the number is 2'
        if x==2: 
            sem=1
        else:
            for i in range(3,x//2):
                if x%i==0:
                    sem=0
        return sem
def twin_Numbers(x):
    '''
    Input: x- interger number
    The subprogram prints the closest prime numbers to x, which satisfy the condition q-p=2
    First we give p the immediate next value to x and q the value p+2 and verify if they are both prime
    '''
    p=x+1 
    q=p+2
    'if they are not in the first case, we continue increasing p with 1 and q with 2 until we find the closest 2 twin prime numbers to x and print them'
    if prim(p)==1 and prim(q)==1:
        return p
    
    else: 
        p=p+1
        q=p+2
        ok=0
        while ok==0:
            if prim(p)==1 and prim(q)==1:
                return p
                ok=1
            else:
                p=p+1
                q=p+2

def ui_twin():
    x=0
    while x!=-1:
        x=int(input("Give me the number: "))
        if x!=-1:
            p=twin_Numbers(x)
            q=p+2
            print(p,' ',q)

ui_twin()

        
                
    
