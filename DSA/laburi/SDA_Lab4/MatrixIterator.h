#pragma once
#include "Matrix.h"
typedef int TElem;
class MatrixIterator
{
public:
	int index;
	void next();
	void first();
	bool valid() const;
	TElem getCurrent() const;

private:
	friend class Matrix;
	MatrixIterator(int column,const Matrix& m);
	const Matrix& matrix;
	int col;
	
};

