#include "MultiMap.h"



MultiMap::MultiMap()
{
	nrEl = 0;
	firstEmpty = 0;
	m = 10;
	T = new TElem[m + 1];
	next = new int[m + 1];
	for (int i = 0; i < m; i++)
	{
		next[i] = -1;
	}
}

int MultiMap::h(TKey k) const
{
	return k % m;
}

void MultiMap::add(TKey c, TValue v)
{
	int pos = h(c);
	if (T[pos].first == 0 && T[pos].second == 0)
		T[pos] = TElem(c, v);
	else
	{
		while (next[pos] != -1)
			pos = next[pos];

		T[firstEmpty] = TElem(c, v);
		next[pos] = firstEmpty;
	}

	++nrEl;
	computeNextEmpty();
}

bool MultiMap::remove(TKey c, TValue v)
{
	if (actuallyRemove(c, v, -1) == true)
	{
		--nrEl;
		return true;
	}

	return false;
}

bool MultiMap::actuallyRemove(TKey c, TValue v, int pozitie)
{
	int locDispersie, locatieE, preLocatieE = -1, locatieCandidat;

	locatieE = locDispersie = h(c);

	while (pozitie == -1 && locatieE != -1 && T[locatieE].first != c && T[locatieE].second != v)	//cazul1 in care elementul e este cel care se vrea sters, adica prima iteratie a functiei fsterge
		locatieE = next[locatieE];	//se gaseste pozitia lui exact in tabela 

	if (pozitie != -1)	//cazul2 cand elementul e este unul care ne incurca
		locatieE = pozitie;	//se da pozitia lui exacta in tabela

	if (pozitie == -1 && locatieE == -1)	// cazul in care elementul e nu exista
		return false;

	for (int i = 0; i < m; i++) {	// cautam predecesorul lui, cine trimite spre el, e valabil pentru cazul 2
		if (next[i] == locatieE)
			preLocatieE = i;
	}

	locatieCandidat = next[locatieE];	//	cine ar putea fi primul element care ne incurca

	if (locatieCandidat == -1) {	//	daca nu existe elemente care sa ne incurce, stergem simplu elementul pe care ne aflam
									//	aici putem ajunge doar daca elementul e este ultimul din lista lui sau singurul
		T[locatieE].first = 0;
		T[locatieE].second = 0;
		next[locatieE] = -1;

		if (preLocatieE != -1)		// daca e ultimul din lista si nu e singur in lista
			next[preLocatieE] = -1;

		computeNextEmpty();
	}
	else
	{
		while (locatieCandidat != -1 && h(T[locatieCandidat].first) != locatieE)
			locatieCandidat = next[locatieCandidat];



		if (locatieCandidat == -1) {
			if (preLocatieE != -1)
				next[preLocatieE] = next[locatieE];

			T[locatieE].first = 0;
			T[locatieE].second = 0;
			next[locatieE] = -1;

			computeNextEmpty();
			return true;
		}
		else {
			TElem save = T[locatieCandidat];
			actuallyRemove(T[locatieCandidat].first, T[locatieCandidat].second, locatieCandidat);
			T[locatieE] = save;
			return true;
		}
	}

	return true;
}

vector<TValue> MultiMap::search(TKey c) const
{
	vector<TValue> foundValues;
	int pos = h(c);
	while (pos != -1)
	{
		if (T[pos].first == c)
			foundValues.push_back(T[pos].second);
		pos = next[pos];
	}
	
	return foundValues;	
}

int MultiMap::size() const
{
	return nrEl;
}

bool MultiMap::isEmpty() const
{
	return nrEl == 0;
}

void MultiMap::computeNextEmpty()
{
	if (size() == 0)
	{
		// resize la cacaturi
		TElem *v = T;
		int lv = m;

		m = m * 2;
		T = new TElem[m];
		delete[] next;
		next = new int[m];

		for (int i = 0; i < m; ++i)
			next[i] = -1;

		nrEl = 0;
		firstEmpty = 0;
		for (int i = 0; i < lv; ++i)
			add(v[i].first, v[i].second);

		delete[] v;
		//firstEmpty = -1;
	}

	firstEmpty = 0;
	while (T[firstEmpty].first != 0 && T[firstEmpty].second != 0)
		++firstEmpty;
}

#include "MultiMapIterator.h"

MultiMapIterator MultiMap::iterator() const
{
	return MultiMapIterator(*this);
}


MultiMap::~MultiMap()
{
	delete[] T;
	delete[] next;
}
