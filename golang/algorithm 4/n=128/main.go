package main

/* Utilizado para imprimir */
import "fmt"
/* Utilizado para pegar o tempo */
import "time"

/**
* Autor: Alexandre Yuji Kajihara e Clodoaldo Basaglia da Fonseca
* Descrição: aplicamos uma função para encontrar o máximo valor do subarranjo, é utiliza o conceito de programação dinâmica.
* Data de criação: 07/11/2017
* Data de atualização: 07/11/2017
*/

/**
* Esta função maxValue(int x, int y) recebemos dois valores inteiros e retornar o 
* o maior entre os dois.
@param x, tipo de inteiro, que é será o valor comparado com y.
@param y, tipo de inteiro, que é será o valor comparado com x.
@return x or y, é um inteiro que retorna x se for maior que y, ou retorna y se for menor igual que x.
*/
func maxValue(x int, y int) int{
	if x > y{
		return x
	}
	return y
}

/**
* Esta função dynamicProgramming(int vector[]) recebemos um vetor que será aplicado 
* no algoritmo o máximo valor do subarranjo. Esse algoritmo é melhor que a função 
* dynamicProgramming para se procurar o máximo valor do subarranjo utilizando
* o conceito de programação dinâmica;
@param vector, vetor do tipo de inteiro, que será aplicado a função enumeration();
@return somatorio, é um inteiro que retorna o máximo do subarranjo.
*/
func dynamicProgramming(vector []int) int {
	var size, i, result int = len(vector) + 1, 0, 0
	solution := make([]int, size)
	
	for i = 0; i < size; i++{
		solution[i] = 0
	}

	for i = 1; i < size; i++{
		solution[i] = maxValue(solution[i-1]+vector[i-1], vector[i-1])
	}	

	result = solution[0]

	for i = 1; i < size; i++{
		if result < solution[i]{
			result = solution[i]
		}
	}

	return result
}

func main() {
	vector := []int{-448, -469, -7537, -997, -4960, 6576, 6375, -536, -5669, 7250, 5407, -1794, -4184, -4026, 7110, 6204, 2144, 1576, 2147, 950, -294, 285, 1320, -2588, 4110, 2481, 3738, 202, 4734, 7562, -7655, -3914, -1099, -7000, 3281, 2125, 7768, 1463, -6611, -6102, 513, 6988, 296, 4521, -5230, -794, 2524, 5106, -7411, -3522, -2137, 479, 4947, 7368, 6084, 857, 1656, 1629, -7142, -1810, 991, -6605, 2468, 8084, -5421, -2452, 2008, -5854, 7196, 3589, -3764, -484, 2385, 4717, -4156, 5347, -4270, 6560, 2252, -3489, -5162, -8086, 5175, 7969, 7474, 3066, 633, 930, -3506, 1683, 7312, 5677, 3270, 1579, 5560, 6041, 7319, -624, -8006, 6322, -5228, -3585, -2363, 5341, -7061, 1673, 2495, -3139, 33, -3454, 1556, 3055, -3347, -1462, 2831, -4074, -6597, -4728, 5048, -1910, 5147, 4159, -4434, 217, -2455, -7074, -1943, -3328}
	start := time.Now()
	fmt.Println("R:", dynamicProgramming(vector))	
	elapsed := time.Since(start)
	fmt.Printf("Tempo em %f segundos\n", elapsed.Seconds())
}
