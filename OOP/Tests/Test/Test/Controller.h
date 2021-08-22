#pragma once
#include "Repository.h"
class Controller
{
public:
	Controller();
	int add(TElem elem);
	DynamicVector<TElem> getPlayers();
	string showPlayers();
	int totalGoalsCountry(string country);
	void initialise();
	~Controller();

private:
	Repository repo;
};

