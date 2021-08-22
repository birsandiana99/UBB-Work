#include "DynamicArray.h"

DynamicArray::DynamicArray(int capacity) : capacity{ capacity }, n{ 0 }
{
	if (capacity <= 0) {
		throw exception();
	}

	//this->v = (TElem*)malloc(capacity * sizeof(TElem));
	this->v = new T[capacity];
}

DynamicArray::~DynamicArray()
{
	//free(this->v);
	//this->v = NULL;
	delete[] this->v;
}

int DynamicArray::size() const
{
	//teta(1)
	return this->n;
}

T DynamicArray::getElement(int pos) const
{
	//teta(1)
	if (pos <= n && n > 0)
		return this->v[pos];
	else
		throw exception();
}

T DynamicArray::setElement(int pos, T newElem)
{
	//teta(1)
	if (pos <= n && n > 0)
	{
		T oldElem = this->v[pos];
		this->v[pos] = newElem;
		/*
		for (int i = 0; i < this->n; ++i) {
		cout << v[i] << ' ';
		}*/

		//cout << "\n---------------\n";

		return oldElem;
	}
	else
		throw exception();
}

void DynamicArray::addToEnd(T newElem)
{
	//O(n)
	if (n == capacity)
	{
		this->capacity *= 2;
		//TElem* aux = (TElem*)realloc(this->v, this->capacity * sizeof(TElem));
		//this->v = aux;
		T* els = new T[this->capacity];
		for (int i = 0; i < this->n; i++)
			els[i] = this->v[i];

		delete[] this->v;
		v = els;
	}

	this->v[n] = newElem;
	n++;
	/*
	for (int i = 0; i < this->n; ++i) {
	cout << v[i] << ' ';
	}

	cout << "\n---------------\n";*/
}

void DynamicArray::addToPosition(int pos, T newElem)
{
	//O(n)
	if (pos <= n)
	{
		if (n == capacity)
		{
			this->capacity *= 2;
			//TElem* aux = (TElem*)realloc(this->v, this->capacity * sizeof(TElem));
			//this->v = aux;

			T* els = new T[this->capacity];
			for (int i = 0; i < this->n; i++)
				els[i] = this->v[i];

			delete[] this->v;
			v = els;
		}

		if (pos == n) {
			v[pos] = newElem;
			++n;
			/*
			for (int i = 0; i < this->n; ++i) {
			cout << v[i] << ' ';
			}

			cout << "\n---------------\n";*/

			return;

		}

		// 0 1 2 3 4 5
		// 5 1

		for (int i = n; i > pos; --i) {
			v[i] = v[i - 1];
		}

		v[pos] = newElem;
		++n;
		/*
		for (int i = 0; i < this->n; ++i) {
		cout << v[i] << ' ';
		}

		cout << "\n---------------\n";*/
	}
	else
		throw exception();
}

T DynamicArray::remove(int pos)
{
	if (pos <= n)
	{
		if (pos == n - 1) {
			--n;

			//for (int i = 0; i < this->n; ++i) {
			//	cout << v[i] << ' ';
			//}

			//cout << "\n---------------\n";

			return v[pos];
		}

		T oldElem = v[pos];

		for (int i = pos; i < n - 1; ++i) {
			v[i] = v[i + 1];
		}

		--n;

		//for (int i = 0; i < this->n; ++i) {
		//cout << v[i] << ' ';
		//}

		//cout << "\n---------------\n";

		return oldElem;
	}
	else
		throw exception();
}

int DynamicArray::findElem(T e)
{
	for (int i = 0; i < this->n; ++i)
	{
		if (v[i] == e)
			return i;
	}

	return -1;
}


T& DynamicArray::operator[](int pos) {
	return this->v[pos];
}