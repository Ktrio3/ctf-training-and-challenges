#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void shell()
{
	system("/bin/sh");
}

int main(int argc, char *argv[])
{
	char c[24] = "example of printf";
	if(argc >= 2)
	{
		strncpy(c, argv[1], 23);
	}

	printf("Th1s %sG%d%dD %s\n", "is a ", 0, 0, c);

	if(argc >= 3)
	{
		printf(argv[2], "is a ", 0, 0, c);
		printf("\n");
	}
	return 0;
}
