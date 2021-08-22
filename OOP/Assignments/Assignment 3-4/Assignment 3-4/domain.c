#include "domain.h"
#include <string.h>

Offer *create(char *type, char*address, int surface, int price)
{
	/*
	Creates an offer
	Input: type, address (character strings), surface,price (integers)
	Output: returns the offer just created
	*/


	
	Offer *new_offer = (Offer*)malloc(sizeof(Offer));

	new_offer->type = (char*)malloc(sizeof(char) * (strlen(type) + 1));
	strcpy_s(new_offer->type, strlen(type)+1, type);



	new_offer->address = (char*)malloc(sizeof(char) * (strlen(address) + 1));
	strcpy_s(new_offer->address, strlen(address)+1,address);

	new_offer->surface= surface;
	new_offer->price = price;

	return new_offer;
}
