#Gere um conjunto de dados simulando as alturas (em cm) de 100 pessoas,
#usando uma distribuição normal com média 170 e desvio padrão 10. Depois
#calcule:
#a. O percentil 25, 50 (mediana) e 75.
#b. A quantidade de pessoas com altura acima de 180 cm.
#c. Plote um histograma dos dados usando Matplotlib (não precisa
#detalhar o código da plotagem).

import numpy as np
import matplotlib.pyplot as plt

alturas = np.random.normal(170, 10, 100)
percentil_25 = np.percentile(alturas, 25)
percentil_50 = np.percentile(alturas, 50)
percentil_75 = np.percentile(alturas, 75)

print("Percentil 25:", percentil_25)
print("Percentil 50:", percentil_50)
print("Percentil 75:", percentil_75)

acima_180 = np.sum(alturas > 180)
print("Quantidade de pessoas com altura acima de 180 cm:", acima_180)

plt.hist(alturas, bins=20)
plt.xlabel("Altura (cm)")
plt.ylabel("Frequência")
plt.title("Distribuição de Alturas")
plt.show()