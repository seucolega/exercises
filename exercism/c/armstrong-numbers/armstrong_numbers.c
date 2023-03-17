#include "armstrong_numbers.h"
#include <math.h>

bool is_armstrong_number(int candidate)
{
    int digits = (candidate == 0) ? 1 : log10(candidate) + 1;
    int toIterate = candidate;
    double sum = 0;

    while (toIterate != 0) {
        sum += pow(toIterate % 10, digits);
        toIterate /= 10;
    }

    return sum == candidate;
}
