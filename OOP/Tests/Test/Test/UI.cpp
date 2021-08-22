#include "UI.h"
#include <iostream>
#include "tests.h"
using namespace std;


UI::UI()
{
}

void UI::printMenu()
{
	
	cout << "\tPress 1. to add a new player"<<endl;
	cout << "\tPress 2. to show all the players, sorted by the number of goals scored"<<endl;
	cout << "\tPress 3. to calculate the total of goals scored by a given country"<<endl;
	cout << "\tPress 0. to exit the application" << endl;
	cout << endl;
}

void UI::run()
{
	tests t = tests();
	t.testAll();
	cout << "Welcome!" << endl;
	Controller c = Controller();
	c.initialise();
	int command = -1;
	while (command != 0)
	{
		printMenu();
		cout << "\tEnter a comand:";
		cin >> command;
		if (command == 1)
		{
			//char name[50];
			string name = "";
			string firstName,lastName, nationality, team;
			int goals;
			cout << endl;
			cout << "\tEnter the player's name: ";
			cin >> firstName;
			cin >> lastName;
			name += firstName + " "+lastName;
			cout << "\tEnter the player's nationality: ";
			cin >> nationality;
			cout << "\tEnter the player's team: ";
			cin >> team;
			cout << "\tEnter the player's number of goals: ";
			cin >> goals;
			cout << endl;
			if (c.add(Player(name, nationality, team, goals)) == -1)
				cout << "\tPlayer not added. It already exists"<<endl;
			else
				cout << "\tPlayer added successfully"<<endl;
			cout << endl;
		}
		else if (command == 2)
		{
			cout << endl;
			cout << c.showPlayers();
			cout << endl;
		}
		else if (command == 3)
		{
			string country;
			cout << endl<<"\tEnter a country:";
			cin >> country;
		
			cout << endl;
			int total = c.totalGoalsCountry(country);
			if (total == 0)
				cout << "\tOops! Looks like the country you are searching for has no goals or does not exist!";
			else
				cout << "\tThe total of goals scored by players in ="<<country<<"= is: "<<total;
			cout << endl<<endl;
		}
		else if (command != 0)
			cout << "\t\tInvalid command";
	}
}


UI::~UI()
{
}
