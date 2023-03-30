#include "difference_of_squares.h"

unsigned int square(unsigned int base, unsigned int power)
{
    for (unsigned int i = 1; i < power; i++)
    {
        base *= base;
    }
    
    return base;
}

unsigned int sum_of_squares(unsigned int number)
{
    int result = 0;

    for (unsigned int i = 1; i <= number; i++)
    {
        result += square(i, 2);
    }

    return result;
}

unsigned int square_of_sum(unsigned int number)
{
    int result = 0;

    for (unsigned int i = 1; i <= number; i++)
    {
        result += i;
    }

    return square(result, 2);
}

unsigned int difference_of_squares(unsigned int number)
{
    return square_of_sum(number) - sum_of_squares(number);
}
