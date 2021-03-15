# Напишите код на Python, реализующий построение графиков:
# 1) окружности,
# 2) эллипса,
# 3) гиперболы.
#
# 1) график окружности:

import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2 * np.pi, 100)
r = np.sqrt(1.0)

x1 = r*np.cos(theta)
x2 = r*np.sin(theta)

fig, ax = plt.subplots(1)

ax.plot(x1, x2)
ax.set_aspect(1)

plt.xlim(-1.25, 1.25)
plt.ylim(-1.25, 1.25)

plt.grid(linestyle='--')

plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('График окружности', fontsize=8)
plt.savefig('plot_circle.png', bbox_inches='tight')

plt.show()

