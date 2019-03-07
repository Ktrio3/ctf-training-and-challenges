#include <stdio.h>
#include <stdlib.h>

void shell()
{
	system("/bin/sh");
}

void bof()
{		
	char s[4];
	printf("Give me a 4 byte string to place at %p: \n", s);
	gets(s);
	printf("%s", s);
	return;
}


int main()
{
	bof();
	printf("Let's see if you pwned me...\n");
	return 0;
}