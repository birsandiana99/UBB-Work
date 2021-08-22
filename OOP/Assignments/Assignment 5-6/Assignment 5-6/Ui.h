#pragma once
#include "Controller.h"
class Ui
{
public:
	Ui();
	~Ui();
	string readString();
	void MenuAdmin();
	void MenuUser();
	void run();
	void openLink(string link);
	void initialise();
	void viewAllDogs(int op);
	void viewDogsFilter(int op);
	void viewAdoptionList();
private:
	Controller controller;
};

