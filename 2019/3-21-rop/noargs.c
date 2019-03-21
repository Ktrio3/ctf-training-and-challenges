#include <stdio.h>
#include <stdlib.h>

int called_1 = 0;
int called_2 = 0;
int called_3 = 0;

void f1()
{
	called_1 = 0xdeadbeef;
	printf("Got the first one\n");
}

void f2()
{
	called_2 = 0x1337dad0;
	printf("Got the second one\n");
}

void f3()
{
	called_3 = 0xcafebabe;
	printf("Got the third one\n");
}

void test_it()
{
	if(called_1 == 0xdeadbeef)
	{
		
		if(called_2 == 0x1337dad0)
		{
			if(called_3 == 0xcafebabe)
			{
				printf("Hey, nice job! You called them all!\n");
				system("/bin/sh");
			}
		}
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