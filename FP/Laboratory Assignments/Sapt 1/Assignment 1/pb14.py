def prim(x):
    '''
    Input: x-integer number
    Output: sem (0 if the number is not prime, 1 if the number is prime)
    Determines if the number given is prime or not by verifying if it has any divisors other than itself
    '''
    sem=1
    if x==1 or x%2==0:
        sem=0
    else:
        if x==2:
            sem=1
        else:
            for i in range(3,x//2):
                if x%i==0:
                    sem=0
    return sem
            
def nelement(n):
    '''
    Input: n- integer which represent the position
    Output: i- the element
    '''
    s=0
    '''
    s- a counter of the numbers 
    '''
    if n==1 or n==2 or n==3:
       return n
    else:
        ok=0
        s=3
        x=4
        aux=x
        while s<=n:
            '''
            if the number is prime we increase the counter, otherwise we decompose it in prime factors, adding the factor to the counter everytime it is the case
            '''
            if prim(x)==1:
                s=s+1
                if s==n:
                    return(x)
                
            else:
                for i in range(2,x):
                    if(x%i==0):
                        
                        while x%i==0:
                            x=x//i
                        s=s+i
                    '''
                    if the counter equals n or is greater than n and less than n+i it means we have reached the position
                    (because there can be the case in which we need the value 3 and the position is on the second 3)
                    '''
                    if s==n or (s-i<=n and s>=n):
                        return(i)          
            '''
            we use an integer named aux so after we decompose the number in prime factors we can increase it by 1 without problems
            '''
            x=aux+1
            aux=x
x=int(input('Give me the position: '))
print(nelement(x))
