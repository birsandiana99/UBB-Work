#pragma once
#include <fstream>
#include <string>
using namespace std;
class Equation
{
public:
	Equation();
	~Equation();


private:
	int a, b, c;
};
istream& operator >> (istream& in, Equation& eq);


