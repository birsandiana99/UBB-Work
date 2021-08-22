#pragma once
#include "Dog.h"
//#include <vector>
//#include "DynamicVector.h"
#include <vector>
using namespace std;
typedef Dog TElem;
class Repository
{
public:
	Repository();
	~Repository();
	int add(TElem elem);
	int remove(int index);
	void update(string name, string new_name, string breed, int age, string photo);
	int getLen();
	int findByName(string name);
	vector<TElem> &getAllDogs();


private:
	vector<TElem> vector;
	//FileManager fileManager;
};

class MyRepoException :public exception {
public:
	explicit MyRepoException(string message) : message(std::move(message)) {};
	const string& getMessage() const {
		return this->message;
	}
private:
	string message;
};
