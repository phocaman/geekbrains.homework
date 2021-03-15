# Напишите код на Python, реализующий построение графиков:
# 1) окружности,
# 2) эллипса,
# 3) гиперболы.
#
# 3) график гиперболы:

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(100, -100)
a = 1
b = 2
y = np.sqrt((x/a) ** 2 - 1 * b ** 2)

plt.plot(x, y)
plt.plot(x, -y)

plt.grid(linestyle='--')

plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('График гиперболы', fontsize=8)
plt.savefig('plot_hyperbola.png', bbox_inches='tight')

plt.show()
