#include "DLL.h"
#include <iostream>
#include <fstream>
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

int DLL::search(TElem elem)
{

	node *currentNode;
	currentNode = this->head;
	int currentIndex = 1;
	while (currentNode != NULL && currentNode->data!=elem)
	{
		currentNode = currentNode->next;
		currentIndex = currentIndex + 1;
	}
	return currentIndex;
}

int DLL::size()
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

TElem DLL::getElement(int pos)
{
	node *currentNode;
	currentNode = this->head;
	int currentIndex = 1;
	while (currentIndex <= pos)
	{
		currentNode = currentNode->next;
		currentIndex += 1;
	}
	if (currentNode == NULL)
		return -1;
	return currentNode->data;
}


int DLL::insertFirst(TElem elem)
{
	node *p;
	p = new node;
	p->data = elem;
	p->next = p->prev = NULL;
	p->next = this->head;
	this->head = p;
	return 1;
}

int DLL::insertLast(TElem elem)
{
	node *p;
	p = new node;
	p->data = elem;
	p->next = p->prev = NULL;
	p->prev = this->tail;
	if (this->head == NULL)
		{
			this->head = p;
			this->tail = p;
		}
	else
		{
			this->tail->next = p;
			this->tail = p;
		}

	return 1;
}

int DLL::insertAtPosition(TElem elem, int pos)
{
	node *p;
	p = new node;
	p->data = elem;
	p->next = p->prev = NULL;
	if (pos < 1)
		return -1;
	else if (pos == 1)
	{
		//insert first
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
			if (this->head == NULL)
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

int DLL::deleteElement(TElem elem)
{
	node *currentNode;
	currentNode = this->head;
	while (currentNode != NULL && currentNode->data != elem)
		currentNode = currentNode->next;

	node *detectedNode;
	detectedNode = currentNode;
	if (currentNode != NULL)
		if (currentNode == this->head)
		{
			//deleteFirst
			this->head = this->head->next;
			this->head->prev = NULL;

			detectedNode = this->head;

		}
		else if (currentNode == this->tail)
		{
			//deleteLast
			this->tail = currentNode->prev;
			this->tail->next = NULL;


		}
		else
		{
			currentNode->next->prev = currentNode->prev;
			currentNode->prev->next = currentNode->next;
		}
	else
		return -1;
	delete currentNode;
	return 1;
}

void DLL::printForTest()
{
	node *p = this->head;
	while (p != NULL)
	{
		cout << p->data << " ";
		p = p->next;
	}
}

void DLL::testList()
{

	DLL list = DLL();
	list.insertLast(1);
	list.insertLast(2);
	list.insertLast(3);
	list.insertLast(4);
	list.insertLast(5);
	list.insertLast(6);
	list.insertLast(7);

	list.insertAtPosition(-12, 2);
	list.insertFirst(0);
	list.insertLast(666);
	list.deleteElement(4);
	list.deleteElement(7);

	cout << list.search(5) << endl;
	list.printForTest();
	cout << endl<<"size: " << list.size();
	cout << endl << list.getElement(6);
}

DLL::~DLL()
{
	delete this->head;
	delete this->tail;
}
