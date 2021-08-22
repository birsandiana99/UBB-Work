#pragma once
#include "Dog.h"

//typedef Dog TElem;
using namespace std;
template <class T>

class DynamicVector
{
public:
	//constructor
	DynamicVector(int capacity = 10);

	//copy constr
	DynamicVector(const DynamicVector& vector);

	//destructor
	~DynamicVector();

	//assignment operator
	DynamicVector& operator=(const DynamicVector& vector);

	DynamicVector& operator+(T& elem);

	DynamicVector& operator+(DynamicVector& dv);

	

	//TElem& operator[](int pos);

	void add(T e);
	T& operator[](int pos);

	int getSize() const;
	int getCap() const;

	int searchElem(string name);
	void deleteElem(int index);
	T * getArray();
	void updateElem(int index, string new_name, string breed, int age, string pic);

private:
	void resize(int f = 2);
	T* elems;
	int size;
	int capacity;
	
};
template <class T>
DynamicVector<T>& operator+(T& elem, DynamicVector<T>& dv);

template <class T>
int DynamicVector<T>::getCap() const {
	return this->capacity;
}


template <class T>
DynamicVector<T>::DynamicVector(int capacity) {
	this->size = 0;
	this->capacity = capacity;
	this->elems = new T[capacity];
}


template <class T>
DynamicVector<T>::DynamicVector(const DynamicVector& vector) {
	this->size = vector.size;
	this->capacity = vector.capacity;
	this->elems = new T[this->capacity];
	for (int i = 0; i < this->size; i++)
		this->elems[i] = vector.elems[i];
}

template <class T>
DynamicVector<T>::~DynamicVector() {
	delete[] this->elems;
}


template <class T>
DynamicVector<T>& DynamicVector<T>::operator=(const DynamicVector& vector) {
	if (this == &vector)
		return *this;

	this->size = vector.size;
	this->capacity = vector.capacity;

	delete[] this->elems;
	this->elems = new T[this->capacity];
	for (int i = 0; i < this->size; i++)
		this->elems[i] = vector.elems[i];
	return *this;
}


template <class T>
DynamicVector<T>& DynamicVector<T>::operator+(DynamicVector& dv) {
	int k = 0;
	int n = dv.getSize();
	for (; k <= n; k++)
	{
		this->add(dv.getArray()[k++]);
	}
	return *this;
}



template <class T>
void DynamicVector<T>::add(T e) {
	if (this->size == this->capacity)
		this->resize();
	this->elems[this->size] = e;
	this->size++;
}

template <class T>
void DynamicVector<T>::resize(int f) {
	this->capacity *= f;
	T* elements = new T[this->capacity];
	for (int i = 0; i < this->size; i++)
		elements[i] = this->elems[i];

	delete[] this->elems;
	elems = elements;
}

template <class T>
T& DynamicVector<T>::operator[](int pos) {
	return this->elems[pos];
}

template <class T>
int DynamicVector<T>::getSize() const {
	return this->size;
}

template <class T>
int DynamicVector<T>::searchElem(string name) {
	for (int i = 0; i <= this->size; ++i) {
		if (this->elems[i].getName() == name) {
			return i;
		}
	}
	return -1;
}


template <class T>
void DynamicVector<T>::deleteElem(int index) {
	for (; index < this->size - 1; ++index) {
		this->elems[index] = this->elems[index + 1];
	}

	this->size = this->size - 1;
}


template <class T>
void DynamicVector<T>::updateElem(int index, string new_name, string breed, int age, string photo) {
	this->elems[index].setBreed(breed);
	this->elems[index].setName(new_name);
	this->elems[index].setAge(age);
	this->elems[index].setPhoto(photo);
}

template <class T>
T * DynamicVector<T>::getArray()
{
	return elems;
}

template<class T>
inline DynamicVector<T>& operator+(T & elem, DynamicVector<T>& dv)
{
	dv.add(elem);

	return dv;
}
