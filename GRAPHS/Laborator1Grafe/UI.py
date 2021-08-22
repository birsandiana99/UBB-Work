l = [1,2,3,4,5]
print(len(l))
for i in range(0,len(l)-1):
    print(i)
    if l[i] == 3:
        l.pop(i)
        
print(l)