#include "Controller.h"



Controller::Controller()
{
}

void Controller::update(Equation e,double a,double b,double c)
{
	this->repo.update(e,a,b,c);
}

vector<Equation> Controller::getAllEquations()
{
	return this->repo.getVector();
}


Controller::~Controller()
{
}
