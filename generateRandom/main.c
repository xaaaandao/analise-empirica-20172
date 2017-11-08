#include <stdio.h>
#include <stdlib.h> /* Usado no atoi */

#define seed 10000

/**
* Autor: Alexandre Yuji Kajihara e Clodoaldo Basaglia da Fonseca
* Descrição: geramos valores aleatórios, com a quantidade que foi passad pelo usuário,
* e no intervalo desejado pelo usuário. Escolhemos a semente como sendo 100, pois
* foi o valor que percebemos que gerava mais valores positivos.
* Data de criação: 07/11/2017
* Data de atualização: 07/11/2017
*/

int main(int argc, char *argv[]){

	if(argc != 4){
		printf("use: %s minValue maxValue count\n", argv[0]);
		exit(1);
	}

	int minValue = atoi(argv[1]);
	int maxValue = atoi(argv[2]);
	int count = atoi(argv[3]);
	int i, positive = 0, negative = 0;
	
	srand(seed);  


	for(i = 0; i < count; i++){
		int number = rand() % (maxValue - minValue + 1) + minValue;
		if(number > 0)
			positive++;
		else
			negative++;
		if(i == 0)
			printf("%d", number);	
		else
			printf(", %d", number);	
	}

	/* printf("\nnumber of positive: %d\n", positive); 
	printf("number of negative: %d\n", negative); */

	return 0;
}
