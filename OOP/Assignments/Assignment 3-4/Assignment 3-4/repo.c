#include "repo.h"
#include <stdlib.h>

DynamicArray * initialize(int capacity)
{
	DynamicArray *dynamicVector = (DynamicArray*)malloc(sizeof(DynamicArray));

	dynamicVector->arr = (TElem*)malloc(capacity * sizeof(TElem));

	dynamicVector->size = 0;
	dynamicVector->capacity = capacity;

	return dynamicVector;
}

void destroyArray(DynamicArray* dynamicVector)
{
	/*
	Frees the memory allocated for the array
	Input: dynamicVector- a DynamicArray pointer
	Output: frees the memory allocated for the DA
	*/
	for (int i = 0; i < dynamicVector->size; i++) {
		free(dynamicVector->arr[i]->type);
		free(dynamicVector->arr[i]->address);
		free(dynamicVector->arr[i]);
	}

	if (dynamicVector != NULL)
		free(dynamicVector->arr);

	free(dynamicVector);
}

void resize(DynamicArray* dynamicVector)
{
	/*
	Enlarges the capacity of the dynamic array
	Input: dynamicVector - a DA
	Output: the capacity of the DA is doubled
	*/
	dynamicVector->capacity *= 2;
	TElem* arr2 = (TElem*)malloc(dynamicVector->capacity * sizeof(TElem));
	for (int i = 0; i < dynamicVector->size; i++)
		arr2[i] = dynamicVector->arr[i];
	free(dynamicVector->arr);
	dynamicVector->arr = arr2;
}

void add(DynamicArray* dynamicVector, TElem element)
{
	/*
	Adds an element of TElem type to the Da
	Input: dynamicVector- a DA, element- a TElem type variable (Offer in our case)
	Output: the TElem element is added to the DA
	*/
	if (dynamicVector->size >= dynamicVector->capacity)
		resize(dynamicVector);
	dynamicVector->arr[dynamicVector->size++] = element;
}

int find(DynamicArray * dynamicVector, char * address)
{
	/*
	Finds the index corresponding to a certain address
	Input: dynamicVector- a DA, address- a string
	Output: i- an integer representing the index of the element with the given address, -1 if not found
	*/
	for (int i = 0; i < dynamicVector->size; i++)
	{
		if (strcmp(dynamicVector->arr[i]->address, address) == 0)
			return i;
	}
	return -1;
}

void delete(DynamicArray * dynamicVector, char * address)
{
	/*
	Deletes an element from the DA by its address
	Input: dynamicVector - a DA, address - a string
	Output: the element is deleted from the Da
	*/
	int i = find(dynamicVector, address);
	

	int j;
	for (j=i;j<dynamicVector->size;j++)
	{
		dynamicVector->arr[j] = dynamicVector->arr[j + 1];
	}
	dynamicVector->size--;

}

void updateSurface(DynamicArray * dynamicVector, char * address,int surface)
{
	/*
	Updated the surface field of an element by its address
	Input: dynamicVector- a DA, address- a string, surface- an integer
	Output: the element with the address address will have the field <surface> replaced with the parameter surface
	*/
	int i = find(dynamicVector, address);
	dynamicVector->arr[i]->surface = surface;
}


void updatePrice(DynamicArray * dynamicVector, char * address,int price)
{
	/*
	Updated the price field of an element by its address
	Input: dynamicVector- a DA, address- a string, price- an integer
	Output: the element with the address address will have the field <price> replaced with the parameter price
	*/
	int i = find(dynamicVector, address);
	dynamicVector->arr[i]->price = price;
}

void insert(DynamicArray* list, int index, struct Offer* elem)
{
	for (int i = list->size; i > index; --i)
		list->arr[i] = list->arr[i - 1];

	list->arr[index] = elem;
	list->size = list->size + 1;
}