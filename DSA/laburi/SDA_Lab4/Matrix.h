#pragma once
#include "MatrixIterator.h"


typedef int TElem;

#define NULL_TELEM 0

struct triple {
	int i;
	int j;
	TElem value;

};

class MatrixIterator;

class Matrix {



private:
	triple * elems;
	int * next;
	int cap;
	int lines, cols;
	int head;
	int firstEmpty;
	
	void resize();
	int insertAtPosition(triple elem, int pos);
	TElem find(int i, int j) const;
	void modifyElem(int i, int j, TElem newElem);
	int remove(int i,int j);
	void update(int i, int j, TElem newValue);

	friend class MatrixIterator;


public:

	//constructor

	//throws exception if nrLines or nrCols is negative or zero

	Matrix(int nrLines, int nrCols);



	//returns the number of lines

	int nrLines() const;



	//returns the number of columns

	int nrColumns() const;



	//returns the element from line i and column j (indexing starts from 0)

	//throws exception if (i,j) is not a valid position in the Matrix

	TElem element(int i, int j) const;



	//modifies the value from line i and column j

	//returns the previous value from the position

	//throws exception if (i,j) is not a valid position in the Matrix

	TElem modify(int i, int j, TElem e);


	MatrixIterator iteratorCol(int col) const;

	~Matrix();

};
