#include "P11.h"
#include "Heap.h"
#include <stdexcept>
void removeMin(list<TElem>& elements, int k)
{
	Heap h = Heap();
	//exceptions here:

	//if k is less than or equal to 0, it throws an exception
	//if k is greater than the number of elements, all elements will be removed

	if (k <= 0)
		throw exception();// ("k must be greater than 0");
	if (k >= elements.size())
	{
		/*
		auto it = elements.begin();
		for (; it != elements.end(); ++it)
		{
			std::cout << *it << endl;
			elements.erase(it);
			
		}*/
		elements.clear();
	}
	else 
	{
		//
		int i = 1;
		auto it = elements.begin();
		for (; it != elements.end() && i <= k; ++it)
		{
			h.addElem(it);
			i++;
		}
		while (it != elements.end())
		{
			if (*it < h.getRoot())
			{
				h.addElem(it);
				h.bubbleDown(0);
			}

			++it;
		}
		h.OurProb(elements, k);
	}
}
