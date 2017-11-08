import time

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
		return x
	return y

##
# Esta função divideAndConquer(int vector[], int start, int end) recebemos um vetor que será aplicado 
# no algoritmo o máximo valor do subarranjo, a posição inicial 
# e a posição final do vetor. Esse algoritmo é melhor que a função 
# divideAndConquer para se procurar o máximo valor do subarranjo utilizando
# o conceito de divisão e conquista.
#@param vector, vetor do tipo de inteiro, que será aplicado a função divideAndConquer().
#@param start, tipo de inteiro, que é a posição inicial do vetor.
#@param end, tipo de inteiro, que é a posição final do vetor.
#@return maxLeft + maxRight or max(divideAndConquer(vector, start, middle), divideAndConquer(vector, middle + 1, end)), é um inteiro que retorna um desses valores valor.
##
def divideAndConquer(vector, start, end):
	i = count = middle = maxRight = maxLeft = 0

	if(start > end):
		return 0

	if(start == end):
		return maxValue(0, vector[start])

	middle = (start + end) // 2

	maxLeft = 0
	count = 0
	i = int(middle)
	while(i >= start):
		count = count + vector[i]
		if(count > maxLeft):
			maxLeft = count
		i-=1

	maxRight = 0
	count = 0
	i = int(middle + 1)
	while(i <= end):
		count = count + vector[i]
		if(count > maxRight):
			maxRight = count
		i += 1

	return maxValue(maxRight + maxLeft, maxValue(divideAndConquer(vector, start, middle), divideAndConquer(vector, middle+1, end)))

