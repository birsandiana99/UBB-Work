#pragma once

//#include "DynamicArray.h"
#include "Dog.h"
#include <string>
#include "Controller.h"
#include <vector>

using namespace std;

class FileManager
{
public:
	FileManager() = default;
	virtual ~FileManager() = default;
	static void loadFromFile(vector<TElem> & v);
	virtual void writeToFile(vector<TElem> & v, string fisier) = 0;
};

class TextFileManager : public FileManager {
public:
	TextFileManager() = default;
	void writeToFile(vector<TElem> & v, string fisier) override;
};

class HTMLFileManager : public FileManager {
public:
	HTMLFileManager() = default;
	void writeToFile(vector<TElem> & v, string fisier) override;
};
