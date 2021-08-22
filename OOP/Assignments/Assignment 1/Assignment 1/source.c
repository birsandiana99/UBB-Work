#include <stdio.h>
#include <stdlib.h>

int citire()
{
	int y;
	scanf_s("%d", &y);
	return y;
}
void citire_vect(int n, int v[])
{
	int i;

	for (i = 0; i <= n - 1; i++)
	{
		printf("x = ");
		int x;
		x = citire();
		v[i] = x;
	}

}
int a(int x, int n)
{
	/*
	Calculates x to the power of n
	input: x and n, integers
	output: an integer representing x to the power of n
	*/

	int i = 1;
	int rez;
	rez = x;
	while (i<n)
	{
		rez = rez * x;
		i++;
	}
	return rez;
}

int prime(int n)
{
	if (n == 1 || n<0)
		return 0;
	if (n == 2)
		return 1;
	else
		if (n % 2 == 0)
			return 0;
		else
			for (int d = 3; d <= n / 2; d = d + 2)
				if (n%d == 0)
					return 0;
	return 1;
}


int b(int n, int v[], int v1[])
{
	/*
	Calculates the maximal sequence of consecutive elements that have contrary signs
	input: n - an integer value representing the number of elements in the vector
	v - an array of integers
	output: prints the maximal sequence, or if none, says there is no such sequence

	*/

	int count,i, lmax = 0, first = 0, last = 0;

	count = 1;
	for (i = 0; i<n-1; i++)
	{
		if (v[i] * v[i + 1] <0)
			count++;
		if (count>lmax)
			lmax = count;
		if (count == lmax)
		{
			first = i+1 - count + 1;
			last = i+1;
		}
		if (v[i] *v[i + 1] >0)
			count = 1;

	}
	int ct = 0;
	for (int j = first; j <= last-1; j++)
		v1[ct++] = v[j];

	return ct;

}

int c(int n, int v[], int v1[])
{
	int count, i, lmax = 0, first = 0, last = 0;

	count = 1;
	for (i = 0; i<n - 1; i++)
	{
		if (prime(v[i] + v[i + 1])==1)
			count++;
		if (count>lmax)
			lmax = count;
		if (count == lmax)
		{
			first = i + 1 - count + 1;
			last = i + 1;
		}
		if (prime(v[i] +v[i + 1]) == 0)
			count = 1;

	}
	int ct = 0;
	for (int j = first; j <= last - 1; j++)
		v1[ct++] = v[j];

	return ct;

}
void printMenu()
{
	printf("1. Show the value x^n. \n");
	printf("2. The maximum subsequence of opposite sign consecutive elements. \n");
	printf("3.  Given a vector of numbers, find the longest subsequence s two consecutive elements is a prime number \n");
	printf("0. To exit. \n");
}
void a_ui()
{
	int x;
	printf("x = ");
	x = citire();
	printf("n = ");
	int k = citire();
	int y = a(x, k);
	printf("%d \n", y);
}

void b_ui()
{/*
	int n=11;
	int v[] = { 1,-2,3,-3,-2,5,-6,7,-8,2 };
	int v1[11];*/
	int n;
	int v[100];
	int v1[100];
	printf("n = ");
	n = citire();
	
	printf("Introduceti elementele vectorului: ");
	citire_vect(n, v);
	n = n + 1;
	
	int l = b(n, v, v1);
	
	if (l == 0)
	{
		printf("nu exista o secventa maxima");
	}
	else
		for (int j = 0; j < l; j++)
			printf("%d ", v1[j]);
}

void c_ui()
{
/*	int n = 11;
	int v[] = { 1,2,4,4,3,2,1,2,3,8};
	int v1[11];*/

	int n;
	int v[100];
	int v1[100];
	printf("n = ");
	n = citire();

	printf("Introduceti elementele vectorului: ");
	citire_vect(n, v);

	
	int l = c(n, v, v1);

	if (l == 0)
	{
		printf("nu exista o secventa maxima");
	}
	else
		for (int j = 0; j < l; j++)
			printf("%d ", v1[j]);
}

int main()
{
	int optiune = 1;
	while (optiune != 0)
	{
		printMenu();
		optiune = citire();
		//printf("%d", optiune);
		if (optiune != 0)
		{

			if (optiune == 1)
			{
				a_ui();
				printf("\n");
			}
			else
			{
				if (optiune == 2)
				{
					b_ui();
					printf("\n");
				}
				else
				{
					if (optiune == 3)
					{
						c_ui();
						printf("\n");
					}

				}
			}

		}
	}











	return 0;
}
