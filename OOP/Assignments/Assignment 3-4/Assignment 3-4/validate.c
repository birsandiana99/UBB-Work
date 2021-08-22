#include "validate.h"


int validateOffer(char * address, char * type, int surface, int price)
{
	/*	
		Validates a certain offer, by its parameters
		Input: type, address (character strings), surface,price (integers)
		Output: 1 if the offer is valid, 0 otherwise
	*/

	if (strlen(address) <= 0)
		return 0;
	if( strcmp(type, "house") != 0 && strcmp(type, "penthouse") != 0 && strcmp(type, "apartment") != 0)
		return 0;
	if(surface <= 0 )
		return 0;
	if(price <= 0)
		return 0;
	return 1;

}
int validateSurface(int surface)
{
	/*
	Validates the surface 
	Input: surface- an integer
	Output: 1 if it is valid, -1 otherwise
	
	*/
	if (surface <= 0)
		return -1;
	return 1;
}
int validatePrice(int price)
{
	/*
	Validates the price
	Input: price- an integer
	Output: 1 if it is valid, -1 otherwise

	*/
	if (price <= 0)
		return -1;
	return 1;
}
int validateAddress(char *address)
{
	/*
	Validates the address
	Input: address- a string
	Output: 1 if it is valid, -1 otherwise

	*/

	if (strlen(address) <= 0)
		return -1;
	return 1;
}

int validateType(char *type)
{

	/*
	Validates the type
	Input: type- a string
	Output: 1 if it is valid, -1 otherwise

	*/
	if (strcmp(type, "house") != 0 && strcmp(type, "penthouse") != 0 && strcmp(type, "apartment") != 0)
		return -1;
	return 1;
}
