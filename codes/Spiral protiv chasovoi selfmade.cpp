#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int n,k,l = 0,w;
	scanf("%d", &n);
	int **a;
	w = n - 1;
	a = (int**)malloc(n * sizeof(int*));
	for (int g = 0; g < n; g++) {
		a[g] = (int*) malloc(n * sizeof(int));
	}
	int i = 0;
	int j = n - 1;
	
	for (k = 0; k < n*n; k++) {
		a[i][j] = k;
		if( i == l + 1 && j == w){w--;l++;}
		if( i == l && j > l){j--;continue;}
		if( j == l && i < w){i++;continue;}
		if( i == w && j < w){j++;continue;}
		if( j == w && i > l){i--;continue;} 
	}
	
	for(i = 0; i < n; i++) {
			for (j = 0; j < n; j++) {
				printf("%4d", a[i][j]);
			}
			printf("\n");
		}
	
	return 0;
}
