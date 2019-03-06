#include<stdio.h>

int main()
{
	int i, j, k;

	printf("TYPES: \n");
	printf("The %%d modifier (arg 100): %d\n", 100);
	printf("The %%c modifier (arg 'A'): %c\n", 'A');
	printf("The %%c modifier (arg 0x41): %c\n", 0x41);
	printf("The %%x modifier (arg 100): %x\n", 100);
	printf("The %%s modifier (arg \"Hello\"): %s\n", "Hello");
	printf("The %%p modifier (arg &i): %p\n", &i);
	printf("The %%n modifier: ");
	printf("Hello%n there%n, General Kenobi!%n\n", &i, &j, &k);
	printf("\t %d chars by 'Hello', %d chars by 'there', %d at the end\n", i, j, k);

	printf("\nWIDTH: \n");
	printf("The %%10d modifier (arg 100): %10d\n", 100);
	printf("The %%20d modifier (arg 100): %20d\n", 100);
	printf("The %%010d modifier (arg 100): %010d\n", 100);

	printf("\nPARAMETER: \n");
	printf("(%%1$d, %%2$d, %%3$d) (arg 1, 2, 3): (%1$d, %2$d, %3$d)\n", 1, 2, 3);
	printf("(%%3$d, %%2$d, %%1$d) (arg 1, 2, 3): (%3$d, %2$d, %1$d)\n", 1, 2, 3);

	//Note that these three make the compiler spit forth some warnings
	printf("(%%3$d, %%3$d, %%3$d) (arg 1, 2, 3): (%3$d, %3$d, %3$d)\n", 1, 2, 3);
	printf("Whoops... (%%4$d, %%5$d, %%6$d) (arg 1, 2, 3): (%4$d, %5$d, %6$d)\n", 1, 2, 3);
	printf("Whoops... (%%1$d, %%2$d, %%3$d) (No args): (%1$d, %2$d, %3$d)\n");

	printf("\nAll together now! (%%3$05d, %%2$10d, %%1$03d) args (1, 2, 3): (%3$05d, %2$10d, %1$03d)\n", 1, 2, 3);
}