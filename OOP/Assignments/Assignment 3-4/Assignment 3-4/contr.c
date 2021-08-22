#include "contr.h"
#include "domain.h"
#include <stddef.h>
#include <string.h>
#include "validate.h"
void runController()
{
	/*
	Initialise the controller
	Input: -
	Output: -
	*/
	offers = initialize(16);
}

int addOffer(char *type, char *address, int surface, int price, int ok)
{
	/*
	Adds an offer 
	Input: type, address (character strings), surface,price (integers)
	Output: 1-if the offer was successfully added, -1 otherwise
	
	*/
	if (find(offers, address)!=-1 || validateOffer(address,type,surface,price)==0)
		return -1;

	struct Offer *offer = create(type, address, surface, price);
	add(offers,offer);
	if (ok == 1)
	{
		undo_op[undo_depth].index = 0;
		undo_op[undo_depth].lastOffer = offer;
		undo_op[undo_depth].operationType = opAdd;
		undo_depth = undo_depth + 1;
	}

	return 1;
}

void initialise_offers()
{
	addOffer("house", "adr1", 1200, 500000,-1);
	addOffer("apartment", "adr2", 45000, 500000,-1);
	addOffer("penthouse", "adr3", 20000, 900000,-1);
	addOffer("house", "adr4", 300, 150000,-1);
	addOffer("house", "adr5", 7000, 134000,-1);
	addOffer("apartment", "adr6", 100, 1200,-1);
	addOffer("apartment", "adr7", 500, 4000,-1);
	addOffer("penthouse", "adr8", 2000, 1000,-1);
	addOffer("penthouse", "adr9", 900, 7000,-1);
	addOffer("penthouse", "adr10", 2200, 620000,-1);

	addOffer("penthouse", "sdfsd", 2000, 1000,-1);
	addOffer("penthouse", "erwe", 900, 7000,-1);
	addOffer("penthouse", "diana3534", 2200, 620000,-1);

	addOffer("apartment", "adr666", 100, 120,-1);
	addOffer("apartment", "adr66666", 100, 12200,-1);
	addOffer("apartment", "adr666666", 100, 3200,-1);
	
}

int c_find(char *address)
{
	/*
	Finds the position of an offer with a certain address
	Input: address- a character string
	Output: the integer representing the position of the offer with the given address
	
	*/
	return find(offers, address);
}

int c_delete(char *address, int ok)
{
	/*
	Deletes an offer with a given address
	Input: address- a string
	Ouput: 1- if deleted successfully, -1 otherwise
	*/
	int pos = find(offers, address);
	if (pos == -1)
		return -1;

	if (ok == 1)
	{
		undo_op[undo_depth].index = pos;
		undo_op[undo_depth].lastOffer = offers->arr[pos];
		undo_op[undo_depth].operationType = opDelete;
		undo_depth = undo_depth + 1;
	}
	delete(offers, address);
	return 1;
}

int c_updatePrice(char *address, int price, int ok)
{
	/*
	Updates an offer with a given address, replacing its price
	Input: address- a string, price- an integer
	Ouput: 1- if updated successfully, -1 otherwise
	*/
	int pos = find(offers, address);
 	if (pos == -1)
		return -1;

	if (ok == 1)
	{
		undo_op[undo_depth].index = pos;
		undo_op[undo_depth].lastOffer = offers->arr[pos];
		undo_op[undo_depth].operationType = opUpdatePrice;
		undo_depth = undo_depth + 1;
	}

	updatePrice(offers,address, price);
	if (ok == 1)
		undo_op[undo_depth - 1].currentOffer = offers->arr[pos];

	return 1;
}

int c_updateSurface(char *address, int surface, int ok)
{
	/*
	Updates an offer with a given address, replacing its surface
	Input: address- a string, surface- an integer
	Ouput: 1- if updated successfully, -1 otherwise
	*/
	int pos = find(offers, address);
	if (pos == -1)
		return -1;

	if (ok == 1)
	{
		undo_op[undo_depth].index = pos;
		undo_op[undo_depth].lastOffer = offers->arr[pos];
		
		undo_op[undo_depth].operationType= opUpdateSurf;
		undo_depth = undo_depth + 1;
	}

	updateSurface(offers, address, surface);
	if(ok==1)
		undo_op[undo_depth - 1].currentOffer = offers->arr[pos];
	return 1;
}

int c_substring(int i,char *adr)
{
	/*
	Verifies if the offer with the index i had an address which contains the parameter given adr
	Input: i- integer, adr- string
	Output: -1 if the condition is not satisfied, 1- if it is

	*/
	char* ok;
	ok = strstr(offers->arr[i]->address,adr);
	if (ok == NULL)
		return -1;
	return 1;

}

int display_surface(int surface,int v[])
{
	int i;
	int ct = 0;
	for (i = 0; i < offers->size; i++)
	{
		if (offers->arr[i]->surface == surface)
			v[ct++] = i;
	}
	
	int j;
	for (i = 0; i < ct-1; i++)
		for (j = i + 1; j < ct; j++)
		{
			if (offers->arr[v[i]]->price > offers->arr[v[j]]->price)
			{
				int aux = v[i];
				v[i] = v[j];
				v[j] = aux;
			}
		}

	

	return ct;
}


int c_viewOffersType(char *type, int surface, int v[])
{
	int i ;
	int k = 0;
	for (i = 0; i < offers->size; i++)
	{
		if (strcmp(offers->arr[i]->type, type) == 0 && offers->arr[i]->surface > surface)
			v[k++] = i;
	}
	return k;
}

