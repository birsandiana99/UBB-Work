#pragma once
#include <vector>
#include <Equation.h>	
using namespace std;
class Repository
{
public:
	Repository();
	//void add(Equation e);
	void update(Equation e,double a,double b,double c);
	vector<Equation> getVector();
	~Repository();

private:
	vector<Equation> myVector;
};

