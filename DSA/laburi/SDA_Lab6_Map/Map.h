#pragma once
#include <iostream>
#include "MapIterator.h"	
#define NULL_TVALUE -1

typedef int TKey;

typedef int TValue;

class MapIterator;

typedef std::pair<TKey, TValue> TElem;



struct Node {
	TKey key; //this is the key
	Node * next;
};

class Map {
	friend class MapIterator;
private:

	// representation of Map
	TKey * T;
	int *next;
	int *values;
	int m; //the size of t
	int firstFree;
	friend class MapIterator;
	int mapSize;
	void init(int m);

public:



	// implicit constructor

	Map();
	int h(TKey k) const;



	// adds a pair (key,value) to the map

	//if the key already exists in the map, then the value associated to the key is replaced by the new value and the old value is returned

	//if the key does not exist, a new pair is added and the value null is returned

	TValue add(TKey c, TValue v);



	//searches for the key and returns the value associated with the key if the map contains the key or null: NULL_TVALUE otherwise

	TValue search(TKey c) const;



	//removes a key from the map and returns the value associated with the key if the key existed ot null: NULL_TVALUE otherwise

	TValue remove(TKey c);



	//returns the number of pairs (key,value) from the map

	int size() const;



	//checks whether the map is empty or not

	bool isEmpty() const;



	//returns an iterator for the map

	MapIterator iterator() const;



	// destructor

	~Map();



};






