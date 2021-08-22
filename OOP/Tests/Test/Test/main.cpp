#include "Player.h"
#include <iostream>
#include "Controller.h"
#include "UI.h"
#include <crtdbg.h>
using namespace std;
int main()
{
	/*
	Player p = Player("Isabelle Gullden", "SWE", "CSM Bucuresti", 80);
	cout << p.toString();
	cout << endl;
	*/
	/*Controller c = Controller();
	c.initialise();
	for (int i = 0; i < c.getPlayers().getSize(); i++)
		cout << c.getPlayers()[i].toString() << endl;
	cout << endl << endl;
	cout << c.totalGoalsCountry("ROU") << endl << endl;
	cout << c.showPlayers();
*/
	UI ui = UI();
	ui.run();
	_CrtDumpMemoryLeaks();
	system("pause");
	return 0;
}
