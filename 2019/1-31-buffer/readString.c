#include <stdio.h>

void getString()
{
	int i =0;	
	char s[12];
	s[10] = '\0';
	
	printf("Your string is at %p\n", s);
	printf("%s", "Give me 10 chars: ");
	while(i < 10)
	{
		s[i] = getchar();
		i++;
	}
	printf("%s\n", s);
}


int main()
{
	getString();
	return 0;
}