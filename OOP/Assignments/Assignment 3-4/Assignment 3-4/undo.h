#pragma once
#include "domain.h"

enum op_type
{
	opAdd,
	opDelete,
	opUpdateSurf,
	opUpdatePrice
};

struct operation
{
	int operationType;
	struct Offer *lastOffer;
	struct Offer *currentOffer;
	int index;
}undo_op[1000],redo_op[1000];

int undo_depth;
int redo_depth;


int undoOperation();
int redoOperation();


