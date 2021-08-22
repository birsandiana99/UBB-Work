'''
Dyanmic Programming

1. overlapping subproblems
2. memoization 
'''
from texttable import Texttable
from random import randint

d = {}
d[0] = 0
d[1] = 1
def f(n): # O(n)
    if n not in d.keys():
        d[n] = f(n-2) + f(n-1)
    return d[n]
    
#f(n) = f(n-2) + f(n-1)
print(f(100))

'''
0-1 knapsack problem
'''
W = 10
values = [2, 1, 3, 5, 4]
weights= [1, 2, 2, 3, 4]
#         1  2  3  4  5
# d1 -> d2 -> d3 -> d4

# n - I am on n-th item right now
def knapsack(W, values, weights, n): # O(2^n)
    if n < 0:
        return 0
    if W < weights[n]:
        return knapsack(W, values, weights, n-1)
    
    return max(knapsack(W, values, weights, n-1),values[n] + knapsack(W-weights[n], values, weights, n-1))

def prettyprint(T):
    tbl = Texttable()
    tbl.header([''] + list(range(len(T[0]))))
    for i in range(len(T)):
        tbl.add_row([i] + T[i])
    print(tbl.draw())

def knapsackDP(W, values, weights):
    n = len(values)
    T = [[0 for i in range(W+1)] for j in range(n+1)]
    
    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                T[i][j] = 0
            elif weights[i-1] > j:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = max(T[i][j], values[i-1] + T[i-1][j-weights[i-1]])
    
    prettyprint(T)
    return T[n][W]

print(knapsack(W, values, weights, len(values)-1))
print(knapsackDP(W, values, weights))


M = [[0 for i in range(8)] for j in range(8)]
for i in range(8):
    for j in range(8):
        M[i][j] = randint(0,5)
        
t = Texttable()
for row in M:
    t.add_row(row)
    
print(t.draw())

s1 = "monday"
s2 = "sunday"

# distance(s1,s2) = 2 # levenshtein
#
# s1 -> s2
# operations
#    - char replace
#    - char insert
#    - char delete

#s1[-1] -> s1[0]

# s1 -> s2
def edit(s1,s2): # O(3^min(len(s1),len(s2)))
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)
    if s1[-1] == s2[-1]:
        return 0 + edit(s1[:-1],s2[:-1])
    return 1 + min(edit(s1[:-1],s2[:-1]), edit(s1[:-1],s2), edit(s1,s2[:-1]))

print(edit("abcd","xabcdy"))

'''
n = len(s1)
m = len(s2)
T[n][m]

T[i][j] = 1+ min(T[i-1][j],T[i][j-1],T[i-1][j-1])
'''