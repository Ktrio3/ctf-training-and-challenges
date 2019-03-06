#include<stdio.h>
#include<stdlib.h>

#define SIZE 100 

void shell()
{
	system("/bin/sh");
}

void vuln(int *i)
{
	char in[SIZE];

	printf("Super secret hacker portal: \n");
	printf("Prove your way in: %p\n", i);

	fgets(in, SIZE, stdin);

	printf(in);
}


int main()
{
	int i = 100;

	vuln(&i);
	if(i == 0x1337)
	{
		puts("Hey, that's pretty good");
	}
	else if(i == 0xdeadbeef)
	{
		puts("Wow! A true, l33t hacker");
	}
	else if(i != 100)
	{
		puts("Eh. Decent\n");
	}
	else
	{
		puts("Try harder\n");
	}
	
}