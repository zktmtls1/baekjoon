#include <stdio.h>
#include <stdlib.h>
int main(void)
{
	int N, M;
	scanf("%d %d", &N, &M);

	int* array = (int*)calloc(N, sizeof(int));
	if (array == NULL) exit(1);

	for (int i = 0; i < N; i++) array[i] = i+1;
	
	for (int a = 0; a < M; a++)
	{
		int c, d;
		scanf("%d %d", &c, &d);

		c = c - 1;
		d = d - 1;
		int temp;

		temp = array[c];
		array[c] = array[d];
		array[d] = temp;
	}
	for (int i = 0; i < N; i++) printf("%d ", array[i]);
	printf("\n");
	free(array);
	return 0;
}