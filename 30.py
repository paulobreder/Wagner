#Crie um conjunto de dados simulando uma relação linear: y=2x+3+ruído,
#onde x varia de 0 a 10 (20 pontos). Use a álgebra matricial do NumPy para
#calcular os coeficientes da regressão linear y=ax+b. Compare os resultados
#com os obtidos usando a função numpy.polyfit.

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 20)
y = 2 * x + 3 + np.random.randn(20)

coeficientes = np.polyfit(x, y, 1)
a, b = coeficientes

y_predito = a * x + b

plt.scatter(x, y)
plt.plot(x, y_predito)
plt.show()
