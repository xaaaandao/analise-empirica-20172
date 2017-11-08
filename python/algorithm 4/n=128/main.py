import time

# Utilizado no array #
import array

##
# Autor: Alexandre Yuji Kajihara e Clodoaldo Basaglia da Fonseca
# Descrição: aplicamos uma função para encontrar o máximo valor do subarranjo, é utiliza o conceito de divisão e conquista.
# Data de criação: 07/11/2017
# Data de atualização: 07/11/2017
##

##
# Esta função max(int x, int y) recebemos dois valores inteiros e retornar o 
# o maior entre os dois.
#@param x, tipo de inteiro, que é será o valor comparado com y.
#@param y, tipo de inteiro, que é será o valor comparado com x.
#@return x or y, é um inteiro que retorna x se for maior que y, ou retorna y se for menor igual que x.
##
def maxValue(x, y):
	if(x > y):
		return int(x)
	return int(y)

##
# Esta função dynamicProgramming(int vector[]) recebemos um vetor que será aplicado 
# no algoritmo o máximo valor do subarranjo. Esse algoritmo é melhor que a função 
# dynamicProgramming para se procurar o máximo valor do subarranjo utilizando
# o conceito de programação dinâmica;
#@param vector, vetor do tipo de inteiro, que será aplicado a função enumeration();
#@return somatorio, é um inteiro que retorna o máximo do subarranjo.
##
def dynamicProgramming(vector):
	i = result = 0
	size = len(vector) 

	solution = array.array('i', (0 for i in range(0, len(vector))))

	i = 1
	while(i < size):
		solution[i] = maxValue(solution[i-1]+vector[i-1], vector[i-1])
		i+=1

	result = solution[0]

	i = 1
	while(i < size):
		if(result < solution[i]):
			result = solution[i]
		i+=1

	return result



def main():
	vector = [-448, -469, -7537, -997, -4960, 6576, 6375, -536, -5669, 7250, 5407, -1794, -4184, -4026, 7110, 6204, 2144, 1576, 2147, 950, -294, 285, 1320, -2588, 4110, 2481, 3738, 202, 4734, 7562, -7655, -3914, -1099, -7000, 3281, 2125, 7768, 1463, -6611, -6102, 513, 6988, 296, 4521, -5230, -794, 2524, 5106, -7411, -3522, -2137, 479, 4947, 7368, 6084, 857, 1656, 1629, -7142, -1810, 991, -6605, 2468, 8084, -5421, -2452, 2008, -5854, 7196, 3589, -3764, -484, 2385, 4717, -4156, 5347, -4270, 6560, 2252, -3489, -5162, -8086, 5175, 7969, 7474, 3066, 633, 930, -3506, 1683, 7312, 5677, 3270, 1579, 5560, 6041, 7319, -624, -8006, 6322, -5228, -3585, -2363, 5341, -7061, 1673, 2495, -3139, 33, -3454, 1556, 3055, -3347, -1462, 2831, -4074, -6597, -4728, 5048, -1910, 5147, 4159, -4434, 217, -2455, -7074, -1943, -3328]
	start = time.time()
	print("R: %d" % (dynamicProgramming(vector)))
	end = time.time()
	print("O tempo em %f segundos" % (end - start))

if __name__ == '__main__':
	main()
