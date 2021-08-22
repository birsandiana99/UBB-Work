#include <stdlib.h>
#include <iostream>
#include "UI.h"
#include "MedicalAnalysis.h"
#include "Person.h"
int main() {
	/*
	BMI *bmi1 = new BMI("12.03.1999",19);
	//cout << bmi1.toString()<<"\n";
	//cout << bmi1.isResultOK()<<endl;
	BP bp1 = BP("12.04.2200", 100, 76);
	cout << bp1.toString() << endl;
	cout << bp1.isResultOK() << endl;

	Person person1 = Person("Anastasia");
	person1.addAnalisys(new BMI("1213", 342));
	

	for (auto& thing : person1.showAllAnalises())
	{
		cout << thing->toString()<<endl;
	}
	
*/
	
	{
		UI ui=UI();
		ui.run();
	}
	
	system("pause");
	return 0;
}
