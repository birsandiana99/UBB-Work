# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 15:48:58 2019

@author: Zsu
"""


class Bag:

    # creates a new, empty Bag
    def __init__(self):
        #theta(1)
        self.__elements = []
        self.__frequences = []
        

    # adds a new element to the Bag
    def add(self, e):
        #O(n)
        if e in self.__elements:
            idx = self.__elements.index(e)
            self.__frequences[idx]+=1
        else:
            self.__elements.append(e)
            self.__frequences.append(1)

    # removes one occurrence of an element from a Bag
    # returns True if an element was actually removed (the Bag contained the element e), or False if nothing was removed
    def remove(self, e):
        #O(n)
        if e not in self.__elements:
            return False
        idx = self.__elements.index(e)
        if self.__frequences[idx]>1:
            self.__frequences[idx]-=1
        else:
            self.__frequences.pop(idx)
            self.__elements.pop(idx)
            
        return True
    # searches for an element e in the Bag
    # returns True if the Bag contains the element, False otherwise
    def search(self, e):
        #O(n)
        if e in self.__elements:
            return True
        return False

    # counts and returns the number of times the element e appears in the bag
    def nrOccurrences(self, e):
        #O(n)
        if e in self.__elements:
            idx = self.__elements.index(e)
            return self.__frequences[idx]
        return 0
        

    # returns the size of the Bag (the number of elements)
    def size(self):
        #Theta(n)
        s = 0
        for f in self.__frequences:
            s+= f
        return s

    # returns True if the Bag is empty, False otherwise
    def isEmpty(self):
        #theta(n)
        return self.size() == 0

    # returns a BagIterator for the Bag
    def iterator(self):
        #theta(1)
        return BagIterator(self)


class BagIterator:

    #creates an iterator for the Bag b, set to the first element of the bag, or invalid if the Bag is empty
    def __init__(self, b):
        #theta(1)
        self.__bag = b
        self.__currentElement = 0
        self.__currentFrequence = 0

    # returns True if the iterator is valid
    def valid(self):
        #O(1)
        if self.__currentElement<len(self.__bag._Bag__elements):
            return True
        return False

    # returns the current element from the iterator.
    # throws ValueError if the iterator is not valid
    def getCurrent(self):
        #theta(1)
        if self.valid()==True:
            return self.__bag._Bag__elements[self.__currentElement]
        else:
            raise ValueError
    # moves the iterator to the next element
    #throws ValueError if the iterator is not valid
    def next(self):
        #O(1)
        if not self.valid():
            raise ValueError
        self.__currentFrequence += 1
        if self.__currentFrequence == self.__bag._Bag__frequences[self.__currentElement]:
            self.__currentElement += 1
            self.__currentFrequence = 0
        

    # sets the iterator to the first element from the Bag
    def first(self):
        #O(1)
        self.__currentElement = 0
        self.__currentFrequence = 0