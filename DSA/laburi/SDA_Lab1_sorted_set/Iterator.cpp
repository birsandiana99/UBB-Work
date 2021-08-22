//#include "stdafx.h"
#include "Iterator.h"
#include <stdexcept>
#include "stdafx.h"


DAIterator::DAIterator(const DynamicArray& c) : da(c)
{
	this->index = 0;
}

void DAIterator::first()
{
	this->index = 0;
}

void DAIterator::next()
{
	if (valid() == 0) {
		throw std::invalid_argument("Invalid iterator");
	}
	this->index++;
}

bool DAIterator::valid() const
{
	return this->index < da.sizee;
}

TElem DAIterator::getCurrent() const
{
	return da.getElement(this->index);
}


