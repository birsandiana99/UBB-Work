#include "Matrix.h"
#include <iostream>
#include <stdlib.h>
#include "ShortTest.h"
#include "ExtendedTest.h"
#include "MatrixIterator.h"
using namespace std;

int main() {
	
	Matrix m = Matrix(10, 10);
	m.modify(1,3,5);
	m.modify(2, 3, 6);
	m.modify(4, 3, 7);
	m.modify(8, 3, 8);
	m.modify(9, 3, 9);
	cout<<m.element(8, 3);
	//cout << m.find(2, 3);
	cout << endl;
	/*MatrixIterator it = m.iteratorCol(3);
	while (it.valid())
	{
		cout << it.getCurrent()<<endl;
		it.next();
	}
	
	*/
	/*
	cout<<"Old elem: "<<m.modify(1, 1, 5);
	cout<<"\nNew elem: "<<m.element(1, 1)<<endl;
	m.modify(1, 1, 0);
	cout << "\nNew elem(0): " << m.element(1, 1)<<endl;
	cout << "Nr lines: " << m.nrLines()<<endl;
	cout << "Nr cols: " << m.nrCols();
	

	m.modify(1, 1, 5);
	m.modify(2, 3, 7);
	m.modify(1, 3, 8);
	cout<<m.element(1, 3);
	m.modify(1, 3, 0);
	m.modify(1, 1, 7);
	cout<<"\n"<<m.element(1, 3);

	*/

	testAll();
	testAllExtended();


	cout << endl;
	system("pause");
	return 0;
}

