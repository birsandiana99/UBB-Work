#include "Validator.h"
#include <iostream>


Validator::Validator()
{
}


Validator::~Validator()
{
}

int Validator::validateDog(string name, string breed, int age, string photo)
{
	//cout << "Dog with name: " << name;
	try {

		Validator::validateAge(age) && Validator::validateName(name) && Validator::validateAge(age) && Validator::validatePhoto(photo);



	}
	catch (const ValidatorException& e){
		cout << e.getMessage() << endl;
		return false;
	}

}

int Validator::validateName(string name)
{
	if (name.empty()) {
		throw ValidatorException("Validation ERROR: Name must not be empty!");
	}

	return true;
}

int Validator::validateAge(int age)
{
	if (age <= 0 || age > 15) {
		throw ValidatorException("Validation ERROR: Age must be between 0 and 15!");
	}

	return true;
}

int Validator::validatePhoto(string photo)
{
	if (photo.empty()) {
		throw ValidatorException("Validation ERROR: Photograph must not be empty!");
	}

	return true;
}

int Validator::validateBreed(string breed)
{
	if (breed.empty()) {
		throw ValidatorException("Validation ERROR: Breed must not be empty!");
	}

	return true;
}
