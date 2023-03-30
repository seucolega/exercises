#include "grains.h"

#define RATIO 2
#define SQUARES 64

uint64_t square(uint8_t index)
{
    long result = RATIO;

    if (index < 2) 
    {
        result--;
    }

    for (uint8_t i = index - 1; i > 1; i--)
    {
        result *= RATIO;
    }
    
    return result;
}

uint64_t total(void)
{
    return square(SQUARES + 1) - 1;
}
