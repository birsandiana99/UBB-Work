#include "MapIterator.h"
#include <exception>
MapIterator::MapIterator(const Map & m):map{ m }{

}

void MapIterator::first()
{
	this->index = 0;
	while (this->map.T[this->index] == NULL_TVALUE)
		++this->index;
}

void MapIterator::next()
{
	if (valid() == 0) {
		throw std::invalid_argument("Invalid iterator");
	}
	++this->index;
	while (this->map.T[this->index] == NULL_TVALUE && this->index<=this->map.m)
		++this->index;
}

bool MapIterator::valid() const
{
	
	if (this->index >= this->map.m || this->map.mapSize==0)
		return false;
	return true;
}

TElem MapIterator::getCurrent() const
{
	if (valid() == 0) {
		throw std::invalid_argument("Invalid iterator");
	}
	auto pair = std::make_pair(this->map.T[index], this->map.values[this->index]);
	return pair;
}
