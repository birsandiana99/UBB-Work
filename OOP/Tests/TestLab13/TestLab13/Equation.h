#pragma once
#include <string>
#include <math.h>
using namespace std;

struct sol {
	double x1;
	double x2;


};
class Equation
{
public:
	Equation(double a,double b,double c);
	double getA();
	double getB();
	double getC();
	void setA(double newA);
	void setB(double newB);
	void setC(double newC);
	string toString();
	struct sol computeResult();

	~Equation();
	
private:
	double a, b, c;
};

/*
istream& operator>>(istream& in, string line)
{
	in >> line;
	double a;
	double b;
	double c;

	size_t pos = line.find(",");
	a = stod(line.substr(0, pos));
	line.erase(0, pos + 1);

	pos = line.find(",");

	b = stod(line.substr(0, pos).c_str());
	line.erase(0, pos + 1);

	pos = line.find(",");

	c = stod(line.substr(0, pos));
	this->a = a;
	this->b = b;
	this->c = c;
}
*/
