#pragma once
#include "domain.h"
#include <string.h>


int validateOffer(char *address, char *type, int surface, int price);
int validateSurface(int surface);
int validatePrice(int price);

int validateAddress(char * address);
int validateType(char * type);
