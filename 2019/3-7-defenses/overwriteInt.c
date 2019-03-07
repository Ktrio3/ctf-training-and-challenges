#include <stdio.h>
#include <time.h>
#include <stdlib.h>

void overwriteInt()
{
	srand(time(NULL));  // Get a psuedo-random seed
	int i = rand();	// Get a pseudo-random number
	char s[4];
	char c;
	int j = 0;

	printf("Variable i is %d or 0x%x at %p\n", i, i, &i);
	printf("Your string is at%p\n", s);

	printf("%s", "Give me a string: ");
	c = getchar();
	while(c != '\n')
	{
		s[j] = c;
		j++;
		c = getchar();
	}

	printf("Variable i is 0x%x\n", i);
}


int main()
{
	overwriteInt();
	return 0;
}