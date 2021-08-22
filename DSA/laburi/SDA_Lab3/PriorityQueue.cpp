#include "PriorityQueue.h"


PriorityQueue::PriorityQueue(Relation r)
{
	//Theta(1)
	this->relation = r;
}

void PriorityQueue::push(TElem e, TPriority p)
{	
	//O(n)
	int pos = 1;
	if (this->dll.isEmpty())
		this->dll.insertLast(Element(e, p));
	else
	{
		while (pos <= this->dll.size() && Element(e, p) != this->dll.getElement(pos) && this->relation(this->dll.getElement(pos).second, p)) {
			pos++;
		}
//		if (pos == this->dll.size())
	//		this->dll.insertLast(Element(e, p));
		//else
			this->dll.insertAtPosition(Element(e, p), pos);
	}
}

Element PriorityQueue::top() 
{
	//Theta(1)
	if(this->isEmpty())
		throw std::invalid_argument("Queue is empty!");
	/*
	else
	{
		int i = 1;
		int maxPriority = 0;
		int maxPriorityIndex = -1;
		while (i <= this->size())
		{
			if (this->dll.getElement(i).second > maxPriority)
			{
				maxPriority = this->dll.getElement(i).second;
				maxPriorityIndex = i;
			}
			i++;
		}
		return this->dll.getElement(maxPriorityIndex);*/

	return this->dll.getFirst()->data;
}

Element PriorityQueue::pop()
{
	//Theta(1)
	if (this->isEmpty())
		throw std::invalid_argument("Queue is empty!");

	Element elem = this->dll.getFirst()->data;
	//this->dll.deleteElement(this->dll.getFirst()->data);
	this->dll.deleteFirst();

	return elem;
}

bool PriorityQueue::isEmpty() 
{
	//Theta(1)
	if (dll.isEmpty() == true)
		return true;
	else
		return false;
	
}

int PriorityQueue::size()
{ 
	//O(n)
	return this->dll.size();
}

bool PriorityQueue::search(Element elem) const
{
	//O(n)
	int x = this->dll.search(elem);
	if (x > this->dll.Size())
		return false;
	else
		return true;

}


PriorityQueue::~PriorityQueue()
{
}



