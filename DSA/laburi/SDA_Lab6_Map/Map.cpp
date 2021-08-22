#include "Map.h"

TValue Map::add(TKey c, TValue v)
{
	//if (c < 0)
	//	return NULL_TVALUE;
	if (this->firstFree == this->m) {
		//realloc
		this->firstFree = m+1;
		this->m *= 2;
		TValue* elements = new TValue[this->m];
		int *nextEls = new int[m];
		TKey *newT = new TKey[m];
		for (int i = 0; i < this->m; i++)
		{
				elements[i] = this->values[i];
				nextEls[i] = this->next[i];
				newT[i] = this->T[i];
		}

		delete[] this->values;
		values = elements;


		delete[] this->next;
		next = nextEls;


		delete[] this->T;
		T = newT;

		
	}

	int ix = this->h(c);
	
	if (this->T[ix] == NULL_TVALUE) {
		this->T[ix] = c;
		this->values[ix] = v;
		this->mapSize++;
		return NULL_TVALUE;
		
	}
	else
	{
		if (this->T[ix] == c)
		{
			//std::cout << "cazu asta";
			TValue oldValue = this->values[ix];
			this->values[ix] = v;
			return oldValue;
		}
		else
		{
			this->T[this->firstFree] = c;
			this->values[this->firstFree] = v;
			while (this->next[ix] != -1)
				ix = this->next[ix];
			this->next[ix] = firstFree;
			while (this->T[firstFree] != NULL_TVALUE && this->firstFree < this->m)
				firstFree++;
			
			return NULL_TVALUE;
		}
		
	}
}

TValue Map::search(TKey c) const
{
	int position = this->h(c);
	if (this->next[position] == -1)
	{
		if (this->T[position] == c)
		{
			return this->values[position];
		}
		else
			return NULL_TVALUE;
	}
	while (position!=-1 && this->T[position] != c && this->next[position] != -1) 
	{
		position = this->next[position];
	}
	if (this->T[position] == c) 
	{
		return this->values[position];
	}
	return NULL_TVALUE;
}

TValue Map::remove(TKey c)
{
	//removes a key from the map and returns the value associated with the key if
	//the key existed ot null: NULL_TVALUE otherwise
	TValue searchResult = search(c);
	if (searchResult == NULL_TVALUE || c == NULL_TVALUE)
		return NULL_TVALUE;
	
	int hashPosition = this->h(c);

	if (this->T[hashPosition] == c)
	{
		TValue valueRemoved = this->values[hashPosition];
		this->T[hashPosition] = NULL_TVALUE;
		this->values[hashPosition] = NULL_TVALUE;
		
		this->mapSize--;
		
		return valueRemoved;
	}
	if (this->next[hashPosition] == -1)
		return NULL_TVALUE;
	
	int nextPosition = this->next[hashPosition];

	while (this->T[nextPosition] != c && this->next[nextPosition] != NULL_TVALUE)
	{
		hashPosition = nextPosition;
		nextPosition = this->next[nextPosition];
	}

	//we check if we found it:

	if (this->T[nextPosition] == c)
	{
		this->next[hashPosition] = this->next[nextPosition];
		TValue oldElement = this->values[nextPosition];
		this->values[nextPosition] = NULL_TVALUE;

		this->mapSize--;

		return oldElement;

	}
}

int Map::size() const
{
	return this->mapSize;
}

bool Map::isEmpty() const
{
	return this->mapSize == 0;
}

MapIterator Map::iterator() const
{
	return MapIterator(*this);
}

void Map::init(int m)
{
	this->values = new TValue[m];
	this->next = new int[m];
	this->T = new TKey[m];

}

Map::Map()
{

	this->mapSize = 0;
	this->m = 10;
	this->values = new TValue[m];
	this->next = new int[m];
	this->T = new TKey[m];
	for (int i = 0; i < this->m; i++) {
		this->T[i] = NULL_TVALUE;
		this->values[i] = NULL_TVALUE;
		this->next[i] = -1;
	}
	this->firstFree = 0;
	
	
}

int Map::h(TKey k) const
{
	int x = k%this->m;
	if (x < 0)
		x = x * (-1);
	return x;
}


Map::~Map()
{
}
