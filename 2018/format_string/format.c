#include <stdio.h>
#include <stdlib.h>

void shell()
{
	system("/bin/sh");
}

void vuln()
{
	char c[40];

	gets(c);

	printf(c);
}

int main(int argc, char *argv[])
{
	vuln();
}
