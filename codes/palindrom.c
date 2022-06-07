#include <stdio.h>
#include <stdlib.h>

int main()
{
    char *mas = malloc(1 * sizeof(char));
    int size = 0;
    char num = '\0';
    int flag = 1;
    int i, j;
    while (num != '\n')
    {
        if (scanf("%c", &num) == 1)
        {
            mas = realloc(mas, ++size);
            mas[size - 1] = num;
        }
        else
        {
            free(mas);
            printf("n/a");
            return 0;
        }
    }
    //  Проверка на палиндром
    for (i = 0, j = size - 2; i <= j; i++, j--)
    {
        if (mas[i] == mas[j] || mas[i] == mas[j] + 32 || mas[i] + 32 == mas[j])
        {
            continue;
        }
        else
        {
            flag = 0;
            break;
        }
    }
    if (flag == 1)
    {
        printf("YES");
    }
    else
    {
        printf("NO");
    }
    free(mas);
    return 0;
}
