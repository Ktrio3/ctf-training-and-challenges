#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void vuln(char *c)
{
	char buf[10];
	strcpy(buf, c);
}

int main(int argc, char *argv[])
{
	if(argc < 2)
	{
		printf("Try again with a string\n");
		exit(-1);
	}
	vuln(argv[1]);
}
