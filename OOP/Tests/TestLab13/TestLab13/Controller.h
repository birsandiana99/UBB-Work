#pragma once
#include "Repository.h"
class Controller
{
public:
	Controller();
	void update(Equation e,double a, double b, double c);
	vector<Equation> getAllEquations();
	~Controller();

private:
	Repository repo;
};

