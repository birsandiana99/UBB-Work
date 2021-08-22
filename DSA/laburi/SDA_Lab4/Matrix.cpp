#include "Matrix.h"
#include <iostream>
#include <stdexcept>
using namespace std;

TElem Matrix::modify(int i, int j, TElem e)
{
	//O(n)
	if (i<0 || i>this->lines - 1 || j<0 || j>this->lines - 1)
		//exception
		throw std::invalid_argument("i and j invalid!");
		
	TElem oldElem = this->find(i,j);
	this->modifyElem(i, j, e);
	return oldElem;
}

MatrixIterator Matrix::iteratorCol(int col) const
{
	//T(1)
	return MatrixIterator(col,*this);
}

Matrix::~Matrix()
{
	delete[] elems;
	delete[] next;
}



Matrix::Matrix(int nrLines, int nrCols)
{
	//O(n)
	if (nrLines <= 0 || nrCols <= 0)
		//exception
		throw std::invalid_argument("nrcols and nrlines must be >0");
	this->lines = nrLines;
	this->cols = nrCols;
	this->cap = nrLines * nrCols;
	elems = new triple[this->cap];
	next = new int[this->cap];
	this->head = -1;
	for (int i = 0; i <= this->cap - 1; i++)
	{
		this->next[i] = i + 1;
	}
	this->next[this->cap - 1] = -1;
	this->firstEmpty = 0;
}




void Matrix::resize()
{
	//Theta(n)
	triple* newElems = new triple[this->cap * 2];
	int* newNext = new int[this->cap * 2];

	for (int i = 0; i < this->cap; i++)
	{
		newElems[i] = this->elems[i];
		newNext[i] = this->next[i];
	}


	for (int i = this->cap; i < this->cap * 2 - 1; i++)
	{
		newNext[i] = i + 1;
	}
	newNext[this->cap * 2 - 1] = -1;


	delete[] this->elems;
	delete[] this->next;

	this->elems = newElems;
	this->next = newNext;
	this->firstEmpty = this->cap-1; 
	this->cap *= 2;
}

int Matrix::insertAtPosition(triple elem, int pos)
{
	//O(n)
	if (pos < 0)
		return -1;
	if (this->firstEmpty == -1)
		this->resize();

	if (pos == 0)
	{
		int newPosition = this->firstEmpty;
		this->elems[newPosition] = elem;
		this->firstEmpty = this->next[this->firstEmpty];
		this->next[newPosition] = this->head;
		this->head = newPosition;
	}
	else
		//if (pos > this->cap)
		//	this->resize();
		//else
		{
			int pozCurrent = 0;
			int nodCurrent = this->head;
			while (nodCurrent != -1 && pozCurrent < pos - 1)
			{
				pozCurrent = pozCurrent + 1;
				nodCurrent = this->next[nodCurrent];
			}
			if (nodCurrent != -1)
			{
				int newElem = this->firstEmpty;
				this->firstEmpty = this->next[firstEmpty];
				this->elems[newElem] = elem;
				this->next[newElem] = this->next[nodCurrent];
				this->next[nodCurrent] = newElem;
			}
			else
				return -1;
		}
}

TElem Matrix::find(int i, int j) const
{
	//O(n)
	/*for (int k = 0; k < this->cap; k++)
	{
		if (this->elems[k].i == i and this->elems[k].j == j)
			return this->elems[k].value;
	}
	return 0;
	*/

	//if (this->firstEmpty() == -1)
	//	return this->head;

	/*int k = this->head;
	//if (this->elems[k].value == -1 || k==-1)
	if(k<0)
		return 0;
	else
	while (this->elems[k].i != i && this->elems[k].j != j && k!=-1)
	{
		k = this->next[k];
	}
	
	return this->elems[k].value;*/
	//cout << "i:" << i << "   j:" << j<<endl;
	int k = this->head;
//	cout << "k:"<<k<<"elems[k]: " << this->elems[k].value<<endl;
	if (k == -1)
		return 0;

	while (k != -1)
	{
		if (this->elems[k].i == i && this->elems[k].j == j)
			return this->elems[k].value;
		k = this->next[k];
	}
	return 0;

	




}

void Matrix::modifyElem(int i, int j, TElem newElem)
{
	//O(n)
	// old elem = 0, newElem=0 - > nimic
	if (this->find(i, j) == 0 && newElem==0)
		return;
	// old elem = 0, newElem!=0 - > add
	if (this->find(i, j) == 0 && newElem != 0)
	{
		triple t;
		t.i = i;
		t.j = j;
		t.value = newElem;
		this->insertAtPosition(t, this->firstEmpty);
		return;
	}
		
	// old elem != 0, newElem=0 - > delete
	if (this->find(i, j) != 0 && newElem == 0)
	{
		this->remove(i, j);
		return;
	}

	
	//old elem != 0, newElem!=0 - > update
	if (this->find(i, j) == 0 && newElem != 0)
	{
		this->update(i, j, newElem);
	}
}

int Matrix::remove(int i, int j)
{
	//O(n)

	int nodCurrent = this->head;
	int prevNode = -1;

	while (nodCurrent != -1 && this->elems[nodCurrent].i != i && this->elems[nodCurrent].j != j)
	{
		prevNode = nodCurrent;
		nodCurrent = this->next[nodCurrent];
	}
	if (nodCurrent != -1) {
		if (nodCurrent == this->head)
			this->head = this->next[this->head];
		else
			this->next[prevNode] = this->next[nodCurrent];


		this->next[nodCurrent] = this->firstEmpty;
		this->firstEmpty = nodCurrent;
		
		//
		this->update(i, j, 0);
		//

		return 1;
	}
	else
		return -1;
	
}

void Matrix::update(int i, int j, TElem newValue)
{
	//O(n)
	//for (int k = 0; k < this->cap; k++)
//	{
	//	if (this->elems[k].i == i and this->elems[k].j == j)
		//	this->elems[k].value = newValue;
//	}


	int k = this->head;
	//	cout << "k:"<<k<<"elems[k]: " << this->elems[k].value<<endl;
	if (k == -1)
		return;

	while (k != -1)
	{
		if (this->elems[k].i == i && this->elems[k].j == j)
			this->elems[k].value = newValue;
		k = this->next[k];
	}
}


int Matrix::nrLines() const
{
	//Theta(1)
	return this->lines;
}

int Matrix::nrColumns() const
{
	//Theta(1)
	return this->cols;
}

TElem Matrix::element(int i, int j) const
{
	//O(n)
	if (i<0 || i>this->lines - 1 || j<0 || j>this->lines - 1)
		//exception
		throw std::invalid_argument("i or j invalid");


//	cout <<"in function::"<< this->find(i, j);
	return this->find(i,j);
}
