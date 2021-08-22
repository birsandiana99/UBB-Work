#include <stdio.h>>
int detMin(int, int);
//Read a string of unsigned numbers in base 10 from keyboard. Determine the minimum value of the string and write it in the file min.txt (it will be created) in 16 base.
int main() {
	int a, b, n, c;
	printf("Din cate numere fac minimul? ");
	scanf("%d", &n);
	printf("Introduceti numerele.\n");
	scanf("%d", &a);
	n--;
	while (n > 0) {
		scanf("%d", &b);
		c = detMin(a, b);
		a = c;
		n--;
	}
	fprintf(fopen("min.txt", "w"), "%x", a);
	return 0;
}