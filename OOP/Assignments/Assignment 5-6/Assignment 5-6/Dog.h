#pragma once
#include <fstream>
#include <string>

using namespace std;

class Dog
{
	public:

	Dog() = default;
	Dog(string breed, string name, int age, string photo);
	~Dog() = default;

	string getBreed() const;
	string getName() const;
	int getAge() const;
	string getPhoto() const;

	void setBreed(string breed);
	void setName(string name);
	void setAge(int age);
	void setPhoto(string photo);
	int compareBreed(string breed);
	string Tostring();
	

	private:
		string breed;
		string name;
		int age;
		string photo;

};

istream& operator >> (istream& in, Dog& dog);
ostream& operator << (ostream& out, const Dog& dog);
