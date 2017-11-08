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
	vector = [-448, -469, -7537, -997, -4960, 6576, 6375, -536, -5669, 7250, 5407, -1794, -4184, -4026, 7110, 6204, 2144, 1576, 2147, 950, -294, 285, 1320, -2588, 4110, 2481, 3738, 202, 4734, 7562, -7655, -3914, -1099, -7000, 3281, 2125, 7768, 1463, -6611, -6102, 513, 6988, 296, 4521, -5230, -794, 2524, 5106, -7411, -3522, -2137, 479, 4947, 7368, 6084, 857, 1656, 1629, -7142, -1810, 991, -6605, 2468, 8084, -5421, -2452, 2008, -5854, 7196, 3589, -3764, -484, 2385, 4717, -4156, 5347, -4270, 6560, 2252, -3489, -5162, -8086, 5175, 7969, 7474, 3066, 633, 930, -3506, 1683, 7312, 5677, 3270, 1579, 5560, 6041, 7319, -624, -8006, 6322, -5228, -3585, -2363, 5341, -7061, 1673, 2495, -3139, 33, -3454, 1556, 3055, -3347, -1462, 2831, -4074, -6597, -4728, 5048, -1910, 5147, 4159, -4434, 217, -2455, -7074, -1943, -3328, 494, -1764, -5207, 3450, 2843, 623, 591, 3966, -5905, -5115, -7366, 2320, -376, 2374, -2818, 4461, -7280, -8187, -7806, -5685, -4723, 5427, 589, -7777, 1393, 4348, 632, 7131, 5466, 6882, -4398, -2241, -3075, -1413, -6992, 7952, 7394, 1791, 3725, -6711, 4869, 4543, 3801, -3708, -1276, -7217, -7440, -372, -7212, -7062, 2128, -3751, 6557, -5476, -3336, -242, 7056, 5481, -1304, 4321, 4162, 2490, -6121, -7106, -7124, -4920, -7355, -7930, 5055, 4554, -6449, 1723, 904, 5536, 6207, 7812, 6511, 6951, -752, 7483, 8082, -6825, -4469, 6446, -4109, 388, -1997, -5245, -2332, 4891, 7260, -6363, -820, -7053, -5285, 241, -3781, -4448, 503, -6927, -8087, 2246, 2989, 1001, -419, 995, 620, -2100, -246, 8052, -2818, -365, -6966, 898, -2120, -2890, -6907, 4076, 49, -1047, 766, -884, 782, 8139, 255, 3689, 179, 4658, 7425, -7511, 5924, 7522, 2919, 712, 330, -5693, -6486, -7251, 391, 1452, -7399, 5758, -7114, -6181, -1537, -1041, -879, -260, -5158, 7362, 6877, 3792, -1714, -542, 3738, 6733, -5054, -4284, 3199, -5822, -3603, 922, -6493, 7500, -6559, 2021, -6393, -4861, 2962, 2190, 4784, 3747, -253, 5862, 5759, 6402, -3380, -3313, -2059, -354, -4151, -3375, -4754, 2327, 4275, 7168, 859, 7413, -5308, -4143, -6610, -727, 4971, -4919, -1427, 6596, 5294, 372, -6457, 56, -5639, 6511, -4390, 2301, 4172, -6832, 502, -7400, -1952, 6636, 438, 2089, -4932, 3868, -3785, 7528, 2844, 5258, 6748, 5720, -7077, -8062, -3200, 6078, -4789, 3565, 4482, -7695, -4264, 6209, 553, -1710, 4527, 4347, -7610, 506, 5708, 1084, 1290, -4445, -481, -6472, 5828, 2772, 5588, -6158, 2107, 231, 7292, 654, -2242, -7986, 784, 2743, 6285, 4180, -1893, 2566, 4677, 2028, 582, -2963, -7875, -3084, -6817, -7301, 5606, 7075, 1967, -1304, -5563, -6706, 416, -7936, 4250, -2197, -5902, -1836, 6227, -6810, 7002, -4216, -6604, -406, 6711, 7873, -4419, -3374, 2246, -7935, 6838, -5373, -2714, 7155, -273, -1347, 8038, -2867, -2464, 1812, 4021, 165, 3290, -3764, 414, -653, 2231, 2704, 5695, 257, 4086, 4505, 4226, 5675, -4102, 2744, 5347, -337, 7554, -607, -88, 6199, 2204, 5382, 5153, -6261, -4158, 4998, -936, 1570, -1390, -5116, -6465, -6293, -688, 2141, 1239, -6658, -3348, -1259, 1792, -7462, -4955, -2183, 6397, -865, -7640, 3543, 6990, 8107, -5265, -1299, 6105, 5132, -4110, 3058, 7063, -75, -145, -2074, -6698, 6657, 1002, -4971, -7836, -7879, 5362, 1595, -6353, -6186, -7865, 3623, -5464, -4627, -6753, -7268, 2692, -6200, 4467, 1482, -6294, 7395, -8010, 7995, 4334, -3927, 2860, 3196, 4190, -5477, -7071, 5676, -7021, 2115, -7487, -6665, 2420, 6059, 3122, 4259, 8065, 3442, -310, -5600, 7007, 1129, -4676, 1506, 3113, 7984, -5205, 5011, 7178, -5030, 4806, 3319, -765, -527, -1686, -4776, 2188, -573, -7293, 3352, -6651, -6588, 4879, 3961, 7656, -199, 19, 7528, -4950, 7901, -6264, -6144, 830, -2756, 3554, -4250, -2965, 6534, -7439, -3980, -6689, 5559, 7523, 730, -3169, -2356, 4146, 7204, 5255, 5037, 2363, 6796, 6634, -951, 2556, 6097, 7042, -5617, 5424, -6109, -5909, 7344, -4061, 3105, -3604, 7678, 7040, 1623, 6011, 7793, 5828, 7506, 5151, 5150, 43, -6211, -5406, -4012, -7208, 8041, -7168, 3347, 6645, 7658, -5796, 1008, 5554, -6955, 3575, 2786, -4879, 5859, 1937, -748, 771, 6517, -1263, -390, -60, -3453, -790, -2425, -4140, -3840, -5468, 4087, -1866, -2690, -8118, -882, -2841, -7101, -5727, -4397, -7644, -3339, 4795, 6095, -2110, 178, 688, 1203, -2156, -5576, -7745, 6799, -7259, -824, -1783, 873, 3916, 5611, 6640, 7968, -6429, -7029, 3855, -103, -1526, 3921, 7199, 3817, 5012, -6729, 7612, 5553, -1876, 4214, 3455, 4199, -3801, -4058, -2791, 2227, -1450, -2352, 826, -517, 5017, 7227, -7837, 740, 4637, 6987, 507, 6400, 8143, -3831, -1904, -1584, -8102, -2905, -5960, 5094, -1442, -6541, 2446, 4867, 5857, -2300, 873, -6144, 1834, 6266, 4275, -7808, -4278, -3100, -141, -7454, -4066, 215, 1470, -7629, -999, -6216, 6955, -1049, -1862, -3149, 5559, -1780, 2138, 7791, -4887, -7497, -6951, 5752, 5554, 7099, -4749, -1766, -7238, 5278, -3700, 5221, 5654, 206, -6071, -2680, 936, -1953, 5719, -5795, -1390, -3472, -3819, -2635, 3671, 2503, 2408, 1030, -7478, -3647, 628, -4172, -2960, 1862, -6621, -5598, 760, -3178, 820, 1706, -6101, 5304, -1274, 7737, -2683, 847, -3143, 6437, 7079, -5617, -7551, -2512, -905, -3185, 3045, -5426, 7510, -2748, 3788, -8168, 1797, -3785, -4148, 7030, 6269, -2585, -6769, -1164, 2421, 2243, -7659, 4513, -645, -740, 4049, 4856, -8094, -7287, 3101, 7169, -4711, 3742, -3535, 2576, -7636, 7694, 5334, 8059, -3246, 929, 8083, 6735, 5337, -4266, 5572, 3405, 1333, 6987, -5959, -4439, 1038, -5426, -8127, -7808, 2026, 4115, 5240, 2117, 5020, 140, 1093, -7892, -4318, 5750, 2869, -3770, 5244, 10, -3904, -6203, -7261, -4022, -7661, 6260, -104, 6096, 1472, -6964, 4890, 3705, -3218, -2265, 6472, -3153, -1889, 297, -7239, -4841, -5779, 5966, 3491, 3507, 6266, 7365, 1056, 942, -4597, -1901, -7248, -317, 88, -6317, 3846, 620, 8127, -4451, -1477, 1406, -3222, -4780, -3081, 1744, 1140, -4810, 6783, 7443, 3671, 7737, -5599, 6077, 5510, 6085, 1383, 3575, 5249, -5754, -3683, -7549, 530, -2739, 319, -7575, -872, -4028, 1229, -938, -295, 7944, -7725, 4667, -5036, -2622, -1782, 4296, 752, -3191, 3546, -3769, -3655, 6132, -5885, -6346, 4024, 3690, 5413, 1072, 6120, -6463, 1708, -1551, -1010, -6174, -933, 6302, -2018, -7905, -2829, 5879, -8153, -2369, 2354, -4997, 3193, -7629, 7483, -4247, -2636, 2828, 168, 1893, 767, 2467, 3739, -3410, -2044, 960, 5847, -4125, 2689, -638, 2517, -6521, 1372, -6617, 7973, 7546, -6330, -3056, 5232, -6291, 2767, -615, -3104, -2241, -51, -3822, 1704, 5497, 7199, -6329, -802, -235, 4330, -5264, 4548, -5907, 3888, 2202, -1839, -1623, -6637, -7515, 40, 2927, -5940, -188, 2272, -4086, 4948, -689, -2184, -486, 6881, 2896, 5466, -1371, 7267, -1031, -4067, 6265, 833, 3323, -2163, -3030, 6252, -5808, -752, 1939, 4578, 5601, -7885, 6125, 6270, 347, 859, -7871, -8033, -5062, -3765, 5099, 2434, 2235, -3579, 1122, -3061, -6314, 7935, -3995, 839, -4325, -5931, -6521, 7183, 98, -1366, 5234, 2475, 6066, -1028, -1140, 3474, -720, -3207, 1543, 7811, 5836, 1864, 7962, -7426, 6283, 4869, 3200, 326, -6911, -3879, 5449, -5041, -4145, -6747, 3990, -278, -4486, 5654, -1296, 3804, -3913, -4263, -1922, -6040, 2902, 5131, 5618, -6011, -6277, -1032, -6401, 7751, -7369, -6631, -7876, 7098, 6422, 3508, -769, 7703, 7821, -3521, -5539, -4517, -2076, 6643, 3390, 1622, 4096, -6107, -2774, -8010, -2177, 3496, -5858, -7468, 426, 7944, -5295, 2341, -1289, -3512, 1892, -474, -1951, 2200, -1568, -3730, -2484, 5855, -4220, -2856, -5866, -1567, 812, 242, -3124, -3999, -6328, -7221, -1922, -910, -7046, 4093, -5615, -4720, 4809, 3004, -4968, 7698, -2856, 1935, -4006, 7220, -6731, 2227, 1228, -107, 6690, 6936, -2453, -5731, -4121, -135, 887, 4883, -8085, 5947, -7317, -6229, 6910, -1046, 1053, 8056, -5154, 3630, -4856, 7840, -1567, -1632, 7337, 3770, -7898, -4862, 2797, -6437, 5550, -4168, 1640, 4039, -5425, 7372, 6492, -1353, -964, -814, -4671, -857, -3060, -3803, 1106, -4342, 3335, -6042, -4487, 6373, 5773, -1151, 6012, -3987, 5409, 5157, 7967, 5704, -7906, 2572, 7451, 5836, 6588, 891, 1674, -7037, 62, -26, -198, 7290, 7352, 3315, -1759, -3908, 7696, 7531, -66, 2838, -6711, 3639, 1011, 7254, -5704, -1170, -4934, 7889, -4206, -5159, 5392, -3919, 5605, 4651, -6276, 4000, -2659, 3583, 5155, 5595, -4636, -3244, 4684, -5485, -8129, -5276, -1201, 7759, -5937, 6917, 2397, -4456, 2364, -4785, -5403, 4844, 2237, -2145, 4532, 6224, 888, 1732, -5888, -1708, -1818, -3980, -5908, 3715, 7795, 7431, 1109, -5042, -4005, -2400, -2334, -3950, 517, 4649, -4392, 2764, 3374, 6197, 6492, -2463, -6789, -7104, -5812, 3641, -1065, 6912, 1672, 8016, 443, 3968, -1885, 6817, 8172, 399, 2331, 7767, -362, -4753, -5468, 3817, 1032, 390, 8051, -6652, -3153, -4534, 4304, -7972, -6537, 2595, -2251, -5134, 3683, 121, 6691, -5583, -1168, 162, -5760, 7468, -4063, 540, 6084, -4091, -7262, 223, -4517, 560, 3654, -1793, -3824, -3507, 6790, -3966, -1967, -4564, -315, -5864, -4352, 1332, 4923, 1589, 4382, 405, -6483, 2881, 3015, 533, -5150, 5439, -192, -1028, -2214, -2300, 3073, -1291, 6115, 6748, 7461, 1568, -3238, -4563, 6254, -4649, -337, -3914, -1029, 7532, -1593, 2811, 663, -4863, -3801, -3147, 3727, -2100, 7926, -1451, 6626, -5425, -4205, -1759, 1739, 1766, 4125, -3389, -7726, 2039, -4842, 7919, -4585, 105, -4837, -6532, 3648, 3011, -2254, -5581, 2350, 4345, 5422, -5179, 7667, -6579, -142, 3201, -487, -409, -6451, -2054, 2350, -2472, 4372, -4111, 7486, 304, 692, 7944, -5857, 4043, 7671, -2250, -4045, -5359, -590, 7787, 5844, 5340, -5987, -6, 1493, 7620, 2999, 959, -7152, -5336, -4033, 545, 2439, -2292, 6684, -3404, 3428, 2855, 677, 2714, -5042, -6831, 2457, -2707, 5396, 1935, 3235, -6850, 4761, -5548, -7264, 2412, 7977, -5066, -5795, 1277, -5647, 5396, -5957, -4615, -8133, -1806, 4122, 2498, 4086, 2605, 7287, -687, -2733, -237, -6166, 418, 1116, 4476, 5903, -1689, -1782, 938, -355, -5214, 3574, 574, 5383, 3358, 3700, 7780, -3558, 6245, 4984, -1331, -6571, 5035, 5047, 5743, -659, 940, 156, -1573, -7939, 5615, 6374, -5921, -2168, -710, 6747, -4465, 5793, -3235, 4665, -2754, -257, 46, 6004, -3075, -4788, 1503, -3495, -162, -453, -6712, 6692, 1168, 6515, 3546, -1282, -2345, -3706, 7066, 4274, -3461, 4481, 2448, -1190, -5888, -6455, -2643, -2161, 7522, 2314, -5689, -3433, -6144, 2550, -5622, -1026, 5946, 4073, 3671, -2417, -4573, 5143, -3918, 4779, 3465, 7813, -4695, -7072, -4094, -5830, 5386, 637, 6835, -359, 7639, -7245, 1370, -3197, -1222, 692, 7301, 1282, 5443, -7035, -4369, 8014, 131, -6624, 3886, -4399, -849, 7498, -7449, 3418, 4084, 4200, 3038, 7573, 5320, 7136, -6449, 2506, -420, -7815, -6054, -982, -6868, 3509, 4006, 103, -4000, 3114, -6816, -6750, 4271, -3001, -6937, -3799, -1433, 5134, -14, 5910, 4431, 729, 1135, 314, -3263, -4020, -305, -6144, -5085, 1430, 4554, 2687, 1807, 6693, -6495, 3124, 2001, 5703, -4974, 6193, 624, -3606, 7627, -3305, 1585, -7510, 1088, -8041, 5816, -7118, 6053, 2054, 1795, -1012, -5825, 6716, 3160, 2054, -7620, 6260, -4709, 5118, 746, 5283, 3610, 2443, 206, -2582, -47, 3424, -4590, -7623, 8010, -5155, -2744, 1402, -4473, 6528, 1545, -6858, 7594, -595, 3380, 1197, 6585, 5739, -288, 1545, -399, 276, -388, 3076, -2798, -7835, 158, -7381, 2793, -7829, -1770, -5447, 3787, 1824, -4886, 3596, 4853, 562, -3203, -7821, -1102, 6534, -6487, -1701, -2261, 5085, 7680, -3877, 2632, -800, 5860, -5968, 7668, -2729, 5292, -3331, -2379, -2742, -2519, -7779, -2379, 3895, -5042, -6792, -2474, -1735, 4996, -5821, 7011, -6407, -5450, -2284, -8074, -3744, 4200, -2143, -6860, 3679, 2173, 3956, -5322, -168, 6180, -5854, 5288, 3280, -993, -5284, -7655, 4672, -4871, -1850, 366, -1721, -450, 6077, 4728, -3654, -7937, 3547, -1869, -5195, -6938, -1759, -755, 5446, 4283, 578, 925, -1745, -3659, 3795, 6279, -5679, 6125, 3366, 5785, -3068, 6274, 6322, -6589, -6798, -3729, 1962, -334, 4014, -154, -3799, -7841, 101, 7932, -1526, 3090, -7206, 4907, -5857, 6432, 997, 2905, -836, 7444, 7438, -5241, 5523, -6442, -7317, 696, 7535, -2193, -1230, 5656, -597, 164, -6265, -6828, 8014, 5941, 1202, -3985, 6292, -6890, -4246, -3427, 4384, -3260, -6721, 6719, -5028, 2461, 1431, 2320, 1704, 669, 5263, -966, 2419, 6139, 7915, 1754, -4255, -1516, -783, 3340, 6832, 1144, 4696, 6654, -1116, -2295, -5524, -3025, -1001, -1586, 1732, -4809, 3347, 3196, -6291, 6503, -2536, 3325, 630, 7360, -4207, -2299, -1806, 6396, -4361, -2092, -43, -424, 4584, 7359, -5284, 3223, 310, 7604, 1676, 7379, -2891, 4336, -3847, 4292, -5442, 6070, 7667, 6089, 1073, -6816, 4399, 6729, 4693, -3164, 5888, -7707, 2721, -4111, 6881, 6552, 1989, -1354, -2072, -1628, -2188, 836, -6605, 6306, 239, 3263, 5484, 5540, -593, -6555, 1632, 2157, 7707, 1106, 53, 579, 2474, -3749, -885, -1026, 1279, -3190, -541, -4200, 884, -1852, -5849, -5320, 4978, 271, 1237, -5403, -7094, 2824, -7298, 1338, -2106, 6379, -1323, 5485, 8008, -7884, -551, 7514, 1415, 7686, -100, -4304, -4256, 7199, 2855, 5208, -4192, -5879, -7193, 4884, 453, -4850, 7749, -2762, 3606, 793, 19, 4704, -4576, 914, -2151, 1502, -900, 4711, -1205, -1093, 5019, 6428, -1772, -1767, 5922, 6320, 2114, -6535, 5326, -3224, 6857, -7067, -919, 7856, 6010, 7727, -5194, 5558, -3228, 6604, -1842, 4984, 3107, 1766, -2295, -7244, -4925, 4989, 5659, 2054, -4297, 2477, 290, 2115, -7490, -1989, 242, 2816, -332, -2633, 7776, -1675, -1508, -1336, -2020, -3699, -1802, 978, -6334, 3155, -619, 8, -54, -5704, -6419, 5835, -4756, -3159, 2623, -7298, 7087, 6510, 3363, -824, 432, 4065, 5379, -7527, -1312, -3145, -1968, -1737, 3372, 4708, 5120, -6841, -7183, -4883, 2322, -5333, 6464, -6490, 2868, -1791, -4010, 4633, -4157, -582, -6719, 6650, 304, -7832, 4967, -4525, -464, -2794, 7732, -3277, -2129, -1780, 1762, 4087, 4675, -3067, 603, 1594, -1724, 1604, 4896, -7603, 4463, 3159, -5908, -870, -6824, -1726, -4429, -2797, 5877, -2964, -4339, -2012, -2612, -7565, 1655, 5109, -2174, 1195, -6361, 3881, 7607, 3585, -224, 4081, -7683, -7822, -2517, -1215, 1966, -5814, -625, -1764, 5537, 1651, 5559, 6897, 8117, -7071, -4092, 5801, -1843, -247, -4403, 3730, 380, 5444, 646, 6390, -1562, 2469, 2079, -2148, -2139, -6346, -6259, -1630, -5984, -592, 5339, 4174, 1786, -3487, -5791, -878, 6356, 7960, -2173, 6273, -7312, 1919, 3873, -970, -6529, 7662, -5433, 2035, 4906, 3405, 233, -4857, -2319, -5889, 1188, 3726, -4043, 3113, -6105, -1835, -5680, 7418, -5862, 4298, -4261, -3461, -4781, -6106, -3701, 1230, -8026, -2821, -5044, 4032, 4401, -3381, 3501, 7152, 6847, 206, 2364, -1121, 3542, -8156, 1182, -3471, 3762, 5323, 7826, 5849, -4713, -6047, 5067, -2383, 6435, -7387, 2348, -6539, -5309, 6831, 2884, -5150, -4182, 6024, 7074, -7982, -5557, 2374, 7363, -6911, -5620, 1534, 160, 6114, 1563, -6859, -5558, -2868, 6656, -5925, -5219, -6258, -3780, 8040, -449, -5538, -7548, -6302, -3893, -4673, -7663, 7183, -1631, -3661, 5007, -2758, -3451, 7642, 7809, -4281, -7470, -6004, 5438, 874, -8091, -1192, 2207, -5457, 4124, 662, -3198, 7089, 2596, 1206, 6928, -6054, 3852, 7572, -4172, 8151, -5301, -3651, 7134, 1260, 880, 3948, 6687, 5614, 3389, 6303, -6860, 4111, -7902, 6762, -3208, -7801, -2631, 7183, -5074, -6699, -356, -88, -7811, -5961, -7075, 7310, -3823, 4969, 6681, 189, 4927, -6813, 4731, 3868, 2632, -2590, -385, 1126, -5169, -5189, -772, -3844, 7106, -482, -5283, -4303, -99, 279, -5313, 3011, 1764, 2523, -5270, 2145, 4754, -4153, 1254, -7270, -7377, -257, 1104, 5734, 1122, -2366, 1402, -4447, 3236, -7184, 4871, 6252, -4188, -4094, -5793, -5275, 3608, -2884, -1393, -4692, 5587, 1478, 6511, -842, -4199, -6952, -6897, -7646, -2921, 2549, -6723, -2114, -5901, 2565, -4580, 3406, -7994, 5014, 7143, 3426, 6022, 3822, 1477, -6359, 7912, 3876, -3449, 3320, -7200, 3350, 6820, 6579, -3365, 5131, -2463, 628, 6363, -1176, 1175, -4750, -6820, 2636, 1320, -4536, -3000, 4932, 7054, -2802, 1753, 6004, -7577, -425, 1625, 2093, 1400, 1337, -2224, 6135, -3544, -1232, 1292, -4917, -2853, 6112, -7987, 2868, -1461, 6569, -6501, 7898, -6382, -5137, 2341, 3130, -1489, 7533, -138, -2636, -3470, -6586, -4824, -2854, 1181, 4985, 7423, -5619, -1879, -2994, -7677, 2769, 3959, 1800, 6037, -7087, -281, 6242, 3965, 6450, 4618, 5656, 6148, 6420, -7682, 296, 1350, -986, -371, -6981, 4570, 4343, -5375, 7930, -6712, 3991, 4723, -7482, 6564, -5349, -2291, 7071, 5613, -6525, 678, 3457, -5428, -7796, 1498, 6729, 6839, -2084, 4184, 4794, -3857, 4686, -3111, 5685, -4493, 4702, 6888, -8115, 845, -6679, 8007, 2325, 5496, 4529, 3028, 3867, 7373, -7456, 2745, 4785, -5797, -4777, 41, -3033, -4381, -6654, -4505, -5743, -546, 7871, 7235, 3782, 4356, -4068, 1266, 8056, -7567, -38, 8133, 1470, 1467, 7939, -4405, -1230, 4276, 6807, -5564, 3448, 7543, 5365, 40, -6455, -7605, -8120, -1304, -3801, -6582, 2383, -1352, 1057, 2053, -2309, -3362, -1784, 1807, 6096, -1921, 2432, -2135, -1989, -4298, 7516, -2242, -511, -1907, -6167, -1897, 721, 5473, -2555, -2114, -2680, -826, -1527, -2616, 6062, 2864, -1014, 252, -6688, -8150, -5896, -813, -3328, 512, -7199, -5424, 6776, 3417, 625, -3406, 7311, -51, 2536, -1401, 6226, 4561, 4886, -1253, 1841, -5862, 4825, 7345, 1496, -4895, -3464, -635, 6154, 3707, 7801, 7658, 3749, -6288, -1348, -7771, 2409, -363, -5011, 992, -5139, 3798, 5770, -6028, -4446, 106, 763, -6420, -3526, -2543, 519, 6500, -221, -2849, 5652, -6917, 440, -6012, 632, -1599, 5887, 241, -2142, 1435, 2137, 4694, 1848, -3647, -3862, 5021, 5529, -816, 627, 3099, 1348, 4365, -4988, -6090, 6137, -322, -441, -1537, -2015, 7523, 3806, -4563, -7587, -3946, -2391, 1237, 2639, -4705, -6723, -7703, 4914, 3607, 5183, -1430, 8144, -6879, -4602, 5473, 489, 4209, 379, -6364, 382, 3583, -4262, -1674, -4940, 3490, 4982, 1230, 2820, 595, 4851, 3417, 4833, -5741, -3547, -728, -2254, -2077, -239, -5533, -6663, -3257, 1221, -6720, -1952, 4812, 6945, 6721, 820, -877, -7836, -6991, -5495, -3905, -472, -2242, 7769, -3683, 7172, 2396, 5096, 3830, -2388, 1729, 6281, 2257, -7200, -4174, -8013, 745, -1515, -6492, 5680, 7899, -5027, -4472, 4510, -6275, -5944, -2863, 1033, -5587, -1669, 3730, -1308, 6051, -6713, -1732, -5833, -7734, -7537, 7447, 4280, -1733, 983, 2368, -7669, 1967, 6386, -7497, -5481, -3329, -5805, -8001, -3631, -2640, -4281, -7314, -730, -2041, -1993, -7890, 564, 4530, 4032, 7440, 2380, 5512, -2485, 4739, 5970, -1830, 3994, 2050, 4629, -3224, -3775, 5145, 6936, -5589, 5832, -6738, -734, -8166, -6547, 3827, -2613, -2644, 4697, 4849, 3508, -5489, 5151, -4129, 7226, 982, -4881, 1413, -1699, 826, -2040, -3929, 7181, -6247, 6313, 3617, -1279, -5663, 561, -2544, -3068, -1800, -1089, 4390, -1773, 548, 24, 3806, 6097, -3472, 462, 1412, -776, -2588, 5467, -1751, 6586, -7607, 7854, -3313, 1404, -2387, 950, 392, -450, -938, -4192, 6464, 1591, 4562, -4281, 6716, -5439, 2822, 2905, 972, -4822, -5271, -3415, -6926, -551, 5231, 2670, 6857, -5558, -56, -3087, -7164, 522, -3433, -2285, -6267, 2364, 6849, 2309, -6278, -2290, 6309, -8015, 7493, 2670, -4104, 6008, 5416, 6903, 713, -1805, -6112, 3634, 2965, -4854, -5118, -5, 6008, -6453, 2630, -2241, -1356, 3650, 6465, 3395, -6836, -7995, -2433, -8180, 2506, -519, -2278, 615, -342, -2986, -4916, 3746, -5178, -7693, 2456, 3727, -1305, 4528, -832, -6541, 7858, 2242, 1646, 5673, 3973, -3917, -4768, -5583, 7917, -6496, 6004, -7112, -6306, -4622, -7108, 4384, 3043, -1194, -3194, -5492, 4005, 83, 6439, 7011, 574, 694, 2545, 7453, -2978, -6488, -7281, -3313, 3938, 2558, -5840, -281, 6825, -2416, 2320, 6550, -728, 131, 7630, 1158, 3694, -7670, -2650, -1456, -680, 2340, 1237, -4876, -5778, -517, -6058, 2989, -8024, 4671, 2249, -2818, 6375, 3161, 2062, 2121, -2482, 4406, -6361, -3850, -6203, 4151, -5501, 1261, -3911, -6063, -5781, 7967, -5549, -239, -1681, 1955, -6092, 7748, 5272, -3677, -970, 7398, 7496, -810, 3877, 1544, 4565, 2059, -3488, -1574, -4021, 2214, -5361, -2190, 6549, -3380, -6240, -7145, 6065, -1966, -5016, -7909, -2192, -2381, 44, 4319, 7767, 2137, 3866, 4838, 6644, -5305, 4043, 5947, 2078, -273, -702, -1558, -6414, 3995, 5060, -2251, -1992, 7883, 3744, -3636, -3690, 5696, -2588, -5818, -4471, 580, -5534, 1530, 6392, 2694, -2352, 5966, -3370, -6686, 2603, -4927, -3799, -1547, -7173, 6463, 6365, 310, -3288, 8135, -3896, -6429, -2309, 2296, -6747, -6766, 6853, -2245, 7115, -3928, 122, -5549, 4844, 2772, 4165, 3035, -2735, -6379, 800, 2088, -4873, -4790, 5353, -488, 1856, 6365, -2217, 20, -1526, 2679, -38, 2762, 4435, 5837, -3135, 5880, 7264, -4475, -4565, 6178, -219, 3749, -7564, -3575, -1680, 4794, 7652, 3777, 6599, 260, -2328, -6467, 3662, -5175, 1229, -2683, -7003, 7204, 5529, -345, 1683, -2710, -5776, -2075, -5065, -727, -4396, -6002, 2983, -777, -8017, -5429, -5221, -7397, -820, 1283, 5581, -1368, -3132, 3987, 7076, 2724, 5704, 2537, 5741, -1259, 8047, 6922, -2256, 5375, -1624, 7611, -5527, 784, -2665, -2408, -8135, 1132, -218, 3040, -7846, -51, 5795, -4874, 736, -3225, 4593, -1875, 3599, -6732, -6089, 2482, 4185, 7800, -3174, 1725, -1660, -3328, 447, 4268, -6145, 7015, 3687, -3488, -393, -7179, 2296, -336, 2145, -6115, -5497, 2492, 2018, -7903, 5802, -5439, -2936, 2194, 870, -7530, 3655, 2966, 3136, -361, 2573, 8147, -6829, -7288, -3374, 1802, 5164, -1335, 625, 650, 3369, -7969, 1664, -2528, -121, -4392, -459, 2574, 6284, -6634, 2863, 3885, -3880, 8112, -2113, 5174, -7611, -6651, -53, 3710, 1172, -5681, 3664, 2527, -4777, -7903, -3863, -7813, -1053, 4954, 1029, -5877, 5177, -5500, -220, -3137, -1707, 7513, 7621, -3616, -7313, 2283, -7923, -3009, 2202, -1844, -6028, 2776, -311, 2104, -1707, -7332, 4615, -6236, 3387, 8023, -5955, 7716, -7983, 1184, 4469, 1230, 3492, 1445, 3923, -4921, 6492, -5977, -5609, 5912, -1409, -4738, 3, -1140, 445, -5988, 5200, 2602, 4980, -3304, -3487, -4920, -2452, -7073, -2972, -7265, -7243, -734, -7750, -7034, -7751, 4904, 2389, 3925, -1844, -1889, 7188, -3552, 318, -6613, -5833, 7101, -3159, 2362, -2239, 5471, 4567, -5232, -128, 1346, -351, 4569, 4611, 5381, 5688, -6554, 6308, 6638, 896, 6743, 7788, 1330, 3454, 1976, -2938, -6591, -8114, -3942, -1951, 388, -2371, 409, -703, 2654, -5422, 5242, -76, 7329, -8183, 7980, 475, -350, 4356, -3107, -3161, 1844, -1469, -5054, 281, 7620, -6504, -132, 749, 5134, -6356, 6003, 6736, -6278, -6140, -3408, 2303, -327, 5185, -6601, -5873, 7948, 6825, 2243, 7084, 6826, 2023, -642, -1716, -1814, 4443, 3307, -8171, -5218, 6437, 302, -5799, 8126, -8022, 3142, 5059, -6186, 944, 3602, -4280, 2989, -8006, 6207, -5531, 5371, 7790, -3212, 5126, 6422, 7216, 4010, 5056, 1046, -4825, -4853, 7416, 7811, 6638, 7438, -5608, 4882, -453, -3223, 4807, -291, 8111, 1674, 1707, 854, -2925, 5620, -4350, -2739, 3626, -1696, -5560, 3224, 3284, 7750, 1453, 2299, 3567, -1684, -4848, 6927, 1647, -5624, 6545, 84, -6387, -7264, -3226, 1344, -2295, -6612, -7139, -2385, 3254, 2760, 6661, -7863, 179, -5889, -2418, -4387, 607, 214, 7029, -4310, -236, 281, 6182, -4862, 6782, -6867, -6136, 228, -4299, -7792, -7880, -2502, -6864, -2914, 7035, -967, -1334, 8080, 4832, -6280, 2647, 3301, -5959, -5374, 5604, -185, -1577, -1990, -8171, -2749, 1892, -215, 5724, -119, 3107, 4305, 1207, 5156, -3659, 5092, 5556, -3347, -5610, 6885, 1923, -6768, -2283, -7604, -6881, -5643, -5700, 3950, 5842, -3475, 6768, 3253, 4525, -3010, -6938, 4546, 2433, 3146, -3870, -35, -5173, 7421, -3923, 4218, 4384, 602, 1109, 1740, 5447, 3691, 432, -823, 5115, 6341, -242, 6418, -7503, 2242, 2176, 6531, 6960, 743, 1583, 3292, 5926, 2837, -363, 158, -2209, 3951, -8070, 802, 3171, -3808, -3173, -645, 4986, 6128, -7098, 2233, 1619, 1526, -6791, -1467, -334, 1159, -3241, 356, -4791, 7127, -1306, -6032, -331, -7915, 5444, -2606, 3106, -3120, 5745, -7296, -7362, 5859, 1690, 3993, -6142, 6709, -4845, 7029, 4637, -3759, 1061, -1945, 5951, 2462, 4780, -2575, -4571, -6654, 5965, -1178, -7728, -3542, 974, 134, -3273, -1775, 5712, 8026, 3297, 3264, -7463, 4119, 923, 2412, -81, 2965, 920, 3259, 1801, -2636, 7692, -5339, 3603, 5451, 5316, 191, -5325, -7456, 1729, -7561, -450, 2186, -2911, -7669, -5881, 2009, -1260, 8023, 1842, -6164, 3087, 2563, 6147, -4183, -3218, -2135, 6974, 5895, -7069, 575, -4942, -7569, 3428, 6854, 6066, 551, -1148, -7460, 1279, -7620, -6829, -7364, 2758, -1548, -6849, 5069, -7732, 83, 4892, 2294, 2111, -214, -3335, 57, 3795, 1631, 6115, 2568, -667, 7238, -5050, 2576, 7853, 6571, 1229, 5718, -1079, -8120, 6450, -7992, -7548, 7813, -7172, 3395, -1935, -5828, 263, -1483, 2439, -3038, -7381, -3642, 4940, -2532, 4599, 534, 7291, 2521, -5090, -1568, 1559, -1956, -7193, 1211, -3586, 2228, -1263, 3528, 2300, -3014, 3720, 2936, -3401, 4740, -1862, 2856, 7096, 6586, -6828, 1343, -4645, -6017, 5885, -7905, -357, 2291, 813, -1258, -3380, 3915, 5358, 6363, -6241, 6357, -619, -1635, 384, 6302, -6308, -5509, -4904, 5604, 5611, -121, 2144, -4443, -5466, 1039, -6058, -4102, -5811, -2511, -1934, -8119, -2232, 5901, 2365, 6774, -3558, 7169, 2488, -6401, 5339, 4439, 8148, -3473, -5396, 331, -5363, -3512, 3014, -2083, -6108, 433, 5988, 4220, 4174, -7671, -2934, 6308, -3589, -552, -4404, 2669, -487, 1549, 370, -6323, 130, 5004, -7347, -5583, 6796, 6184, 7049, 6743, -5489, -6548, -1118, -2660, -1868, -6305, 3441, 216, 2312, 1228, -3757, -1715, 1749, 1494, -3608, 6344, -7251, 173, 821, 446, -6471, -7002, 2316, 1851, 6194, 3161, 4460, 4789, 1145, 3308, 3332, 3848, 4952, -5987, -7013, -5108, -4100, 4620, 3292, 6405, -2345, 7720, -3511, 7588, 1021, 1074, 5739, 1954, -6946, -1641, -5793, -5225, -451, 4715, 4810, -2457, -324, 1077, -5869, -7372, -3815, 5655, 4668, -7056, 7860, 5847, -3980, -4440, 2266, 7497, -6228, 8113, 7016, -1555, 7500, -156, 7711, 5038, -6403, -7428, -4795, -4012, -4469, 2946, -7489, -7852, -7712, 371, 1410, -5388, 1191, 5787, -7934, -2334, 6915, 8119, -4688, -5265, -4514, 5770, -5961, -2558, 5682, -7138, 4079, 4981, 890, 3590, 1826, 2679, 4346, 5215, 6859, 8070, -31, 7554, -7983, 441, -268, 1619, 3245, -7278, -795, 3496, -1428, -2072, 3422, 2076, 855, 7092, -355, 3078, -3667, -2866, 4124, -7789, -6086, -3179, 3993, 3933, 7684, 147, 955, 6342, 16, -7277, 5696, 225, 1349, -2765, -6348, -3607, -1850, 1049, 8081, 4914, 7169, 3302, -1210, -177, 2201, 6627, -5292, 6726, -4439, 7024, 7130, -2341, -4356, 2922, -6601, -4873, -5124, 2539, -6723, 3084, 3446, 7165, -4883, -3406, -3801, -3047, 1180, 2533, 6194, 1068, -753, 5163, -3822, 6229, -3215, 6563, 4655, -322, 5089, -7985, -1499, 4018, -2133, 2338, -1253, -550, 5657, 1808, -6212, 7118, -3301, 5419, 6090, 0, -6180, -5903, 5145, 3192, 4822, 3139, -3940, -4132, 101, 422, -6096, 5078, -1216, 6744, -3437, -4320, 6951]
	start = time.time()
	print("R: %d" % (enumeration(vector, len(vector))))
	end = time.time()
	print("O tempo em %f segundos" % (end - start))

if __name__ == '__main__':
	main()
