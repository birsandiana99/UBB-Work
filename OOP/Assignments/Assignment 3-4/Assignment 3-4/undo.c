#include "undo.h"
#include "contr.h"

int undoOperation()
{
	/*
	Undo the last operation
	*/
		
	
	if (undo_depth == 0)
		return -1;
	int x = undo_op[undo_depth - 1].operationType;
	switch (x)
	{
		case opAdd:
		{
			char address[100];
			strcpy_s(address, strlen(undo_op[undo_depth - 1].lastOffer->address)+1, undo_op[undo_depth - 1].lastOffer->address);
			c_delete(address, -1);
			break;
		}
		default:
			return -1;
			break;
			
		case opDelete:
		{
			insert(offers, undo_op[undo_depth - 1].index, undo_op[undo_depth - 1].lastOffer);
		}
		break;

		case opUpdatePrice:
		{
			c_updatePrice(undo_op[undo_depth - 1].lastOffer->address, undo_op[undo_depth- 2].lastOffer->price, -1);
		}
		break;

		case opUpdateSurf:
		{
			c_updateSurface(undo_op[undo_depth - 1].lastOffer->address, undo_op[undo_depth - 2].lastOffer->surface, -1);
		}
		break;
	}


	redo_op[redo_depth].index = undo_op[undo_depth - 1].index;
	redo_op[redo_depth].lastOffer = undo_op[undo_depth - 1].lastOffer;
	redo_op[redo_depth].currentOffer = undo_op[undo_depth - 1].currentOffer;
	redo_op[redo_depth].operationType = undo_op[undo_depth - 1].operationType;
	

	redo_depth = redo_depth + 1;
	undo_depth = undo_depth - 1;

	return 1;
}

int redoOperation()
{
	/*
	Redo the last operation
	*/
	if (redo_depth == 0)
		return -1;
	int x = redo_op[redo_depth -1].operationType;
	switch (x)
	{
	case opAdd:
	{
		struct Offer *offer;
		offer = redo_op[redo_depth - 1].lastOffer;
		addOffer(offer->type, offer->address,offer->surface, offer->price, -1);
		
	}
	break;

	case opDelete:
	{
		//char address[100];

		//strcpy(address, strlen(redo_op[redo_depth - 1].lastOffer->address)+1, redo_op[redo_depth - 1].lastOffer->address);
		c_delete(redo_op[redo_depth - 1].lastOffer->address, -1);
	}
	break;

	case opUpdatePrice:
	{
		c_updatePrice(redo_op[redo_depth - 1].currentOffer->address, redo_op[redo_depth - 1].currentOffer->price, -1);
	}
	break;

	case opUpdateSurf:
	{
		c_updateSurface(redo_op[redo_depth - 1].currentOffer->address, redo_op[redo_depth - 1].currentOffer->surface, -1);
	}
	break;



	default:
		return -1;
		break;
	}


	
	redo_depth = redo_depth - 1;
	return 1;

}
