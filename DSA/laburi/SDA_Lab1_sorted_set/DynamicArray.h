#pragma once
typedef int TElem;

#include "Iterator.h"

class DynamicArray
{
private:
	friend class DAIterator;
	int cap;
	int sizee;
	TElem* elems;
public:
	DynamicArray(int cap);
	DynamicArray();
	int size() const;
	TElem getElement(int pos) const;
	TElem setElement(int pos, TElem newElem);
	void addToEnd(TElem newElem);
	void addToPosition(int pos, TElem newElem);
	TElem remove(int pos);
	void resize();
	int search(TElem element);
	~DynamicArray();
	DAIterator iterator() const;
};



