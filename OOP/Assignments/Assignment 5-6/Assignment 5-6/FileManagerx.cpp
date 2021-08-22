#include "FileManagerx.h"
//#include "FileMng.h"

void FileManager::loadFromFile(vector <TElem> &v)
{
	ifstream in("fisier.txt");
	Dog dog;

	while (in >> dog)
	{
		v.emplace_back(dog);
	}
}
/*
void TextFileManager::writeToFile(vector <TElem> &v)
{
	ofstream out("fisier.txt");
	for (int i = 0; i < v.size(); ++i)
	{
		out << v[i].getName() + "," << v[i].getAge() << "," + v[i].getBreed() << "," + v[i].getPhoto() << endl;
	}
}

void HTMLFileManager::writeToFile(vector <TElem> & v)
{
	ofstream out("htmlFile.html");
	out << "<!DOCTYPE html>" << endl;
	out << "<html>" << endl;
	out << "<head><title>Dog adoption list</title></head>" << endl;
	out << "<body style=\"background-color:pink;\"><table border=\"1\">" << endl;

	out << "<tr>" << endl;
	out << "<td>Name</td>" << endl;
	out << "<td>Age</td>" << endl;
	out << "<td>Breed</td>" << endl;
	out << "<td>Photo</td>" << endl;
	out << "</tr>" << endl;

	for (const auto& dog : v) {
		out << "<tr>" << endl;
		out << "<td>" << dog.getName() << "</td>" << endl;
		out << "<td>" << dog.getAge() << "</td>" << endl;
		out << "<td>" << dog.getBreed() << "</td>" << endl;
		out << "<td>" << dog.getPhoto() << "</td>" << endl;
		out << "</tr>" << endl;
	}

	out << "</table>" << endl;
	out << "</body>" << endl;
	out << "</html>" << endl;
}

*/

void TextFileManager::writeToFile(vector<TElem>& v, string fisier)
{
	//ofstream out("fisier.txt");
	ofstream out(fisier);
	for (int i = 0; i < v.size(); ++i)
	{
		out << v[i].getName() + "," << v[i].getAge() << "," + v[i].getBreed() << "," + v[i].getPhoto() << endl;
	}
}

void HTMLFileManager::writeToFile(vector<TElem>& v,string fisier)
{
	//ofstream out("htmlFile.html");
	ofstream out(fisier);

	out << "<!DOCTYPE html>" << endl;
	out << "<html>" << endl;
	out << "<head><title>Dog adoption list</title></head>" << endl;
	out << "<body style=\"background-color:pink;\"><table border=\"1\">" << endl;

	out << "<tr>" << endl;
	out << "<td>Name</td>" << endl;
	out << "<td>Age</td>" << endl;
	out << "<td>Breed</td>" << endl;
	out << "<td>Photo</td>" << endl;
	out << "</tr>" << endl;

	for (const auto& dog : v) {
		out << "<tr>" << endl;
		out << "<td>" << dog.getName() << "</td>" << endl;
		out << "<td>" << dog.getAge() << "</td>" << endl;
		out << "<td>" << dog.getBreed() << "</td>" << endl;
		out << "<td>" << dog.getPhoto() << "</td>" << endl;
		out << "</tr>" << endl;
	}

	out << "</table>" << endl;
	out << "</body>" << endl;
	out << "</html>" << endl;
}
