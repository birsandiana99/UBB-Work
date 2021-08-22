#include "Player.h"



Player::Player()
{
}

Player::Player(string name, string nationality, string team, int goals)
{/*
	name = name;
	nationality = nationality;
	team = team;
	goals = goals;
	*/
	this->name = name;
	this->nationality = nationality;
	this->team = team;
	this->goals = goals;
}

string Player::getName()
{
	return this->name;
}

string Player::getNationality()
{
	return this->nationality;
}

string Player::getTeam()
{
	return this->team;
}

int Player::getGoals()
{
	return this->goals;
}

string Player::toString()
{
	string s = "";
	s += this->getName() + " | " + this->getNationality() + " | " + this->getTeam() + " | " + to_string(this->getGoals());
	return s;
}


Player::~Player()
{
}
