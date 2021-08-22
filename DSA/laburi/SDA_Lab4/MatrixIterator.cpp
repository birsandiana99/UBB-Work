#include "MatrixIterator.h"
#include <stdexcept>

MatrixIterator::MatrixIterator(int column,const Matrix &m): matrix(m)
{
	//T(1)
	this->col = column;
	this->index = 0;
}



TElem MatrixIterator::getCurrent() const
{
	//O(n)
	return matrix.element(this->index, this->col);
}

void MatrixIterator::next()
{
	//T(1)
	if (valid() == 0) {
		throw std::invalid_argument("Invalid iterator");
	}
	this->index++;
}

bool MatrixIterator::valid() const
{
	//T(1)
	return this->index < this->matrix.nrLines() && this->col < this->matrix.nrColumns();
}

void MatrixIterator::first()
{
	//T(1)
	this->index = 0;
}


