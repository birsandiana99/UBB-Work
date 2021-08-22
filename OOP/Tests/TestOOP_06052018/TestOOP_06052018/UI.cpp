#include "UI.h"
using namespace std;
#include <iostream>
#include <string>
#include "Person.h"

UI::UI()
{
}

void UI::printMenu()
{
	cout << "Press 1. to add an analysis...\n";
	cout << "Press 2. to view all the analyses...\n";
	cout << "Press 3. to show if you are healthy...\n";
	cout << "Press 4. to write to the file...\n";
	cout << "Press 0. to exit...\n";
}

void UI::run()
{
	string name;
	cout << "Enter your name: ";
	cin>>name;
	Person person = Person(name);
	person.initialize();
	printMenu();
	int command = -1;
	while (command != 0)
	{
		cout << "Enter the option: ";
		cin >> command;
		if (command == 1)
		{
			int type;
			cout << "\tEnter the type of the analisys(1 for BMI, 2 for BP) : ";
			cin >> type;
			cout << "\n";
			if (type == 1)
			{
				string date;
				double value;
				cout << "\tEnter a date: ";
				cin >> date;
				cout << "\tEnter the value: ";
				cin >> value;

				person.addAnalisys(new BMI(date, value));
			}
			else if (type == 2)
			{
				string date;
				int diastolic, systolic;
				cout << "\tEnter a date: ";
				cin >> date;
				cout << "\tEnter the diastolic value: ";
				cin >> diastolic;
				cout << "\tEnter the systolic value: ";
				cin >> systolic;
				person.addAnalisys(new BP(date, systolic, diastolic));
			}
				

		}
		else if (command == 2)
		{
			for (auto& thing : person.showAllAnalises())
			{
				cout << thing->toString() << endl;
			}

		}
		else if (command == 3)
		{
			int month;
			cout << "Give me the current month: ";
			cin >> month;
			if (person.isHealthy(month)==1)
				cout << "Healthy!";
			else
				cout << "Unhealthy :(";
		}
		else if (command == 4)
		{
			person.writeToFile("2019.03.13");
		}
		
	}

}


UI::~UI()
{
}
