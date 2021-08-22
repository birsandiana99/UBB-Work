#include "SortedSet.h"
#include "stdafx.h"


SortedSet::SortedSet(Relation r)
{
	this->r = r;
}

bool SortedSet::add(TComp e)
{
	/*
	O(n)
	*/
	if (this->da.search(e) != -1) //&& (this->da.search(e) < this->da.size())) 
			return false; //O(n)
	else {
		int pos = 0;
		while (pos < this->da.size() && e!= this->da.getElement(pos) && this->r(this->da.getElement(pos),e)) {
			pos++;
		}
		this->da.addToPosition(pos, e);
		return true;
	}
}

bool SortedSet::remove(TComp e)
{
	/*
	O(n)
	*/
	if (this->da.search(e) > -1)
	{
		int pos = da.search(e);
		da.remove(pos);
		return true;
	}
	return false;
}

bool SortedSet::search(TElem elem) const
{	/*
	O(n)
	*/
	for (int i = 0; i < da.size(); ++i)
	{
		if (da.getElement(i) == elem)
			return true;
	}

	return false;
}

int SortedSet::size() const
{
	/*
	Theta(1)
	*/
	return da.size();
}

bool SortedSet::isEmpty() const
{
	/*
	Theta(1)
	*/
	return da.size() == 0;
}

SortedSetIterator SortedSet::iterator() const
{
	/*
	Theta(1)
	*/
	return SortedSetIterator(*this);
}


SortedSet::~SortedSet()
{
}


