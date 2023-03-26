#include "isogram.h"
#include <string.h>
#include <ctype.h>

char *normalize(char phrase[]) {
    int from = 0;
    int to = 0;

    while (phrase[from] != '\0') 
    {
        if (isspace(phrase[from]) || phrase[from] == '-')
        {
            ++from;
            continue;
        }
        phrase[to] = tolower(phrase[from]);
        ++to;
        ++from;
    }
    phrase[to] = '\0';

    return phrase;
}

bool is_isogram(const char phrase[])
{
    if (!phrase) {
        return false;
    }

    char p[24];
    strcpy(p, phrase);
    normalize(p);

    for (int i = 0; p[i] != '\0'; i++) 
    {
        for (int j = i + 1; p[j] != '\0'; j++) 
        {
            if (p[i] == p[j]) 
            {
                return false;
            }
        }
    }

    return true;
}
