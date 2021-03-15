# Напишите код на Python, реализующий построение графиков:
# 1) окружности,
# 2) эллипса,
# 3) гиперболы.
#
# 2) график эллипса:

import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2 * np.pi, 100)

c_x = 1
c_y = 0.5
r_x = 2
r_y = 1.5

plt.plot(c_x + r_x * np.cos(theta), c_y + r_y * np.sin(theta))

plt.grid(linestyle='--')

plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('График эллипса', fontsize=8)
plt.savefig('plot_ellipse.png', bbox_inches='tight')

plt.show()
