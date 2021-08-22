#include <iostream>
#include <stdlib.h>
#include "DLL.h"
#include "ShortTest.h"
#include "ExtendedTest.h"
using namespace std;
int main()
{
	//DLL l = DLL(); l.testList();


	testAll();
	testAllExtended();
	system("pause");
	return 0;
}