#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *mas = malloc(1 * sizeof(int));
    int size = 0;
    int num = 0;
    int tmp = 0;
    // int flag = 1;
    int i, j;
    while (num != -1)
    {
        if (scanf("%d", &num) == 1)
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
    //  Сортировка массива по возрастанию
    for (int i = 0; i < size - 1; i++)
    {
        for (int j = i + 1; j < size - 1; j++)
        {
            if (mas[i] > mas[j])
                ё
                {
                    tmp = mas[j];
                    mas[j] = mas[i];
                    mas[i] = tmp;
                }
        }
    }
    //  Смена элементов массива (первый - последний - второй ...)
    for (i = 0, j = size - 2; i <= j; i++, j--)
    {
        if (i == j)
            printf("%d", mas[i]);
        else if (i + 1 == j)
            printf("%d %d", mas[i], mas[j]);
        else
            printf("%d %d ", mas[i], mas[j]);
    }
    //  Печать массива
    for (int i = 0; i < size - 1; i++)
    {
        if (i == size - 2)
            printf("%d", mas[i]);
        else
            printf("%d ", mas[i]);
    }
    free(mas);
    return 0;
}
