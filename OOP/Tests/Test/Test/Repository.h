#pragma once
#include "Player.h"
#include "DynamicVector.h"
typedef Player TElem;
class Repository
{
public:
	Repository();
	int add(TElem elem);
	DynamicVector<TElem> getPlayers();
	~Repository();
private:
	DynamicVector<TElem> da;
};

