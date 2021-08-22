#include "MedicalAnalysis.h"
#include<sstream>


MedicalAnalysis::MedicalAnalysis(string date)
{
	this->date = date;
}



string MedicalAnalysis::getDate()
{
	return this->date;
}

MedicalAnalysis::~MedicalAnalysis()
{
}

BMI::BMI(string date, double value): MedicalAnalysis{date}
{
	this->value = value;
}

bool BMI::isResultOK()
{
	if (this->value > 18.5 && this->value < 25) {

		return true;
	}
	return false;
}

string BMI::toString()
{
	stringstream buffer;
	buffer << "\tBMI \n\tDate: "<<this->date << "\tValue: " << this->value;
	return buffer.str();
}

BP::BP(string date, int systolicValue, int diastolicValue):MedicalAnalysis{date}
{
	this->diastolicValue = diastolicValue;
	this->systolicValue = systolicValue;
}

bool BP::isResultOK()
{
	if (this->diastolicValue > 60 && this->diastolicValue < 79 && this->systolicValue>90 and this->systolicValue < 119)
		return true;
	return false;
}

string BP::toString()
{
	stringstream buffer;
	buffer << "\tBP \n\tDate: " << this->date << "\tSystolic value: " << this->systolicValue << "\tDiastolic value: " << this->diastolicValue;
	return buffer.str();
}
