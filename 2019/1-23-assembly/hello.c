#include <stdio.h>

void printIt(int n)
{
	int i;
	for(i=0; i < n; i++) // Loop n times.
	{
		puts("Hello, exploitation meeting!\n"); // Print a string
	}
}

int main()
{
	printIt(10);
	return 0;
}
