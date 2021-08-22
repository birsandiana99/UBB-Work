#pragma once
#include "Repository.h"
#include <string>
#include "Validator.h"
#include "Comparator.h"
#include "FileManagerx.h"
class Controller
{
public:
	Controller();
	~Controller();
	int add(TElem elem);
	int remove(string name);
	int update(string name, string new_name);
	int alreadyExists(string name);
	vector<TElem> &getAllDogs();
	vector<TElem> getAdoptionList();
	int addToAdoptionList(TElem elem, int op);
	int getSize();
	void sort(Comparator<Dog> & comp);

private:
	Repository repo;
	vector<TElem> adoptionList;
};

