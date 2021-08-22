#pragma once
#include <stdio.h>
#include <stdlib.h>
using namespace std;
#include <iostream> 
#include <utility> 
#include "DLL.h"

typedef int TElem;

typedef int TPriority;


typedef pair<TElem, TPriority> Element;


typedef bool(*Relation)(TPriority p1, TPriority p2);



class PriorityQueue {

private:

	//representation of PriorityQueue
	Relation relation;
	DLL dll;

public:

	//implicit constructor

	PriorityQueue(Relation r);



	//adds an element with priority to the queue

	void push(TElem e, TPriority p);



	//returns the element with the highest priority with respect to the order relation

	//throws exception if the queue is empty

	Element top();



	//removes and returns the element with the highest priority

	//throws exception if the queue is empty

	Element pop();



	//checks if the queue is empty

	bool isEmpty();


	int size();

	bool search(Element elem) const;


	//destructor

	~PriorityQueue();



};