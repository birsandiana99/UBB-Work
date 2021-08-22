#include "DLL.h"
#include <iostream>
#include <fstream>
#include <stdexcept>
using namespace std;

DLL::DLL()
{
	this->head = NULL;
	this->tail = NULL;
}

bool DLL::isEmpty()
{
	return this->head == NULL;
}

node * DLL::getFirst()
{
	return this->head;
}

node * DLL::getLast()
{
	return this->tail;
}

int DLL::search(Element elem) const
{

	node *currentNode;
	currentNode = this->head;
	int currentIndex = 1;
	while (currentNode != NULL && currentNode->data!=elem)
	{
		currentNode = currentNode->next;
		currentIndex = currentIndex + 1;
	}
	//
	//if (currentNode->data != elem)
//		return -1;
	//
	return currentIndex;
}

const int DLL::size()
{
	node *currentNode;
	currentNode = this->head;
	int currentIndex = 1;
	while (currentNode != NULL)
	{
		currentNode = currentNode->next;
		currentIndex = currentIndex + 1;
	}

	return currentIndex-1;
}

Element DLL::getElement(int pos)
{
	//O(n)
	if (pos == 1)
		return this->head->data;
	else {
		node *currentNode;
		currentNode = this->head;
		int currentIndex = 1;
		while (currentIndex < pos && currentNode!=NULL)
		{
			currentNode = currentNode->next;
			currentIndex += 1;
		}
		if (currentNode == NULL)
			throw std::invalid_argument("No element at that position!");

		return currentNode->data;
	}

}


int DLL::insertFirst(Element elem)
{
	node *p;
	p = new node;
	p->data = elem;
	p->prev = NULL;
	p->next = NULL;
	this->head->prev = p;
	this->head = p;
	return 1;
}

int DLL::insertLast(Element elem)
{
	node *p;
	p = new node;
	p->data = elem;
	p->next = NULL;
	p->prev = NULL;
	//p->prev = this->tail;
	if (this->head == NULL)
		{
			this->head = p;
			this->tail = p;
		}
	else
		{
			this->tail->next = p;
			p->prev = this->tail;
			this->tail = p;
			
		}

	return 1;
}

int DLL::insertAtPosition(Element elem, int pos)
{ //O(n)
	node *p;
	p = new node;
	p->data = elem;
	p->next = p->prev = NULL;
	if (pos < 1)
		return -1;
	else if (pos == 1)
	{
		//insert first
		this->head->prev = p;
		p->next = this->head;
		this->head = p;
	}
	else
	{
		node *currentNode;
		currentNode = this->head;
		int currentIndex = 1;
		while (currentNode != NULL && currentIndex < pos - 1)
		{
			currentNode = currentNode->next;
			currentIndex = currentIndex + 1;
		}
		if (currentNode == NULL)
			return -1;
		else if (currentNode == this->tail)
		{
			//insert last
			p->prev = this->tail;
			if (this->head == NULL) //-
			{
				this->head = p;
				this->tail = p;
			}
			else
			{
				this->tail->next = p;
				this->tail = p;
			}
		}
		else
		{
			p->next = currentNode->next;
			p->prev = currentNode;
			currentNode->next->prev = p;
			currentNode->next = p;
		}
	}
	return 1;
}

int DLL::deleteElement(Element elem)
{
	node *currentNode;
	currentNode = this->head;
	while (currentNode != NULL && currentNode->data != elem)
		currentNode = currentNode->next;

	node *detectedNode;
	detectedNode = currentNode;
	if (currentNode != NULL)
	{
		if (detectedNode == this->head)
		{
			//deleteFirst
			this->head = this->head->next;
			this->head->prev = NULL;

			//detectedNode = this->head;

		}
		else if (currentNode == this->tail)
		{
			//deleteLast
			
			this->tail = currentNode->prev;
			this->tail->next = NULL;
			this->tail->prev = currentNode->prev->prev;
		}
		else
		{
			

			currentNode->next->prev = currentNode->prev;
			currentNode->prev->next = currentNode->next;

		}
	}
	else
		return -1;
	//delete detectedNode;
	return 1;
}

void DLL::deleteFirst()
{
	if (this->head == this->tail)
		this->head = this->tail = NULL;
	else{
		node *p = this->head->next;
		p->prev = NULL;
		this->head = p;
		//this->head = this->head->next;
		//this->head->prev = NULL;
	}
}

void DLL::printForTest()
{
	node *p = this->head;
	while (p != NULL)
	{
		cout << "("<<p->data.first<<", "<<p->data.second<<") ";
		p = p->next;
	}
}

void DLL::testList()
{

	DLL list = DLL();
	list.insertLast(Element(2, 4));
	list.insertLast(Element(2,3));
	list.insertLast(Element(-2, -3));
	list.insertLast(Element(12, 13));
	list.insertLast(Element(22, 23));
	list.insertLast(Element(22, 53));
	list.insertLast(Element(1, 3));
	list.insertLast(Element(0, 0));
	list.insertLast(Element(-1, -1));
	list.insertLast(Element(12, 13));

	list.insertAtPosition(Element(-12,-12), 2);
//	list.insertFirst(Element(0,-999));
	list.insertLast(Element(666,666));
	
	list.printForTest();
	cout << endl;
	list.deleteElement(Element(12,13));
	
	list.deleteElement(Element(666,666));
	list.deleteElement(Element(2, 4));
	//cout << endl << "size: " << list.size();
	//cout << list.search(Element(666,666)) << endl;
	list.printForTest();
	cout << "for 666,666: ";
	cout << list.search(Element(666, 666));
	cout << "for (0,0): "; cout << list.search(Element(0, 0));
	//cout << endl<<"size: " << list.size();
	//cout << endl <<"("<<list.getElement(6).first<<", "<<list.getElement(6).second<<")";
}

int DLL::Size() const
{
	node *currentNode;
	currentNode = this->head;
	int currentIndex = 1;
	while (currentNode != NULL)
	{
		currentNode = currentNode->next;
		currentIndex = currentIndex + 1;
	}

	return currentIndex - 1;
}

DLL::~DLL()
{
	//delete this->head;
	//delete this->tail;
}
