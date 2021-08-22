#pragma once

typedef struct Offer Offer;
struct Offer
{
	char *address, *type;
	int surface, price;
};

struct Offer *create(char *type, char*address, int surface, int price);

