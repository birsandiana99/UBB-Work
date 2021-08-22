#pragma once
using namespace std;
#include <string>
class MedicalAnalysis
{
public:
	MedicalAnalysis(string date);
	virtual bool isResultOK()=0;
	virtual string toString()=0;
	string getDate();
	~MedicalAnalysis();
protected:
	string date;
};


class BMI : public MedicalAnalysis {
public:
	BMI(string date, double value);
	bool isResultOK() override;
	string toString() override;
private:
	//string date;
	double value;

};


class BP : public MedicalAnalysis {
public:
	BP(string date, int systolicValue, int diastolicValue);
	bool isResultOK() override;
	string toString() override;
private:
	//string date;
	int systolicValue;
	int diastolicValue;

};
