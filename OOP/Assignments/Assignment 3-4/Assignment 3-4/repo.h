#pragma once
#include "domain.h"

typedef struct Offer *TElem;

typedef struct DynamicArray
{
	TElem *arr;
	int size, capacity;

}DynamicArray;

DynamicArray * initialize(int capacity);
void destroyArray(DynamicArray* );


void resize(DynamicArray* arr);

void add(DynamicArray* arr, TElem t);

int find(DynamicArray* arr, char * address);

void delete(DynamicArray * dynamicVector, char  *address);

void updateSurface(DynamicArray * dynamicVector, char * address,int surface);


void updatePrice(DynamicArray * dynamicVector, char *address, int price);

void insert(DynamicArray * list, int index, Offer * elem);
