//#include "stdafx.h"
#include "DynamicArray.h"
#include <stdexcept>
#include "stdafx.h"


DynamicArray::DynamicArray(int cap)
{
	/*
	Theta(1)
	*/
	if (cap <= 0) {
		throw std::invalid_argument("Capacity must be positive");
	}
	this->cap = cap;
	this->sizee = 0;
	this->elems = new TElem[this->cap];
}

DynamicArray::DynamicArray()
{

}

int DynamicArray::size() const
{
	/*
	Theta(1)
	*/
	return this->sizee;
}

TElem DynamicArray::getElement(int pos) const
{
	/*
	Theta(1)
	*/
	if (pos < 0 || pos >= this->sizee) {
		throw std::invalid_argument("Invalid position");
	}
	return this->elems[pos];
}

TElem DynamicArray::setElement(int pos, TElem newElem)
{
	/*
	O(1)
	*/
	if (pos < 0 || pos >= this->sizee) {
		throw std::invalid_argument("Invalid position");
	}
	auto result = this->elems[pos];
	this->elems[pos] = newElem;
	return result;
}

void DynamicArray::addToEnd(TElem newElem)
{
	/*
	
	*/
	resize();
	this->elems[this->sizee++] = newElem;
}

void DynamicArray::addToPosition(int pos, TElem newElem)
{
	/*
	O(n)
	*/
	if (pos >= 0 && pos <= this->sizee) {
		resize(); //O(n)
		this->sizee++;
		for (int i = this->sizee - 1; i > pos; i--) {
			this->elems[i] = this->elems[i - 1];
		}
		this->elems[pos] = newElem;
	}
	else {
		throw std::invalid_argument("Invalid position");
	}

}

TElem DynamicArray::remove(int pos)
{
	/*
	O(n)
	*/
	if (pos < 0 || pos >= this->sizee) {
		throw std::invalid_argument("Invalid position");
	}
	auto result = this->elems[pos];
	for (; pos < this->sizee - 1; ++pos) {
		this->elems[pos] = this->elems[pos + 1];
	}
	this->elems[sizee - 1]=-99999;
	this->sizee--;
	return result;
}

void DynamicArray::resize()
{
	/*
	O(n)
	*/
	if (this->sizee == this->cap) {
		TElem* copy = new TElem[this->cap * 2];
		for (int i = 0; i <this->sizee; i++) {
			copy[i] = this->elems[i];
		}
		delete[] this->elems;
		this->elems = copy;
		this->cap *= 2;
	}
}

int DynamicArray::search(TElem element)
{
	/*
	O(n)
	*/
	for (int i = 0; i <= this->sizee; i++) {
		if (this->elems[i] == element)
			return i;
	}
	return -1;
	
}

DAIterator DynamicArray::iterator() const
{
	/*
	
	*/
	return DAIterator(*this);
}


DynamicArray::~DynamicArray()
{
	/*
	O(n)
	*/
	delete[] this->elems;
}
