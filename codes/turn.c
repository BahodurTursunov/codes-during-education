#include <stdio.h>
#include <stdlib.h>

int** input(int N);
//  ПОВОРОТ МАТРИЦЫ ВЛЕВО - ВПРАВО на 90 ГРАДУСОВ
int main(void) {
    int N;
    scanf("%d", &N);
    int** mas = input(N);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (scanf("%d", &mas[i][j]) == 1) {
                continue;
            } else {
                printf("n/a");
                free(mas);
                return 0;
            }
        }
    }
    int** mas2 = input(N);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
//            mas2[j][i] = mas[i][N-j-1];
            mas2[j][i] = mas[N-i-1][j];
        }
    }
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (j == N - 1) {
                printf("%d", mas2[i][j]);
            } else {
                printf("%d ", mas2[i][j]);
            }
        }
        if (i != N - 1) {
            printf("\n");
        }
    }
    free(mas2);
    free(mas);
    return 0;
}

int** input(int N) {
    int** array = malloc(N * N * sizeof(int) + N * sizeof(int*));
    int* ptr = (int*)(array + N);
    for (int i = 0; i < N; i++) {
        array[i] = ptr + N * i;
    }
    return array;
}
