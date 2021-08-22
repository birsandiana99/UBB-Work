#include "Map.h"
#include <iostream>
#include "ShortTest.h"
#include "ExtendedTest.h"
using namespace std;
int main() {
	
	/*Map m;
	m.add(3, 4);
	m.add(8, 5);
	m.add(9, 5);
	m.add(10, 5);
	m.add(11, 5);

	cout << m.add(8, 9)<<endl;
	cout << m.size()<<endl;
	cout << m.search(3);

	cout << endl<<m.remove(11);
	cout << endl << m.search(11);

	cout << endl << "now we are iterating the list:" << endl;
	MapIterator i = m.iterator();
	while (i.valid() == true) {
		cout << i.getCurrent().first<<" " <<i.getCurrent().second << endl;
		i.next();
	}*/


	//testAll();
	testAllExtended();
	cout << "gata";
	system("pause");
	return 0;
}