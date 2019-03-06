#include <stdio.h>
#include <stdlib.h>

void call_me()
{
	system("/bin/sh");
}

void vuln(char a, char b)
{
	char c[40];

	printf("Give me a format string %c%c :", a, b);
	gets(c);

	printf(c);
	putchar('\n');
}

int main(int argc, char *argv[])
{
	vuln(':', ')');
}
