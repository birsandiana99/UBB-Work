#include <iostream>
#include "Dog.h"
#include "DynamicVector.h"
#include "Repository.h"
#include "Ui.h"
#include "Tests.h"
#include <crtdbg.h>
#include "Comparator.h"
using namespace std;

int main()
{

	//Tests t = Tests();
	//t.runAll();

	/*
	Controller c = Controller();
	Dog d1 = Dog("br1", "a", 12, "photo");
	Dog d2 = Dog("br1", "b", 12, "photo");
	Dog d3 = Dog("br1", "aa", 12, "photo");
	Dog d4 = Dog("br1", "abg", 12, "photo");
	Dog d5 = Dog("br1", "y", 12, "photo");
	Dog d6 = Dog("br1", "u", 12, "photo");
	Dog d7 = Dog("br1", "r", 12, "photo");
	Dog d8 = Dog("br1", "q", 12, "photo");
	
	
	c.add(d1);
	c.add(d2);
	c.add(d3);
	c.add(d4);
	c.add(d5);
	c.add(d6);
	c.add(d7);
	c.add(d8);
	cout << endl<<c.getSize()<<endl;

	CompareAscendingByName c1;
	//cout << c1.compare(d2, d1);
	

	c.sort(c1);
	for (int i = 0; i < c.getAllDogs().size(); i++)
		cout << c.getAllDogs()[i].Tostring()<<endl;
	*/

//	Dog d1 = Dog("lab", "pugy", 23, "");
//	Validator::validateDog(d1.getName(), d1.getBreed(), d1.getAge(), d1.getPhoto());

	/*
	Dog d1 = Dog("lab", "pugy", 23, "fs");
	Dog d2 = Dog("lab", "pugy", 23, "fd");
	Dog d3 = Dog("lab32", "pugy", 23, "");
	Controller c1 = Controller();
	cout<<"For d1: \t"<<c1.add(d1);
	cout<<  endl<<"For d2: \t" <<c1.add(d2);

	cout<< endl<< "For d3: \t"  << c1.add(d3);
	*/

	{
		Ui ui = Ui();
		ui.run();
	}
	
	_CrtDumpMemoryLeaks();
	cout << "\n";
	system("pause");
	return 0;
}