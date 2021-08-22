// SDA_Lab5.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include "TestP11.h"

int main()
{
	
	//list<int> mylist{ 1, 2, 3, 4, 5 , 6, 7, 8, 9, 10, 11, 12, 13, 14};
	
	
	// h = Heap(mylist);
	/*
	auto ite = mylist.begin();
	mylist.erase(ite);
	for (auto it = mylist.begin(); it != mylist.end(); ++it)
	{
		cout << *it << " ";
	}
	*/

	//Heap h = Heap();
	
	
	/*h.addElem(2);
	h.addElem(3);
	h.addElem(67);
	h.addElem(44);
	h.addElem(17);
	h.addElem(19);
	h.addElem(12);
	h.printEl();
	cout << endl << endl << endl;

	h.addElem(555);
	h.printEl();
	cout << endl << endl << endl;
	cout << endl<<"Acum facem remove:";
	cout<<h.remove();
	
	//h.addElem(897);


	h.printEl();

	*/
	/*
	cout << "Give me a kkk:";
	int k;
	cin >> k;

	int i = 1;
	auto it = mylist.begin();
	for ( ;it != mylist.end() && i<=k; ++it)
	{
		h.addElem(it);
		i++;
	}
	h.printEl();
	cout << endl;
	cout << "Iteratoru ii aici:" << *it;
	cout << endl << endl << endl;

	while (it != mylist.end())
	{
		cout << "It: " << *it << endl;

		if (*it < h.getRoot())
		{
			h.addElem(it);
			h.bubbleDown(0);
			//h.remove();
		}

		++it;
	}

	h.printEl();
	

	h.OurProb(mylist,k);

	*/


		//mylist.erase(h.returnInArray()[i]);
	/*
	for (auto it = mylist.begin(); it != mylist.end(); ++it)
	{
		cout << *it << " ";
	}
	*/

	testP11();
	system("pause");
	return 0;
}

