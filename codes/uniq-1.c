#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a = 0;
    int i, j;
    int *mas = NULL;
    int size = 0;
    while (a != -1)
    {
        if (scanf("%d", &a) == 1)
        {
            mas = realloc(mas, ++size);
            mas[size - 1] = a;
        }
    }
    for (i = 0, j = size - 2; i <= j; i++, j--)
    {
        if (i == j)
        {
            printf("%d", mas[i]);
            printf("\n");
        }
        else
        {
            printf("%d %d ", mas[i], mas[j]);
        }
    }
    return 0;
}
// int *sort(int *mas, int size);

// int main()
// {
//     int a = 0;
//     int *mas = NULL;
//     int size = 0;
//     while (a != -1)
//     {
//         if (scanf("%d", &a) == 1)
//         {
//             mas = realloc(mas, ++size);
//             mas[size - 1] = a;
//         }
//     }

//     sort(mas, size);

//     for (int i = 0; i < size - 1; i++)
//     {
//         if (mas[i] != mas[i + 1])
//         {
//             if (i == size - 2)
//                 printf("%d", mas[i]);
//             else
//                 printf("%d ", mas[i]);
//         }
//     }
//     free(mas);
//     return 0;
// }

// int *sort(int *mas, int size)
// {
//     int temp;
//     for (int i = 0; i < size - 1; i++)
//     {
//         for (int j = i + 1; j < size - 1; j++)
//         {
//             if (mas[i] > mas[j])
//             {
//                 temp = mas[i];
//                 mas[i] = mas[j];
//                 mas[j] = temp;
//             }
//         }
//     }
//     return mas;
// }