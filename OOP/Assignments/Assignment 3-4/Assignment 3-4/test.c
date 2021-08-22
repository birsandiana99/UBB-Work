#include "test.h"
#include "contr.h"
#include <stdio.h>
void testAdd()
{
	runController();
	int x = addOffer("house", "adr1", 123, 123,1);
	assert(offers->size == 1 && x==1);

	assert(addOffer("penthouse", "adr1", 123, 1234,1) == -1);
	assert(addOffer("", "house", 123, 123,1) == -1);

}
void testValidator()
{
	assert(validateOffer("", "house", 123,123 ) == 0);
	assert(validateOffer("adr", "gdf",123 ,123 ) == 0);
	assert(validateOffer("adr1", "house",0 ,123 ) == 0);
	assert(validateOffer("adr1", "house",123 , 0) == 0);

	assert(validateOffer("adr1", "house",123 ,123 ) == 1);

}
void testUpdate()
{
	runController();
	int x = addOffer("house", "adr1", 123, 123,1);
	c_updatePrice("adr1", 666,1);
	assert(offers->arr[0]->price == 666);

	c_updateSurface("adr1", 666,1);
	assert(offers->arr[0]->surface == 666);

	assert(c_updatePrice("adrrrr", 1234,1) == -1);
}

void testDelete()
{
	runController();
	addOffer("penthouse", "adr1", 123, 1234,1);
	addOffer("house", "adr2", 222, 222,1);
	addOffer("penthouse", "adr3", 333, 444,1);
	c_delete("adr1",1);
	assert(offers->size == 2);
	assert(c_delete("adrrrr",1) == -1);
}

void testFound()
{
	runController();
	addOffer("penthouse", "adr1", 123, 1234,1);
	addOffer("house", "ddr2", 222, 222,1);
	addOffer("penthouse", "ccr3", 333, 444,1);
	assert(c_substring(0, "adr") == 1);
}


void testUndo()
{
	runController();
	addOffer("penthouse", "adr1", 123, 1234,1);
	addOffer("house", "ddr2", 222, 222,1);
	addOffer("penthouse", "ccr3", 333, 444,1);

	c_delete("adr1", 1);
	undoOperation();
	assert(offers->size == 3);

	redoOperation();
	assert(offers->size == 2);


	addOffer("house", "adr3", 11, 22,1);
	undoOperation();
	assert(offers->size == 2);
	redoOperation();
	assert(offers->size == 3);
}