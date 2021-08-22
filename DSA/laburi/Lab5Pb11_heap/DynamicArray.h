#pragma once

#include <exception>
#include <iostream>
#include <list>
#include <stdlib.h>
#include <iterator>
using namespace std;
typedef int TElem;

typedef list<int>::iterator T;

using namespace std;

class DAIterator;

class DynamicArray {
private:

	/*representation of Dynamic Array*/
	T * v;
	int n; // current size
	int capacity;


public:
	// constructor
	// throws exception if capacity is 0 or negative
	DynamicArray(int capacity = 10);

	//returns the size (number of elements) from the DynamicArray
	int size() const;

	//returns the element from a given position (indexing starts from 0)
	//throws exception if pos is not a valid position
	T getElement(int pos) const;

	//changes the element from a pozition to a different value
	//returns the old element from pozition poz
	//throws exception if pos is not a valid position
	T setElement(int pos, T newElem);

	//adds a new element to the end of the DynamicArray
	void addToEnd(T newElem);

	//adds a new element to a given position in a DynamicArray
	//throws exception if pos is not a valid position
	void addToPosition(int pos, T newElem);

	//removes an element from a given position
	//returns the removed element
	//throws exception if pos is not a valid position
	T remove(int pos);

	//returns an iterator for the DynamicArray
	inline DAIterator iterator() const;

	//destructor
	~DynamicArray();

	void runTests();
	void runExtendedTests();

	int findElem(T e);
	T & operator[](int pos);
};

