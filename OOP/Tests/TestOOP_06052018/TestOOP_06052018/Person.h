#pragma once
#include <string>
using namespace std;
#include "MedicalAnalysis.h"
#include <stdlib.h>
#include <vector>
class Person
{
public:
	Person(string name);
	void addAnalisys(MedicalAnalysis *m);
	//vector<MedicalAnalysis> getALlAnalises();
	const vector<MedicalAnalysis*> &showAllAnalises();
	bool isHealthy(int month);
	void initialize();
	void writeToFile(string date);
	~Person();
private:
	string name;
	vector<MedicalAnalysis*> vector;
};

