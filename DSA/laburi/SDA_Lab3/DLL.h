#pragma once
#include <iostream>


typedef int TElem;

typedef int TPriority;


typedef std::pair<TElem, TPriority> Element;

struct node
{
	Element data;
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
	int search(Element elem) const;
	const int size();
	Element getElement(int pos);
	int insertFirst(Element elem);
	int insertLast(Element elem);
	int insertAtPosition(Element elem,int pos);
	int deleteElement(Element elem);
	void deleteFirst();
	void printForTest();
	void testList();
	int Size() const;
	//bool booleanSearch(Element elem) const;
	~DLL();

private:
	node *head;
	node *tail;
};

