#Crie dois arrays de tamanho 10 contendo números aleatórios entre 1 e 100.
#Some, subtraia, multiplique e divida os dois arrays.

import numpy as np

array1 = np.random.randint(1, 101, 10)
array2 = np.random.randint(1, 101, 10)

print(array1)
print(array2)

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)