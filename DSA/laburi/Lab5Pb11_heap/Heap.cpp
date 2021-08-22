#include "Heap.h"
#include <list>
#include <iostream>
#include <stdexcept>
#include <algorithm>
using namespace std;


Heap::Heap()
{

}
void swap(int *x, int *y)
{
	int *aux;
	aux = x;
	x = y;
	y = aux;

}

Heap::~Heap()
{
}


/*
void Heap::bubbleDown(int p)
{
	int poz = p;
	TElem elem = this->elems[p];
	while (poz < this->len)
	{
		int maxChild = -1;
		if (poz * 2 <= this->len)
			maxChild = poz * 2;
		if (poz * 2 + 1 <= len && this->elems[2 * poz + 1] < this->elems[2 * poz])
			maxChild = poz * 2 + 1;
		if (maxChild != -1 && this->elems[maxChild] < elem)
		{
			TElem tmp = this->elems[poz];

			this->elems[poz] = this->elems[maxChild];
			this->elems[maxChild] = tmp;
			poz = maxChild;
		}
		else
			poz = this->len + 1;
	}
}
*/
void Heap::bubbleDown(int index)
{
	int leftChild = 2 * index + 1;
	int rightChild = 2 * index + 2;
	if (leftChild >= this->len)
		return;
	int minIndex = index;

	if (*(this->elems[index]) < *(this->elems[leftChild]))
	{
		minIndex = leftChild;
	}

	if (rightChild <this->len && *(this->elems[minIndex]) < *(this->elems[rightChild]))
	{
		minIndex = rightChild;
	}
	if (minIndex != index)
	{
		T aux = this->elems[index];
		this->elems[index] = this->elems[minIndex];
		this->elems[minIndex] = aux;
		bubbleDown(minIndex);

	}
}
void Heap::OurProb(list<TElem> &listt,int n)
{

	//cout << "len: " << len<<endl<<endl<<endl<<endl<<endl;
	
	//auto maxit = listt.begin();
	

	//cout << "Iteratoarele: ";
	for (int k = 0; k < n; k++)
	{
		std::list<TElem>::iterator it = this->elems[k];
		//cout << *it;
		//it = this->elems[k];
		listt.erase(it);
		
	}

}
void Heap::printEl()
{

	cout << "len: " << len << endl << endl << endl << endl << endl;
	for (int k = 0; k < this->len; k++)
		cout << *(this->elems[k]) << " ";

	
}

void Heap::addElem(T elem)
{
	this->elems.addToEnd(elem);
	this->len = this->elems.size();
	bubbleUp(this->len-1);
}

TElem Heap::getRoot()
{
	return *(this->elems[0]);
}

void Heap::bubbleUp(int p)
{	
	//cout<<"Facem bubble up pt pozitia: " << p;
	int poz = p;
	T elem = this->elems[p];
	int parent = (p-1) / 2;
	while (poz > 0 && *(elem) > *(this->elems[parent]))
	{
		this->elems[poz] = this->elems[parent];
		poz = parent;
		parent = poz / 2;
	}
	this->elems[poz] = elem;
}

DynamicArray Heap::returnInArray()
{
	return this->elems;
}

TElem Heap::remove()
{
	if (this->len == 0)
		throw("Empty heap!");
	T deletedElem = elems[0];
	this->elems[0] = this->elems[this->len - 1];
	this->len--;
	
	bubbleDown(0);

	//bubbleUp(this->len - 1);
	return *deletedElem;

}