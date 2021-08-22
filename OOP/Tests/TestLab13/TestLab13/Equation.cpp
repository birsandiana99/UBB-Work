#include "Equation.h"
using namespace std;
#include <algorithm>


Equation::~Equation()
{
}

Equation::Equation(double a, double b, double c) : a(a),b(b),c(c)
{
}

double Equation::getA()
{
	return this->a;
}

double Equation::getB()
{
	return this->b;
}

double Equation::getC()
{
	return this->c;
}

void Equation::setA(double newA)
{
	this->a = newA;
}

void Equation::setB(double newB)
{
	this->b = newB;
}

void Equation::setC(double newC)
{
	this->c = newC;
}

string Equation::toString()
{ 
	string s = "";
	if (this->a != 0)
		if (this->b != 0 || this->c != 0)
			s += to_string(this->a) + " * x^2 + ";
		else
			s += to_string(this->a) + " * x^2";
	if (this->b != 0)
		if (this->c != 0)
			s += to_string(this->b) + " * x + ";
		else
			s += to_string(this->b) + " * x ";
	if (this->c != 0)
		s += to_string(this->c);
	//s += to_string(this->a) + " * x^2 + " + to_string(this->b) + " * x + " + to_string(this->c);
	return s;
}

struct sol Equation::computeResult()
{
	double delta = b*b - 4 * a*c;
	if (delta > 0)
	{
		double x1;
		double x2;
		x1 = (-1 * b + sqrt(delta)) / 2 * a;
		x2 = (-1 * b - sqrt(delta)) / 2 * a;
		sol mysolution;
		mysolution.x1 = x1;
		mysolution.x2 = x2;
		return mysolution;

	}
//	else
	//{
		//delta = -1 * delta;
//		return 0;
	//}
}

