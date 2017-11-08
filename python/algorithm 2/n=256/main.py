import time

##
# Autor: Alexandre Yuji Kajihara e Clodoaldo Basaglia da Fonseca
# Descrição: aplicamos uma função para encontrar o máximo valor do subarranjo, é superior ao algoritmo um enumeration.
# Data de criação: 07/11/2017
# Data de atualização: 07/11/2017
##

##
# Esta função betterEnumeration(int vector[], int n) recebemos um vetor e o seu tamanho 
# e o algoritmo irá encontrar o máximo valor do subarranjo.
# Esse algoritmo é melhor que a função enumeration para se procurar o máximo valor do subarranjo.
#@param vector, vetor do tipo de inteiro, que será aplicado a função betterEnumeration().
#@param n, tipo de inteiro, que é o tamanho dos vetores.
#@return best, é um inteiro que retorna o melhor valor.
##
def betterEnumeration(vector, n):
	i = j = 0
	best = count = 0
	while (i < n):
		count = 0
		j = i
		while (j < n):
			count += vector[j]
			if(count > best):
				best = count
			j+=1
		i+=1
	return best


def main():
	vector = [-448, -469, -7537, -997, -4960, 6576, 6375, -536, -5669, 7250, 5407, -1794, -4184, -4026, 7110, 6204, 2144, 1576, 2147, 950, -294, 285, 1320, -2588, 4110, 2481, 3738, 202, 4734, 7562, -7655, -3914, -1099, -7000, 3281, 2125, 7768, 1463, -6611, -6102, 513, 6988, 296, 4521, -5230, -794, 2524, 5106, -7411, -3522, -2137, 479, 4947, 7368, 6084, 857, 1656, 1629, -7142, -1810, 991, -6605, 2468, 8084, -5421, -2452, 2008, -5854, 7196, 3589, -3764, -484, 2385, 4717, -4156, 5347, -4270, 6560, 2252, -3489, -5162, -8086, 5175, 7969, 7474, 3066, 633, 930, -3506, 1683, 7312, 5677, 3270, 1579, 5560, 6041, 7319, -624, -8006, 6322, -5228, -3585, -2363, 5341, -7061, 1673, 2495, -3139, 33, -3454, 1556, 3055, -3347, -1462, 2831, -4074, -6597, -4728, 5048, -1910, 5147, 4159, -4434, 217, -2455, -7074, -1943, -3328, 494, -1764, -5207, 3450, 2843, 623, 591, 3966, -5905, -5115, -7366, 2320, -376, 2374, -2818, 4461, -7280, -8187, -7806, -5685, -4723, 5427, 589, -7777, 1393, 4348, 632, 7131, 5466, 6882, -4398, -2241, -3075, -1413, -6992, 7952, 7394, 1791, 3725, -6711, 4869, 4543, 3801, -3708, -1276, -7217, -7440, -372, -7212, -7062, 2128, -3751, 6557, -5476, -3336, -242, 7056, 5481, -1304, 4321, 4162, 2490, -6121, -7106, -7124, -4920, -7355, -7930, 5055, 4554, -6449, 1723, 904, 5536, 6207, 7812, 6511, 6951, -752, 7483, 8082, -6825, -4469, 6446, -4109, 388, -1997, -5245, -2332, 4891, 7260, -6363, -820, -7053, -5285, 241, -3781, -4448, 503, -6927, -8087, 2246, 2989, 1001, -419, 995, 620, -2100, -246, 8052, -2818, -365, -6966, 898, -2120, -2890, -6907, 4076, 49, -1047, 766, -884, 782, 8139, 255, 3689, 179, 4658]
	start = time.time()
	print("R: %d" % (betterEnumeration(vector, len(vector))))
	end = time.time()
	print("O tempo em %f segundos" % (end - start))

if __name__ == '__main__':
	main()
