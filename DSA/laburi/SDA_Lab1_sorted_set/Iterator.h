#pragma once

#include "DynamicArray.h"

class DAIterator
{
private:
	friend class DynamicArray;
	DAIterator(const DynamicArray& c);
	const DynamicArray& da;
public:
	int index;
	void first();
	void next();
	bool valid() const;
	TElem getCurrent() const;
};

