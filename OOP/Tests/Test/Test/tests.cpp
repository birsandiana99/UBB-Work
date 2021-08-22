#include "tests.h"
#include <assert.h>


tests::tests()
{
}

void tests::testAdd()
{
	Controller c = Controller();
	assert(c.add(Player("name1", "country1", "team1", 10))==1);
	c.add(Player("name2", "country1", "team2", 11));
	c.add(Player("name3", "country12", "team3", 19));
	c.add(Player("name4", "country21", "team1", 18));
	c.add(Player("name5", "country2", "team5", 17));
	assert(c.add(Player("name6", "country3", "team4", 16))==1);
	c.add(Player("name7", "country4", "team7", 15));
	c.add(Player("name8", "country5", "team10", 14));
	c.add(Player("name9", "country6", "team12", 13));
	c.add(Player("name10", "country1", "team1", 12));
	assert(c.getPlayers().getSize() == 10);
	assert(c.add(Player("name1", "country1", "team1", 10)) == -1);
	//c.add(Player("name10", "country1", "team1", 12));
	//assert(c.getPlayers().getSize() == 10);
	//c.add(Player("name111", "country1", "team1", 12));
	//assert(c.getPlayers().getSize() == 11);

}

void tests::testTotalGoalsCountry()
{
	Controller c = Controller();
	c.add(Player("name1", "country1", "team1", 10));
	c.add(Player("name2", "country1", "team2", 11));
	c.add(Player("name10", "country1", "team1", 12));
	c.add(Player("name3", "country12", "team3", 19));
	c.add(Player("name4", "country21", "team1", 18));
	c.add(Player("name5", "country2", "team5", 17));
	c.add(Player("name6", "country3", "team4", 16));
	c.add(Player("name7", "country4", "team7", 15));
	c.add(Player("name8", "country5", "team10", 14));
	c.add(Player("name9", "country6", "team12", 13));
	
	assert(c.totalGoalsCountry("country1") == 33);
	assert(c.totalGoalsCountry("country6") == 13);
	assert(c.totalGoalsCountry("fsj") == 0);
}

void tests::testAll()
{
	testAdd();
	testTotalGoalsCountry();
}


tests::~tests()
{
}
