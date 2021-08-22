#include "DynamicArray.h"
#include "Iterator.h"
#include "SortedSet.h"
#include "SortedSetIterator.h"
#include <stdio.h>
#include <iostream>
#include <assert.h>
#include "ShortTest.h"
#include "ExtendedTest.h"
using namespace std;

bool rel(TComp e1, TComp e2) {
	if (e1 <= e2) {
		return true;
	}
	else {
		return false;
	}
}

int main() {
	
	/*SortedSet s = SortedSet(rel);
	s.add(1);
	s.add(3);
	s.add(2);
	s.add(18);
	s.add(-1);
	s.add(5);
	s.add(15);
	s.add(6);
	s.add(7);
	s.add(-90);
	s.add(22);
	s.add(12);
	s.add(44);
	s.add(40);
	s.add(20);
	s.add(10);
	//cout << s.size();

	SortedSetIterator it2 = s.iterator();
	while (it2.valid())
	{
		//cout << 0;
		//cout << it.valid();
		cout << it2.getCurrent() << " ";
		it2.next();
	}
	cout << endl << endl;

	SortedSetIterator it = s.iterator();

	while (it.valid())
	{
		//cout << 0;
		//cout << it.valid();
		cout<<it.getCurrent()<<" ";
		it.jumpForward(5);
	}
	cout << endl << endl;

	s.remove(2);

	SortedSetIterator it2 = s.iterator();
	while (it2.valid())
	{
		//cout << 0;
		//cout << it.valid();
		cout << it2.getCurrent() << " ";
		it2.next();
	}
	
	*/
	testAll();

	testAllExtended();
	system("pause");
	return 0;
}