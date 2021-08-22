#pragma once
#include <list>
#include <iostream>
#include "DynamicArray.h"
#include<iterator> 

using namespace std;


class Heap
{
public:
	Heap();
	~Heap();
	TElem remove();
	void bubbleDown(int p);
	//list<TElem> returnInList(list<TElem> l);
	void printEl();
	void heapify(int i);
	// to get index of left child of node at index i 
	int left(int i) { return (2 * i + 1); }

	// to get index of right child of node at index i 
	int right(int i) { return (2 * i + 2); }
	void OurProb(list<TElem> &listt, int n);
	void addElem(T elem);
	TElem getRoot();
	void bubbleUp(int p);
	DynamicArray returnInArray();
 private:
	int cap;
	int len;
	//std::list<TElem>::iterator elems;
	DynamicArray elems;
};

