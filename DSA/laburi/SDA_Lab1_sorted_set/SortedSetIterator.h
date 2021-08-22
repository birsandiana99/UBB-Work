#pragma once
#include "SortedSet.h"

typedef int TComp;
typedef TComp TElem;
typedef bool(*Relation)(TComp, TComp);
class SortedSet;

class SortedSetIterator
{

private:
	friend class SortedSet;
	SortedSetIterator(const SortedSet& set);
	const SortedSet &set;
	int currIndex;
	

public:
	void jumpForward(int k);
	void first();
	void next();
	bool valid() const;
	TElem getCurrent() const;

};

