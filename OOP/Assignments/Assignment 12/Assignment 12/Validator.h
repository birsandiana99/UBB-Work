#pragma once
#include "Dog.h"
#include <string>

typedef Dog TElem;


class ValidatorException :public exception {
public:
	explicit ValidatorException(string message) : message(std::move(message)) {};
	const string& getMessage() const {
		return this->message;
	}
private:
	string message;
};



class Validator
{
public:
	Validator();
	~Validator();
	static int validateDog(string name, string breed, int age, string photo);
	static int validateName(string name);
	static int validateAge(int age);
	static int validatePhoto(string photo);
	static int validateBreed(string breed);

};

