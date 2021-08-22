'''
    D&C: Determine the smallest number in a list
    
    Divide: divide list into halves
    Conquer: find the smallest number in each half
    Combine: compare the 2 minimums 
    
'''

def minList(data):
    '''
    Returns the smallest element in list data
    :input data - the input list
    :output the smallest element in data
    '''
    if len(data) == 1:
        return data[0]
    
    m = len(data) // 2
    m1 = minList(data[:m])
    m2 = minList(data[m:])
    
    return min(m1,m2)

'''
    D&C: Determine the smallest number in a list
    
    Divide: divide list into the first element and the rest of the list
    Conquer: find the minimum in the rest of the list
    Combine: compare the 2 minimums 
    
'''

def minListChipConquer(data):
    '''
    Returns the smallest element in list data
    :input data - the input list
    :output the smallest element in data
    '''
    if len(data) == 1:
        return data[0]
        
    return min(data[0],minListChipConquer(data[1:]))


d = [3, 9, 1, 6, -1, 6, 2, 2, 5, 1]
print(minList(d))
print(minListChipConquer(d))

'''
    Sum of the elements found at positions that are multiples of 3 in a list
    1 8 5 4 0 1 4 3 1 4 1
    x     x     x     x    = 13
'''
def sumOfMultiples(data):
    if len(data) == 0:
        return 0
    
    return data[0]+sumOfMultiples(data[3:])

print(sumOfMultiples(d))

'''
    Calculate the r-th root of given number n with precision p
    given: n, p ,r
    find: x
'''

def root(n, r, p):
    return rootInternal(n, r, p, 0, n)

def rootInternal(n, r, p, left, right):
    m = (left + right) / 2
    if abs(n-m**r) < p:
        return m
    
    if n < m**r:
        return rootInternal(n, r, p, left, m)
    else:
        return rootInternal(n, r, p, m, right)
    
p = 0.1
for i in range(8):
    print(root(2, 2, p), root(2, 2, p) ** 2)
    p /= 10
    
'''
    BKT
    
    1. search space representation
    2. consistent function
    3. solution
'''

def consistent(x):
    return len(x) == len(set(x))

def solution(x, n):
    return len(x) == n

def solutionFound(x, n):
    print(x)

def backtrackIterative(n):
    x = [-1]
    while len(x) > 0:
        chosen = False
        while not chosen and x[len(x) - 1] < n - 1:
            x[len(x) - 1] += 1
            chosen = consistent(x)
        if chosen:
            if solution(x, n):
                solutionFound(x, n)
            else:
                x.append(-1)
        else:
            x = x[:-1]
            
backtrackIterative(4)

from texttable import Texttable

def consistent1(x):
    if len(x) != len(set(x)):
        return False
    
    for i in range(len(x) - 1):
        if abs(x[-1] - x[i]) == len(x) - i - 1:
            return False
    return True

def solution1(x, n):
    return len(x) == n

def solutionFound1(x, n):
    t = Texttable()
    for i in x:
        row = ['' ]* n
        row[i] = 'Q'
        t.add_row(row)
        
    print(t.draw())
    print("\n")
    
def backtrackIterative1(n):
    x = [-1]
    while len(x) > 0:
        chosen = False
        while not chosen and x[len(x) - 1] < n - 1:
            x[len(x) - 1] += 1
            chosen = consistent1(x)
        if chosen:
            if solution1(x, n):
                solutionFound1(x, n)
            else:
                x.append(-1)
        else:
            x = x[:-1]

backtrackIterative1(4)

def BacktrackRecursive(x, n):
    x.append(0)
    for i in range(0, n):
        x[len(x) - 1] = i
        if consistent(x):
            pass