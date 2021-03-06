/**
* Autor: Alexandre Yuji Kajihara e Clodoaldo Basaglia da Fonseca
* Descrição: aplicamos uma função para encontrar o máximo valor do subarranjo, é utiliza o conceito de divisão e conquista.
* Data de criação: 07/11/2017
* Data de atualização: 07/11/2017
*/

public class Subarraymax{
	/**
	* Esta função divideAndConquer(int vector[], int start, int end) recebemos um vetor que será aplicado 
	* no algoritmo o máximo valor do subarranjo, a posição inicial 
	* e a posição final do vetor. Esse algoritmo é melhor que a função 
	* divideAndConquer para se procurar o máximo valor do subarranjo utilizando
	* o conceito de divisão e conquista.
	@param vector, vetor do tipo de inteiro, que será aplicado a função divideAndConquer().
	@param start, tipo de inteiro, que é a posição inicial do vetor.
	@param end, tipo de inteiro, que é a posição final do vetor.
	@return maxLeft + maxRight or max(divideAndConquer(vector, start, middle), divideAndConquer(vector, middle + 1, end)), é um inteiro que retorna um desses valores valor.
	*/
	public static int divideAndConquer(int []vector, int start, int end){
		int i = 0, count, middle, maxLeft, maxRight;
		if(start > end) {
			return 0;
		}
		
		if(start == end) {
			return Math.max(0, vector[start]);
		}
		
		middle = (start + end) / 2;
		
		maxRight = 0;
		count = 0;
		i = middle;
		while(i >= start){
			count = count + vector[i];
			if(count > maxRight){
				maxRight = count;
			}
			i--;
		}
		
		maxLeft = 0;
		count = 0;
		i = middle + 1;
		while(i <= end) {
			count = count + vector[i];
			if(count > maxLeft){
				maxLeft = count;
			}
			i++;
		}
		
		return Math.max(maxLeft + maxRight, Math.max(divideAndConquer(vector, start, middle), divideAndConquer(vector, middle + 1, end)));
		
	}

	public static void main(String []argv){
		int []vector = {-448, -469, -7537, -997, -4960, 6576, 6375, -536, -5669, 7250, 5407, -1794, -4184, -4026, 7110, 6204, 2144, 1576, 2147, 950, -294, 285, 1320, -2588, 4110, 2481, 3738, 202, 4734, 7562, -7655, -3914, -1099, -7000, 3281, 2125, 7768, 1463, -6611, -6102, 513, 6988, 296, 4521, -5230, -794, 2524, 5106, -7411, -3522, -2137, 479, 4947, 7368, 6084, 857, 1656, 1629, -7142, -1810, 991, -6605, 2468, 8084, -5421, -2452, 2008, -5854, 7196, 3589, -3764, -484, 2385, 4717, -4156, 5347, -4270, 6560, 2252, -3489, -5162, -8086, 5175, 7969, 7474, 3066, 633, 930, -3506, 1683, 7312, 5677, 3270, 1579, 5560, 6041, 7319, -624, -8006, 6322, -5228, -3585, -2363, 5341, -7061, 1673, 2495, -3139, 33, -3454, 1556, 3055, -3347, -1462, 2831, -4074, -6597, -4728, 5048, -1910, 5147, 4159, -4434, 217, -2455, -7074, -1943, -3328, 494, -1764, -5207, 3450, 2843, 623, 591, 3966, -5905, -5115, -7366, 2320, -376, 2374, -2818, 4461, -7280, -8187, -7806, -5685, -4723, 5427, 589, -7777, 1393, 4348, 632, 7131, 5466, 6882, -4398, -2241, -3075, -1413, -6992, 7952, 7394, 1791, 3725, -6711, 4869, 4543, 3801, -3708, -1276, -7217, -7440, -372, -7212, -7062, 2128, -3751, 6557, -5476, -3336, -242, 7056, 5481, -1304, 4321, 4162, 2490, -6121, -7106, -7124, -4920, -7355, -7930, 5055, 4554, -6449, 1723, 904, 5536, 6207, 7812, 6511, 6951, -752, 7483, 8082, -6825, -4469, 6446, -4109, 388, -1997, -5245, -2332, 4891, 7260, -6363, -820, -7053, -5285, 241, -3781, -4448, 503, -6927, -8087, 2246, 2989, 1001, -419, 995, 620, -2100, -246, 8052, -2818, -365, -6966, 898, -2120, -2890, -6907, 4076, 49, -1047, 766, -884, 782, 8139, 255, 3689, 179, 4658, 7425, -7511, 5924, 7522, 2919, 712, 330, -5693, -6486, -7251, 391, 1452, -7399, 5758, -7114, -6181, -1537, -1041, -879, -260, -5158, 7362, 6877, 3792, -1714, -542, 3738, 6733, -5054, -4284, 3199, -5822, -3603, 922, -6493, 7500, -6559, 2021, -6393, -4861, 2962, 2190, 4784, 3747, -253, 5862, 5759, 6402, -3380, -3313, -2059, -354, -4151, -3375, -4754, 2327, 4275, 7168, 859, 7413, -5308, -4143, -6610, -727, 4971, -4919, -1427, 6596, 5294, 372, -6457, 56, -5639, 6511, -4390, 2301, 4172, -6832, 502, -7400, -1952, 6636, 438, 2089, -4932, 3868, -3785, 7528, 2844, 5258, 6748, 5720, -7077, -8062, -3200, 6078, -4789, 3565, 4482, -7695, -4264, 6209, 553, -1710, 4527, 4347, -7610, 506, 5708, 1084, 1290, -4445, -481, -6472, 5828, 2772, 5588, -6158, 2107, 231, 7292, 654, -2242, -7986, 784, 2743, 6285, 4180, -1893, 2566, 4677, 2028, 582, -2963, -7875, -3084, -6817, -7301, 5606, 7075, 1967, -1304, -5563, -6706, 416, -7936, 4250, -2197, -5902, -1836, 6227, -6810, 7002, -4216, -6604, -406, 6711, 7873, -4419, -3374, 2246, -7935, 6838, -5373, -2714, 7155, -273, -1347, 8038, -2867, -2464, 1812, 4021, 165, 3290, -3764, 414, -653, 2231, 2704, 5695, 257, 4086, 4505, 4226, 5675, -4102, 2744, 5347, -337, 7554, -607, -88, 6199, 2204, 5382, 5153, -6261, -4158, 4998, -936, 1570, -1390, -5116, -6465, -6293, -688, 2141, 1239, -6658, -3348, -1259, 1792, -7462, -4955, -2183, 6397, -865, -7640, 3543, 6990, 8107, -5265, -1299, 6105, 5132, -4110, 3058, 7063, -75, -145, -2074, -6698, 6657, 1002, -4971, -7836, -7879, 5362, 1595, -6353, -6186, -7865, 3623, -5464, -4627, -6753, -7268, 2692, -6200, 4467, 1482, -6294, 7395, -8010, 7995};
		long startTime = System.nanoTime();
		System.out.println("R: " + divideAndConquer(vector, 0, vector.length - 1));
		long endTime = System.nanoTime();
		long duration = endTime - startTime;
		double convertToSeconds = (double)duration / 1000000000.0;
	    System.out.printf("Tempo em %f segundos\n", convertToSeconds);
	}
}