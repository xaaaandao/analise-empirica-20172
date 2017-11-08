import time

##
# Autor: Alexandre Yuji Kajihara e Clodoaldo Basaglia da Fonseca
# Descrição: aplicamos uma função para encontrar o máximo valor do subarranjo, é um dos menos eficiente.
# Data de criação: 07/11/2017
# Data de atualização: 07/11/2017
##

##
# Esta função enumeration(int vector[], int n) recebemos um vetor e seu tamanho 
# e aplicamos a função achando o máximo valor do subarranjo.
# Esse algoritmo é o menos eficiente para se procurar o máximo valor do subarranjo.
# @param vector, vetor do tipo de inteiro, que será aplicado a função enumeration().
# @param n, tipo de inteiro, que é o tamanho dos vetores.
# @return best, é um inteiro que retorna o melhor valor.
##
def enumeration(vector, n):
	i = j = k = 0
	best = count = 0
	while (i < n):
		j = i
		while (j < n):
			count = 0
			k = i
			while (k <= j):
				count = count + vector[k]
				k+=1
			if(count > best):
				best = count
			j+=1
		i+=1
	return best


def main():
	vector = [-448, -469, -7537, -997, -4960, 6576, 6375, -536, -5669, 7250, 5407, -1794, -4184, -4026, 7110, 6204, 2144, 1576, 2147, 950, -294, 285, 1320, -2588, 4110, 2481, 3738, 202, 4734, 7562, -7655, -3914, -1099, -7000, 3281, 2125, 7768, 1463, -6611, -6102, 513, 6988, 296, 4521, -5230, -794, 2524, 5106, -7411, -3522, -2137, 479, 4947, 7368, 6084, 857, 1656, 1629, -7142, -1810, 991, -6605, 2468, 8084, -5421, -2452, 2008, -5854, 7196, 3589, -3764, -484, 2385, 4717, -4156, 5347, -4270, 6560, 2252, -3489, -5162, -8086, 5175, 7969, 7474, 3066, 633, 930, -3506, 1683, 7312, 5677, 3270, 1579, 5560, 6041, 7319, -624, -8006, 6322, -5228, -3585, -2363, 5341, -7061, 1673, 2495, -3139, 33, -3454, 1556, 3055, -3347, -1462, 2831, -4074, -6597, -4728, 5048, -1910, 5147, 4159, -4434, 217, -2455, -7074, -1943, -3328]
	start = time.time()
	print("R: %d" % (enumeration(vector, len(vector))))
	end = time.time()
	print("O tempo em %f segundos" % (end - start))

if __name__ == '__main__':
	main()
