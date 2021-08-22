#include "repo.h"
#include "domain.h"
#include "ui.h"
#include "contr.h"
#include <crtdbg.h>
#include <string.h>
#include <stdio.h>



int main()
{
	
	run();
	destroyArray(offers);
	_CrtDumpMemoryLeaks();
	return 0;
}