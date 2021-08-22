#pragma once
#include "Map.h"

typedef int TKey;

typedef int TValue;


typedef std::pair<TKey, TValue> TElem;
//unidirectional iterator for a container
class Map;
class MapIterator{
	friend class Map;
	private:
		
		int index;
		const Map& map;

public:

	MapIterator(const Map& c);

	void first();
	

	void next();


	bool valid() const;


	TElem getCurrent() const;



};


