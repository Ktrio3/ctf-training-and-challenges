#include <stdio.h>
#include <stdarg.h>

// this function will take the number of values to average
// followed by all of the numbers to average
// Taken from https://www.cprogramming.com/tutorial/lesson17.html
double average ( int num, ... )
{
  va_list arguments;                     // A place to store the list of arguments
  double sum = 0;

  va_start ( arguments, num );           // Initializing arguments to store all values after num
  for ( int x = 0; x < num; x++ )        // Loop until all numbers are added
    sum += va_arg ( arguments, int ); // Adds the next value in argument list to sum.
  va_end ( arguments );                  // Cleans up the list

  return sum / num;                      // Returns the average
}

int main(int argc, char const *argv[])
{
	double avg1 = average(3, 100, 250, 275);
	double avg2 = average(5, 1, 2, 3, 4, 5);
	printf("Average of [%d, %d, %d] is %f\n", 100, 250, 275, avg1);
	printf("Average of [%d, %d, %d, %d, %d] is %f\n", 1, 2, 3, 4, 5, avg2);
	return 0;
}