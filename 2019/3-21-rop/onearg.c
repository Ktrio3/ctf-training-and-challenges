#include <stdio.h>
#include <stdlib.h>

int called_1 = 0;
int called_2 = 0;
int called_3 = 0;

void f1(int a, int b)
{
	if(a == 0xdeadbeef && b == 0xcafebabe)
	{
		printf("Huh, you know how to ROP with args now?\n");
		system("/bin/sh");
	}
}

void bof()
{		
	char s[4];
	printf("Give me a 4 byte string to place at %p: ", s);
	gets(s);
}


int main()
{
	bof();
	printf("Still here, eh?");

	return 0;
}