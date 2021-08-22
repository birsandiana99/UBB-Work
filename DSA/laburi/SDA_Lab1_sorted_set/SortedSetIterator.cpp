#include "SortedSetIterator.h"
#include "stdafx.h"
#include <stdexcept>

SortedSetIterator::SortedSetIterator(const SortedSet &set) : set {set}
{
	/*
	Theta(1)
	*/
	currIndex = 0;
}



void SortedSetIterator::jumpForward(int k)
{
	/*
	Theta(1)
	*/
	if(!valid() or k<=0)
	{
		throw std::invalid_argument("exception");
	}
	currIndex = currIndex + k;
}

void SortedSetIterator::first()
{
	/*
	Theta(1)
	*/
	currIndex = 0;
}

void SortedSetIterator::next()
{
	/*
	Theta(1)
	*/
	if (!valid())
	{
		throw std::invalid_argument("exception");
	}
	++currIndex;
}

bool SortedSetIterator::valid() const
{
	/*
	Theta(1)
	*/
	return currIndex < set.size();
}

TElem SortedSetIterator::getCurrent() const
{
	/*
	Theta(1)
	*/
	return set.da.getElement(currIndex);
}
