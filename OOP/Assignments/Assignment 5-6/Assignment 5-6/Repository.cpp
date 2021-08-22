#include "Repository.h"
#include "FileManagerx.h"
/*
Repository::Repository()
{
	this->vector = vector;
}
*/


Repository::Repository()
{
	//this->fileManager = f;
	//this->fileManager.loadFromFile(this->vector);

	TextFileManager::loadFromFile(vector);
}

Repository::~Repository()
{	
	//vector.~DynamicVector();
}
int Repository::add(TElem elem)
{
	//if(this->findByName(elem.getName())!=-1)
		
	vector.emplace_back(elem);
	//this->fileManager.writeToFile(vector);
	FileManager* textFileManager = new TextFileManager();
	textFileManager->writeToFile(vector, "fisier.txt");
	
	return 1;
}

int Repository::remove(int index)
{
	vector.erase(vector.begin()+index);
	FileManager* textFileManager = new TextFileManager();
	textFileManager->writeToFile(vector,"fisier.txt");
	//this->fileManager.writeToFile(vector);
	return 1;
}

void Repository::update(string name, string new_name, string breed, int age, string photo)
{
	int idx;
	idx = findByName(name);
	vector[idx].setName(new_name);

	FileManager* textFileManager = new TextFileManager();
	textFileManager->writeToFile(vector,"fisier.txt");
	//this->fileManager.writeToFile(vector);
}

int Repository::getLen()
{
	return vector.size();
}

int Repository::findByName(string name)
{
	for (int i = 0; i < vector.size(); i++)
	{
		if (vector[i].getName() == name)
			return i;
	}
	return -1;
}

vector<TElem> &Repository::getAllDogs()
{
	return this->vector;
}

