# Нарисуйте график функции:
#
# y(x) = k∙cos(x – a) + b
#
# для некоторых (2-3 различных) значений параметров k, a, b

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 3*np.pi, 201)

k, a, b = np.linspace(2, 6, num=3)
k1, a1, b1 = np.linspace(4, 8, num=3)
k2, a2, b2 = np.linspace(6, 10, num=3)

print(f'k = {k}, a = {a}, b = {b}')
print(f'k1 = {k1}, a1 = {a1}, b1 = {b1}')
print(f'k2 = {k2}, a2 = {a2}, b2 = {b2}')

plt.figure(figsize=(10, 5))
plt.plot(x, k * np.cos(x - a) + b, color='blue', label='k, a, b')
plt.plot(x, k1 * np.cos(x - a1) + b1, color='orange', label='k1, a1, b1')
plt.plot(x, k2 * np.cos(x - a2) + b2, color='green', label='k2, a2, b2')

plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend(frameon=False)
plt.title('График функции y(x) = k∙cos(x – a) + b', fontsize=8)
plt.savefig('plot_function.png', bbox_inches='tight')
plt.show()
