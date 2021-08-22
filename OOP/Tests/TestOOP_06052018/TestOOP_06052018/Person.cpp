#include "Person.h"
using namespace std;
#include <iostream>
#include <algorithm>
#include <fstream>

Person::Person(string name)
{
	this->name = name;
}

void Person::addAnalisys(MedicalAnalysis *m)
{
	this->vector.emplace_back(m);
}



const vector<MedicalAnalysis *> &Person::showAllAnalises()
{
	return this->vector;
}
bool Person::isHealthy(int month)
{
	int ct = 0;
	for (auto& thing : this->vector)
	{
		string date = thing->getDate();
		int x = stoi(date.substr(5, 2));
		//cout<<x;
		if (x == month) { ct++; 
			if (thing->isResultOK() == 0)
				return false;
		}
	}
	return true;
}



void Person::initialize()
{
	BMI *bmi1 =new BMI("2019.03.12", 20);
	BP *bp1 = new BP("2019.03.23", 100, 69);
	BP *bp2 = new BP("2019.05.23", 100, 69);
	this->addAnalisys(bmi1);
	this->addAnalisys(bp2);
	this->addAnalisys(bp1);
}
void Person::writeToFile(string date)
{
	//sort(vector.begin(), vector.end(), [](MedicalAnalysis *x1, MedicalAnalysis *x2) {
	//	return x1->getDate() < x2 ->getDate();
	//});

	ofstream out("outfile.txt");
	for (const auto& thing : this->vector) {
		if(thing->getDate()>date)
			out << thing->toString() << "  Result: "<<thing->isResultOK()<<endl;
	}

	out.close();
}
Person::~Person()
{
}
