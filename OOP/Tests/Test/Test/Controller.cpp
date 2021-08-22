#include "Controller.h"



Controller::Controller()
{
}

int Controller::add(TElem elem)
{
	/*
	Adds a new player to the DA contained by the repo atribute of the controller
	Input: elem - an element of type TElem
	Output: adds the new player; Returns 1 if successful, -1 otherwise(if the element already exists)
	*/
	return this->repo.add(elem);
}

DynamicVector<TElem> Controller::getPlayers()
{
	return this->repo.getPlayers();
}

string Controller::showPlayers()
{
	string s = "";
	DynamicVector<TElem> dv;
	for (int i = 0; i < this->repo.getPlayers().getSize(); i++)
		dv.add(this->repo.getPlayers()[i]);

	for(int i=0;i<dv.getSize()-1;i++)
		for(int j=i+1;j<dv.getSize();j++)
			if (dv[i].getGoals() > dv[j].getGoals())
			{
				swap(dv[i], dv[j]);
			}
	for (int i = 0; i < dv.getSize(); i++)
		s += "\t"+dv[i].toString()+"\n";
	return s;
}

int Controller::totalGoalsCountry(string country)
{
	/*
	Calculates the total of goals scored by players of a given country
	Input: country - a string representing the country we want to find the total score of
	Output: totalScore - an integer representing the total score (if the country does not exist it will return 0)
	
	*/
	int totalScore = 0;
	for (int i = 0; i < this->repo.getPlayers().getSize(); i++)
		if (this->repo.getPlayers()[i].getNationality() == country)
		{
			totalScore += this->repo.getPlayers()[i].getGoals();
		}
	return totalScore;
}

void Controller::initialise()
{
	this->add(Player("Isabelle Gullden", "SWE", "CSM Bucuresti", 80));
	this->add(Player("Cristina Neagu", "ROU", "Buducnost", 63));
	this->add(Player("Anabela Oprisor", "ROU", "Bucharest CC", 37));
	this->add(Player("Allison Pineau", "FRA", "HCM Baia Mare", 82));
	this->add(Player("Ilina Ekaterina", "RUS", "Rostov-Don", 80));
}


Controller::~Controller()
{
}
