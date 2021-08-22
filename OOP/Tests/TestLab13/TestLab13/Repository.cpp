#include "Repository.h"
#include <fstream>


Repository::Repository()
{
	ifstream in("fisier.txt");
	string line;
	//in >> line;
	while(in >> line)
	{ 
		
		//string line;
		//in >> line;
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

		

		Equation eq = Equation(a,b,c);
		myVector.emplace_back(eq);

		
	}
	
}


void Repository::update(Equation e, double a, double b, double c)
{	ofstream out("fisier.txt");
	for (int i = 0; i < myVector.size(); i++)
	{
		if (myVector[i].getA() == e.getA() && myVector[i].getB() == e.getB() && myVector[i].getC() == e.getC())
		{
			myVector[i].setA(a);
			myVector[i].setB(b);
			myVector[i].setC(c);

		}
		
		//out.precision(1);
		out << myVector[i].getA();
		out << ",";
		//out.precision(1);
		out << myVector[i].getB();
		out << ",";
		//out.precision(1);
		out << myVector[i].getC();
		out << endl;

	}


}

vector<Equation> Repository::getVector()
{
	return this->myVector;
}

Repository::~Repository()
{
}
