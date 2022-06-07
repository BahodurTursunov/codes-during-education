#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int calc(int r)
{
    int m, res = 0;
    while (r != 0)
    {
        m = r % 10;
        r = r / 10;
        if (m % 2 != 0)
        {
            if (res == 0)
            {
                res = abs(m);
            }
            else
            {
                res = abs(res * m);
            }
            printf("r = %d, m = %d, res = %d", r, m, res);
        }
        return res;
    }

    int main()
    {
        int r;
        char c;
        if (scanf("%d%c", &r, &c) == 2 && c == '\n')
        {
            printf("%d", calc(r));
        }
        else
        {
            printf("n/a");
        }
        return 0;
    }
