def largestnumber(x):
    '''
    Input: x-integer number
    Output: y- the largest number created with the same digits as x
    '''

    'we create an empy list in which we will put all the digits of x'
    l=[] 
    while x!=0:
        l.append(x%10)
        x=x//10

    'we sort the list, then reverse it so we obtain the digits in descending order'
    l.sort()
    l.reverse()

    'we use the elements of the list to create y'
    k=0
    y=0 
    while k<len(l):
        y=y*10+int(l[k])
        k=k+1
    return y

x=int(input("Give x a value: "))
print(largestnumber(x))
