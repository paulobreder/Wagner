#Crie uma matriz 2×2 para representar uma transformação linear e um vetor
#v=[1,2]. Aplique a transformação ao vetor v multiplicando-o pela matriz.

import numpy as np

matriz = np.array([[1, 2], [3, 4]])
vetor = np.array([1, 2])

print(matriz)
print(vetor)

print(matriz.dot(vetor))


