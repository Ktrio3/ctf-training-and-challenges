#include <stdio.h>
#include <stdlib.h>

struct User{
	char name[4];
	int admin;
};

int main()
{
	struct User p;
	p.admin = 0;
	char c;
	int j = 0;

	printf("%s", "Give me your username: ");
	c = getchar();
	while(c != '\n')
	{
		p.name[j] = c;
		j++;
		c = getchar();
	}

	if(p.admin != 0)
	{
		system("/bin/sh");
	}
	else
	{
		printf("Welcome %s!", p.name);
	}
	return 0;
}