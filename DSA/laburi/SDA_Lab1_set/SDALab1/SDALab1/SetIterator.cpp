#include "SetIterator.h"

SetIterator::SetIterator(const Set & set) : set{ set }
{
	currentIndex = 0;
}

void SetIterator::first()
{
	currentIndex = 0;
}

class NotValidException : public exception
{
	virtual const char* what() const throw()
	{
		return "Element not valid!";
	}
};

void SetIterator::next()
{
	try
	{
		if (!valid())
		{
			throw new NotValidException();
		}

		++currentIndex;
	}
	catch (exception &e)
	{
		cout << e.what();
	}
	
}

bool SetIterator::valid() const
{
	return currentIndex < set.size();
}

TElem SetIterator::getCurrent() const
{
	try
	{
		if (!valid())
			throw new NotValidException();
		else
			return set.da.getElement(currentIndex);
	}
	catch (exception &e)
	{
		cout << e.what();
	}
}

