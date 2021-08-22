#pragma once
#include <string>
using namespace std;

class Player
{
public:
	Player();
	Player(string name, string nationality, string team, int goals);
	string getName();
	string getNationality();
	string getTeam();
	int getGoals();
	string toString();

	~Player();
private:
	string name;
	string nationality;
	string team;
	int goals;
};

