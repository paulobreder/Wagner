#Simule um conjunto de dados com 50 amostras (linhas) e 3 características
#(colunas) usando números aleatórios entre 0 e 1. Para cada coluna, calcule:
#a. A média e o desvio padrão.
#b. O valor máximo e o valor mínimo.
#c. Normalize os dados de cada coluna para que fiquem no intervalo [0,
#1].

import numpy as np

dados = np.random.rand(50, 3)
media = np.mean(dados, axis=0)
desvio_padrao = np.std(dados, axis=0)
maximo = np.max(dados, axis=0)
minimo = np.min(dados, axis=0)
normalizado = (dados - media) / desvio_padrao

print("Média:", media)
print("Desvio padrão:", desvio_padrao)
print("Máximo:", maximo)
print("Mínimo:", minimo)
print("Dados normalizados:", normalizado)
