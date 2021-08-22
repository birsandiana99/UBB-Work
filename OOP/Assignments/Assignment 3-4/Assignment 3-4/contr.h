#pragma once

#include "repo.h"
#include "undo.h"

struct DynamicArray* offers;

void runController();

void initialiseValues();

int addOffer(char *type, char *address, int surface, int price, int ok);

int c_find(char *address);


int c_delete(char *address,int ok);

int c_updatePrice(char *address, int price, int ok);

int c_updateSurface(char *address, int surface, int ok);

int c_substring(int i, char *adr);

int display_surface(int surface, int v[]);

int c_viewOffersType(char * type, int surface, int v[]);


