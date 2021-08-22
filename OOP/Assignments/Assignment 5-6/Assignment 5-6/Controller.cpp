#include "Controller.h"
#include "FileManagerx.h"
#include <iostream>
Controller::Controller()
{
	this->repo = Repository();
	//this->adoptionList = Repository();
}


Controller::~Controller()
{
	//delete[] this->repo.getAllDogs().getArray();
	//delete[] this->adoptionList.getAllDogs().getArray();
	//repo.~Repository();
	//adoptionList.~Repository();
}

int Controller::add(TElem elem)
{
	/*
	if (alreadyExists(elem.getName()) == 0)// && Validator::validateDog(elem))
	{repo.add(elem); return 1; }
	
		return -1;
		*/

	//&& Validator::validateAge(elem.getAge())
//	try{
	
	if (Validator::validateDog(elem.getName(), elem.getBreed(), elem.getAge(), elem.getPhoto()) == false)
		return 0;
	if (alreadyExists(elem.getName()) == 0)
	{		
			repo.add(elem);
			return 1;

		//else
			//throw MyRepoException("Name already exists!");
			
	}
	//}
	//catch(alreadyExistsException &e)
	//{
	//	cout << e.what();
	//}
	return -1;
}

int Controller::remove(string name)
{
	//if (Validator::validateName(name) == 0)
		//return -1;

	int i = repo.findByName(name);
	if (i == -1)
		return -1;
	repo.remove(i);
	return 1;
}

int Controller::update(string name, string new_name)
{
	//if (Validator::validateName(name) == 0 || !Validator::validateName(new_name))
		//return -1;
	int i = repo.findByName(name);
	repo.update(name, new_name, repo.getAllDogs()[i].getBreed(), repo.getAllDogs()[i].getAge(), repo.getAllDogs()[i].getPhoto());
	return 1;
}

int Controller::alreadyExists(string name)
{
	return repo.findByName(name)!=-1;
}

vector<TElem> &Controller::getAllDogs()
{
	return repo.getAllDogs();
}
vector<TElem> Controller::getAdoptionList()
{
	return adoptionList;
}

int Controller::addToAdoptionList(TElem elem, int op)
{
	int ok = -1;
	for (int i = 0; i < adoptionList.size(); i++)
	{
		if (adoptionList[i].getName() == elem.getName())
			ok = i;
	}
	if (ok == -1) {
		adoptionList.emplace_back(elem);

		if (op == 1)
		{
			FileManager* textFileManager = new TextFileManager();
			textFileManager->writeToFile(adoptionList,"fisierAdoptie.txt");
		}
		else if (op == 2)
		{
			FileManager* textFileManager = new HTMLFileManager();
			textFileManager->writeToFile(adoptionList,"htmlFile.html");
		}
	}
	else
		return -1;
}

int Controller::getSize()
{
	return this->repo.getLen();
}


void Controller::sort(Comparator<TElem>& comp)
{
	for (int i = 0; i < this->getAllDogs().size() - 1; i++)
		for (int j = i; j < this->getAllDogs().size(); j++)
			if (comp.compare(this->getAllDogs()[i], this->getAllDogs()[j]) != 0)
				swap(this->getAllDogs()[i], this->getAllDogs()[j]);
}

