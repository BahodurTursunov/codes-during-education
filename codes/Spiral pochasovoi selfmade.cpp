#include <stdio.h>
#include <stdlib.h>
 
int main() {
	double n1;
	int n,k,i,j,l = 0, w;
	int **a;
	if ( scanf("%lf", &n1) == 1 && n1 == (int) n1 ) {
		n = (int) n1;
		w = n - 1;
		a = (int**)malloc(n * sizeof(int*));
		for (int g = 0; g < n; g++) {
			a[g] = (int*) malloc(n * sizeof(int));
		}
		i = 0;
		j = 0;
		for ( k = 0; k<n*n; k++ ){
			a[i][j] = k;
			if((i == (l+1)) && (j == l)){w--;l++;}
			if((j == w) && (i < w)){i++;continue;}
			if((i == l) && (j < w)){j++;continue;}
			if((i == w) && (j > l)){j--;continue;}
			if((j == l) && (i > l)){i--;continue;}		
		}
		for(i = 0; i < n; i++) {
			for (j = 0; j < n; j++) {
				printf("%4d", a[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}