def main():
	vector = [-448, -469, -7537, -997, -4960, 6576, 6375, -536, -5669, 7250, 5407, -1794, -4184, -4026, 7110, 6204, 2144, 1576, 2147, 950, -294, 285, 1320, -2588, 4110, 2481, 3738, 202, 4734, 7562, -7655, -3914, -1099, -7000, 3281, 2125, 7768, 1463, -6611, -6102, 513, 6988, 296, 4521, -5230, -794, 2524, 5106, -7411, -3522, -2137, 479, 4947, 7368, 6084, 857, 1656, 1629, -7142, -1810, 991, -6605, 2468, 8084, -5421, -2452, 2008, -5854, 7196, 3589, -3764, -484, 2385, 4717, -4156, 5347, -4270, 6560, 2252, -3489, -5162, -8086, 5175, 7969, 7474, 3066, 633, 930, -3506, 1683, 7312, 5677, 3270, 1579, 5560, 6041, 7319, -624, -8006, 6322, -5228, -3585, -2363, 5341, -7061, 1673, 2495, -3139, 33, -3454, 1556, 3055, -3347, -1462, 2831, -4074, -6597, -4728, 5048, -1910, 5147, 4159, -4434, 217, -2455, -7074, -1943, -3328, 494, -1764, -5207, 3450, 2843, 623, 591, 3966, -5905, -5115, -7366, 2320, -376, 2374, -2818, 4461, -7280, -8187, -7806, -5685, -4723, 5427, 589, -7777, 1393, 4348, 632, 7131, 5466, 6882, -4398, -2241, -3075, -1413, -6992, 7952, 7394, 1791, 3725, -6711, 4869, 4543, 3801, -3708, -1276, -7217, -7440, -372, -7212, -7062, 2128, -3751, 6557, -5476, -3336, -242, 7056, 5481, -1304, 4321, 4162, 2490, -6121, -7106, -7124, -4920, -7355, -7930, 5055, 4554, -6449, 1723, 904, 5536, 6207, 7812, 6511, 6951, -752, 7483, 8082, -6825, -4469, 6446, -4109, 388, -1997, -5245, -2332, 4891, 7260, -6363, -820, -7053, -5285, 241, -3781, -4448, 503, -6927, -8087, 2246, 2989, 1001, -419, 995, 620, -2100, -246, 8052, -2818, -365, -6966, 898, -2120, -2890, -6907, 4076, 49, -1047, 766, -884, 782, 8139, 255, 3689, 179, 4658, 7425, -7511, 5924, 7522, 2919, 712, 330, -5693, -6486, -7251, 391, 1452, -7399, 5758, -7114, -6181, -1537, -1041, -879, -260, -5158, 7362, 6877, 3792, -1714, -542, 3738, 6733, -5054, -4284, 3199, -5822, -3603, 922, -6493, 7500, -6559, 2021, -6393, -4861, 2962, 2190, 4784, 3747, -253, 5862, 5759, 6402, -3380, -3313, -2059, -354, -4151, -3375, -4754, 2327, 4275, 7168, 859, 7413, -5308, -4143, -6610, -727, 4971, -4919, -1427, 6596, 5294, 372, -6457, 56, -5639, 6511, -4390, 2301, 4172, -6832, 502, -7400, -1952, 6636, 438, 2089, -4932, 3868, -3785, 7528, 2844, 5258, 6748, 5720, -7077, -8062, -3200, 6078, -4789, 3565, 4482, -7695, -4264, 6209, 553, -1710, 4527, 4347, -7610, 506, 5708, 1084, 1290, -4445, -481, -6472, 5828, 2772, 5588, -6158, 2107, 231, 7292, 654, -2242, -7986, 784, 2743, 6285, 4180, -1893, 2566, 4677, 2028, 582, -2963, -7875, -3084, -6817, -7301, 5606, 7075, 1967, -1304, -5563, -6706, 416, -7936, 4250, -2197, -5902, -1836, 6227, -6810, 7002, -4216, -6604, -406, 6711, 7873, -4419, -3374, 2246, -7935, 6838, -5373, -2714, 7155, -273, -1347, 8038, -2867, -2464, 1812, 4021, 165, 3290, -3764, 414, -653, 2231, 2704, 5695, 257, 4086, 4505, 4226, 5675, -4102, 2744, 5347, -337, 7554, -607, -88, 6199, 2204, 5382, 5153, -6261, -4158, 4998, -936, 1570, -1390, -5116, -6465, -6293, -688, 2141, 1239, -6658, -3348, -1259, 1792, -7462, -4955, -2183, 6397, -865, -7640, 3543, 6990, 8107, -5265, -1299, 6105, 5132, -4110, 3058, 7063, -75, -145, -2074, -6698, 6657, 1002, -4971, -7836, -7879, 5362, 1595, -6353, -6186, -7865, 3623, -5464, -4627, -6753, -7268, 2692, -6200, 4467, 1482, -6294, 7395, -8010, 7995, 4334, -3927, 2860, 3196, 4190, -5477, -7071, 5676, -7021, 2115, -7487, -6665, 2420, 6059, 3122, 4259, 8065, 3442, -310, -5600, 7007, 1129, -4676, 1506, 3113, 7984, -5205, 5011, 7178, -5030, 4806, 3319, -765, -527, -1686, -4776, 2188, -573, -7293, 3352, -6651, -6588, 4879, 3961, 7656, -199, 19, 7528, -4950, 7901, -6264, -6144, 830, -2756, 3554, -4250, -2965, 6534, -7439, -3980, -6689, 5559, 7523, 730, -3169, -2356, 4146, 7204, 5255, 5037, 2363, 6796, 6634, -951, 2556, 6097, 7042, -5617, 5424, -6109, -5909, 7344, -4061, 3105, -3604, 7678, 7040, 1623, 6011, 7793, 5828, 7506, 5151, 5150, 43, -6211, -5406, -4012, -7208, 8041, -7168, 3347, 6645, 7658, -5796, 1008, 5554, -6955, 3575, 2786, -4879, 5859, 1937, -748, 771, 6517, -1263, -390, -60, -3453, -790, -2425, -4140, -3840, -5468, 4087, -1866, -2690, -8118, -882, -2841, -7101, -5727, -4397, -7644, -3339, 4795, 6095, -2110, 178, 688, 1203, -2156, -5576, -7745, 6799, -7259, -824, -1783, 873, 3916, 5611, 6640, 7968, -6429, -7029, 3855, -103, -1526, 3921, 7199, 3817, 5012, -6729, 7612, 5553, -1876, 4214, 3455, 4199, -3801, -4058, -2791, 2227, -1450, -2352, 826, -517, 5017, 7227, -7837, 740, 4637, 6987, 507, 6400, 8143, -3831, -1904, -1584, -8102, -2905, -5960, 5094, -1442, -6541, 2446, 4867, 5857, -2300, 873, -6144, 1834, 6266, 4275, -7808, -4278, -3100, -141, -7454, -4066, 215, 1470, -7629, -999, -6216, 6955, -1049, -1862, -3149, 5559, -1780, 2138, 7791, -4887, -7497, -6951, 5752, 5554, 7099, -4749, -1766, -7238, 5278, -3700, 5221, 5654, 206, -6071, -2680, 936, -1953, 5719, -5795, -1390, -3472, -3819, -2635, 3671, 2503, 2408, 1030, -7478, -3647, 628, -4172, -2960, 1862, -6621, -5598, 760, -3178, 820, 1706, -6101, 5304, -1274, 7737, -2683, 847, -3143, 6437, 7079, -5617, -7551, -2512, -905, -3185, 3045, -5426, 7510, -2748, 3788, -8168, 1797, -3785, -4148, 7030, 6269, -2585, -6769, -1164, 2421, 2243, -7659, 4513, -645, -740, 4049, 4856, -8094, -7287, 3101, 7169, -4711, 3742, -3535, 2576, -7636, 7694, 5334, 8059, -3246, 929, 8083, 6735, 5337, -4266, 5572, 3405, 1333, 6987, -5959, -4439, 1038, -5426, -8127, -7808, 2026, 4115, 5240, 2117, 5020, 140, 1093, -7892, -4318, 5750, 2869, -3770, 5244, 10, -3904, -6203, -7261, -4022, -7661, 6260, -104, 6096, 1472, -6964, 4890, 3705, -3218, -2265, 6472, -3153, -1889, 297, -7239, -4841, -5779, 5966, 3491, 3507, 6266, 7365, 1056, 942, -4597, -1901, -7248, -317, 88, -6317, 3846, 620, 8127, -4451, -1477, 1406, -3222, -4780, -3081, 1744, 1140, -4810, 6783, 7443, 3671, 7737, -5599, 6077, 5510, 6085, 1383, 3575, 5249, -5754, -3683, -7549, 530, -2739, 319, -7575, -872, -4028, 1229, -938, -295, 7944, -7725, 4667, -5036, -2622, -1782, 4296, 752, -3191, 3546, -3769, -3655, 6132, -5885, -6346, 4024, 3690, 5413, 1072, 6120, -6463, 1708, -1551, -1010, -6174, -933, 6302, -2018, -7905, -2829, 5879, -8153, -2369, 2354, -4997, 3193, -7629, 7483, -4247, -2636, 2828, 168, 1893, 767, 2467, 3739, -3410, -2044, 960, 5847, -4125, 2689, -638, 2517, -6521, 1372, -6617, 7973, 7546, -6330, -3056, 5232, -6291, 2767, -615, -3104, -2241, -51, -3822, 1704, 5497, 7199, -6329, -802, -235, 4330, -5264, 4548, -5907, 3888, 2202, -1839, -1623, -6637, -7515, 40, 2927, -5940, -188, 2272, -4086, 4948, -689, -2184, -486, 6881, 2896, 5466, -1371, 7267, -1031, -4067, 6265, 833, 3323, -2163, -3030, 6252, -5808, -752, 1939, 4578, 5601, -7885, 6125, 6270, 347, 859, -7871, -8033, -5062, -3765, 5099, 2434, 2235, -3579, 1122, -3061, -6314, 7935, -3995, 839, -4325, -5931, -6521, 7183, 98, -1366, 5234, 2475, 6066, -1028, -1140, 3474, -720, -3207, 1543, 7811, 5836, 1864, 7962, -7426, 6283, 4869, 3200, 326, -6911, -3879, 5449, -5041, -4145, -6747, 3990, -278, -4486, 5654, -1296, 3804, -3913, -4263, -1922, -6040, 2902, 5131, 5618, -6011, -6277, -1032, -6401, 7751, -7369, -6631, -7876, 7098, 6422, 3508, -769, 7703, 7821, -3521, -5539, -4517, -2076, 6643, 3390, 1622, 4096, -6107, -2774, -8010, -2177, 3496, -5858, -7468, 426, 7944, -5295, 2341, -1289, -3512, 1892, -474, -1951, 2200, -1568, -3730, -2484, 5855, -4220, -2856, -5866, -1567, 812, 242, -3124, -3999, -6328, -7221, -1922, -910, -7046, 4093, -5615, -4720, 4809, 3004, -4968, 7698, -2856, 1935, -4006, 7220, -6731, 2227, 1228, -107, 6690, 6936, -2453, -5731, -4121, -135, 887, 4883, -8085, 5947, -7317, -6229, 6910, -1046, 1053, 8056, -5154, 3630, -4856, 7840, -1567, -1632, 7337, 3770, -7898, -4862, 2797, -6437, 5550, -4168, 1640, 4039, -5425, 7372, 6492, -1353, -964, -814, -4671, -857, -3060, -3803, 1106, -4342, 3335, -6042, -4487, 6373, 5773, -1151, 6012, -3987, 5409, 5157, 7967, 5704, -7906, 2572, 7451, 5836, 6588, 891, 1674, -7037, 62, -26, -198, 7290, 7352, 3315, -1759, -3908, 7696, 7531, -66, 2838, -6711, 3639, 1011, 7254, -5704, -1170, -4934, 7889, -4206, -5159, 5392, -3919, 5605, 4651, -6276, 4000, -2659, 3583, 5155, 5595, -4636, -3244, 4684, -5485, -8129, -5276, -1201, 7759, -5937, 6917, 2397, -4456, 2364, -4785, -5403, 4844, 2237, -2145, 4532, 6224, 888, 1732, -5888, -1708, -1818, -3980, -5908, 3715, 7795, 7431, 1109, -5042, -4005, -2400, -2334, -3950, 517, 4649, -4392, 2764, 3374, 6197, 6492, -2463, -6789, -7104, -5812, 3641, -1065, 6912, 1672, 8016, 443, 3968, -1885, 6817, 8172, 399, 2331, 7767, -362, -4753, -5468, 3817, 1032, 390, 8051, -6652, -3153, -4534, 4304, -7972, -6537, 2595, -2251, -5134, 3683, 121, 6691, -5583, -1168, 162, -5760, 7468, -4063, 540, 6084, -4091, -7262, 223, -4517, 560, 3654, -1793, -3824, -3507, 6790, -3966, -1967, -4564, -315, -5864, -4352, 1332, 4923, 1589, 4382, 405, -6483, 2881, 3015, 533, -5150, 5439, -192, -1028, -2214, -2300, 3073, -1291, 6115, 6748, 7461, 1568, -3238, -4563, 6254, -4649, -337, -3914, -1029, 7532, -1593, 2811, 663, -4863, -3801, -3147, 3727, -2100, 7926, -1451, 6626, -5425, -4205, -1759, 1739, 1766, 4125, -3389, -7726, 2039, -4842, 7919, -4585, 105, -4837, -6532, 3648, 3011, -2254, -5581, 2350, 4345, 5422, -5179, 7667, -6579, -142, 3201, -487, -409, -6451, -2054, 2350, -2472, 4372, -4111, 7486, 304, 692, 7944, -5857, 4043, 7671, -2250, -4045, -5359, -590, 7787, 5844, 5340, -5987, -6, 1493, 7620, 2999, 959, -7152, -5336, -4033, 545, 2439, -2292, 6684, -3404, 3428, 2855, 677, 2714, -5042, -6831, 2457, -2707, 5396, 1935, 3235, -6850, 4761, -5548, -7264, 2412, 7977, -5066, -5795, 1277, -5647, 5396, -5957, -4615, -8133, -1806, 4122, 2498, 4086, 2605, 7287, -687, -2733, -237, -6166, 418, 1116, 4476, 5903, -1689, -1782, 938, -355, -5214, 3574, 574, 5383, 3358, 3700, 7780, -3558, 6245, 4984, -1331, -6571, 5035, 5047, 5743, -659, 940, 156, -1573, -7939, 5615, 6374, -5921, -2168, -710, 6747, -4465, 5793, -3235, 4665, -2754, -257, 46, 6004, -3075, -4788, 1503, -3495, -162, -453, -6712, 6692, 1168, 6515, 3546, -1282, -2345, -3706, 7066, 4274, -3461, 4481, 2448, -1190, -5888, -6455, -2643, -2161, 7522, 2314, -5689, -3433, -6144, 2550, -5622, -1026, 5946, 4073, 3671, -2417, -4573, 5143, -3918, 4779, 3465, 7813, -4695, -7072, -4094, -5830, 5386, 637, 6835, -359, 7639, -7245, 1370, -3197, -1222, 692, 7301, 1282, 5443, -7035, -4369, 8014, 131, -6624, 3886, -4399, -849, 7498, -7449, 3418, 4084, 4200, 3038, 7573, 5320, 7136, -6449, 2506, -420, -7815, -6054, -982, -6868, 3509, 4006, 103, -4000, 3114, -6816, -6750, 4271, -3001, -6937, -3799, -1433, 5134, -14, 5910, 4431, 729, 1135, 314, -3263, -4020, -305, -6144, -5085, 1430, 4554, 2687, 1807, 6693, -6495, 3124, 2001, 5703, -4974, 6193, 624, -3606, 7627, -3305, 1585, -7510, 1088, -8041, 5816, -7118, 6053, 2054, 1795, -1012, -5825, 6716, 3160, 2054, -7620, 6260, -4709, 5118, 746, 5283, 3610, 2443, 206, -2582, -47, 3424, -4590, -7623, 8010, -5155, -2744, 1402, -4473, 6528, 1545, -6858, 7594, -595, 3380, 1197, 6585, 5739, -288, 1545, -399, 276, -388, 3076, -2798, -7835, 158, -7381, 2793, -7829, -1770, -5447, 3787, 1824, -4886, 3596, 4853, 562, -3203, -7821, -1102, 6534, -6487, -1701, -2261, 5085, 7680, -3877, 2632, -800, 5860, -5968, 7668, -2729, 5292, -3331, -2379, -2742, -2519, -7779, -2379, 3895, -5042, -6792, -2474, -1735, 4996, -5821, 7011, -6407, -5450, -2284, -8074, -3744, 4200, -2143, -6860, 3679, 2173, 3956, -5322, -168, 6180, -5854, 5288, 3280, -993, -5284, -7655, 4672, -4871, -1850, 366, -1721, -450, 6077, 4728, -3654, -7937, 3547, -1869, -5195, -6938, -1759, -755, 5446, 4283, 578, 925, -1745, -3659, 3795, 6279, -5679, 6125, 3366, 5785, -3068, 6274, 6322, -6589, -6798, -3729, 1962, -334, 4014, -154, -3799, -7841, 101, 7932, -1526, 3090, -7206, 4907, -5857, 6432, 997, 2905, -836, 7444, 7438, -5241, 5523, -6442, -7317, 696, 7535, -2193, -1230, 5656, -597, 164, -6265, -6828, 8014, 5941, 1202, -3985, 6292, -6890, -4246, -3427, 4384, -3260, -6721, 6719, -5028, 2461, 1431, 2320, 1704, 669, 5263, -966, 2419, 6139, 7915, 1754, -4255, -1516, -783, 3340, 6832, 1144, 4696, 6654, -1116, -2295, -5524, -3025, -1001, -1586, 1732, -4809, 3347, 3196, -6291, 6503, -2536, 3325, 630, 7360, -4207, -2299, -1806, 6396, -4361, -2092, -43, -424, 4584, 7359, -5284, 3223, 310, 7604, 1676, 7379, -2891, 4336, -3847, 4292, -5442, 6070, 7667, 6089, 1073, -6816, 4399, 6729, 4693, -3164, 5888, -7707, 2721, -4111, 6881, 6552, 1989, -1354, -2072, -1628, -2188, 836, -6605, 6306, 239, 3263, 5484, 5540, -593, -6555, 1632, 2157, 7707, 1106, 53, 579, 2474, -3749, -885, -1026, 1279, -3190, -541, -4200, 884, -1852, -5849, -5320, 4978, 271, 1237, -5403, -7094, 2824, -7298, 1338, -2106, 6379, -1323, 5485, 8008, -7884, -551, 7514, 1415, 7686, -100, -4304, -4256, 7199, 2855, 5208, -4192, -5879, -7193, 4884, 453, -4850, 7749, -2762, 3606, 793, 19, 4704, -4576, 914, -2151, 1502, -900, 4711, -1205, -1093, 5019, 6428, -1772, -1767, 5922, 6320, 2114, -6535, 5326, -3224, 6857, -7067, -919, 7856, 6010, 7727, -5194, 5558, -3228, 6604, -1842, 4984, 3107, 1766, -2295, -7244, -4925, 4989, 5659, 2054, -4297, 2477, 290, 2115, -7490, -1989, 242, 2816, -332]
	start = time.time()
	print("R: %d" % (divideAndConquer(vector, 0, len(vector) - 1)))
	end = time.time()
	print("O tempo em %f segundos" % (end - start))

if __name__ == '__main__':
	main()
