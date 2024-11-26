#Dado o array x=[0,1,2,3,4] e y=[1,2,0,2,1], crie novos valores para xxx em
#passos de 0.1 usando numpy.interp. Plote os valores interpolados (se
#necessário, use Matplotlib para exibir).

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 2, 0, 2, 1])

xx = np.arange(0, 5, 0.1)
yy = np.interp(xx, x, y)

plt.plot(x, y, 'o', xx, yy)
plt.show()

