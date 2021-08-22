#include "Repository.h"



Repository::Repository()
{
}

int Repository::add(TElem elem)
{
	/*
	Adds a new player to the DA contained by the repo 
	Input: elem - an element of type TElem
	Output: elem is added to the DA; returns 1 if successful, -1 otherwise(if the element already exists)
	*/
	if (this->da.searchElem(elem.getName()) != -1)
		return -1;
	else
	{
		this->da.add(elem);
		return 1;
	}
}

DynamicVector<TElem> Repository::getPlayers()
{
	return this->da;
}


Repository::~Repository()
{
}
