#include "Dog.h"
#include <iostream>


Dog::Dog(string breed, string name, int age, string photo) : breed(breed), name(name), age(age), photo(photo)
{}

string Dog::getBreed() const
{
	return this->breed;
}


string Dog::getName() const
{
	return this->name;
}

int Dog::getAge() const
{
	return this->age;
}

string Dog::getPhoto() const
{
	return this->photo;
}

void Dog::setBreed(string breed)
{
	this->breed = breed;
}

void Dog::setName(string name)
{
	this->name = name;
}

void Dog::setAge(int age)
{
	this->age = age;
}

void Dog::setPhoto(string photo)
{
	this->photo = photo;
}

int Dog::compareBreed(string breed)
{
	if (this->breed.compare(breed) ==0)
		return 1;
	return 0;
}

string Dog::Tostring()
{
	string s;
	s += "Breed: " + this->getBreed() + " / Name: " + this->getName() + " / Age: " + to_string(this->getAge());
	return s;
}



istream & operator>>(istream & in, Dog & dog)
{
	string name;
	int age;
	string breed;
	string photo;

	string line;
	in >> line;

	size_t pos = line.find(",");
	name = line.substr(0, pos);
	line.erase(0, pos + 1);

	pos = line.find(",");

	age = atoi(line.substr(0, pos).c_str());
	line.erase(0, pos + 1);

	pos = line.find(",");

	breed = line.substr(0,pos);
	photo = line;

	dog.setName(name);
	dog.setAge(age);
	dog.setBreed(breed);
	dog.setPhoto(photo);

	return in;
}
/*
ostream & operator<<(ostream & out, const Dog & dog)
{
	out << dog.getName() << "  " << dog.getAge() << "  " << dog.getBreed() << "  " << dog.getPhoto() << endl;
	return out;
}
*/


