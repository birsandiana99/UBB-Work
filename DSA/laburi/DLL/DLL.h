#pragma once
#include <iostream>


typedef int TElem;

typedef int TPriority;


typedef pair<TElem, TPriority> Element;

struct node
{
	TElem data;
	node *prev;
	node *next;
};
class DLL
{
public:
	DLL();
	bool isEmpty();
	node * getFirst();
	node * getLast();
	int search(TElem elem);
	int size();
	TElem getElement(int pos);
	int insertFirst(TElem elem);
	int insertLast(TElem elem);
	int insertAtPosition(TElem elem,int pos);
	int deleteElement(TElem elem);
	void printForTest();
	void testList();
	~DLL();

private:
	node *head;
	node *tail;
};

