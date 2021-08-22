class Iter:
    def __init__(self, lst =[]):
        self._l = lst
        self._index = 0
        
        
    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        #print(len(self._objects))
        n = self._index
        self._index = self._index + 1
        
        if n >= len(self):
            #print("da")
            raise StopIteration
        return self._l[n]
    
    def __delitem__(self,index):
        index = index + 1
        del self._l[index-1]
        return self._l
        
        
    def __setitem__(self,i,obj):
        #print(i)
        self._l[i] = obj
    
    def __len__(self):
        return len(self._l)
    
    def __getitem__(self,index):
        return self._l[index]
    
    def __index__(self):
        return self._index

    def append(self,obj):
        self._l.append(obj)