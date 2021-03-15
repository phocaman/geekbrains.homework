# 5. Задание (в программе):
#
# 1) Нарисуйте трехмерный график двух параллельных плоскостей.
# 2) Нарисуйте трехмерный график двух любых поверхностей второго порядка.
#
# 1) график двух параллельных плоскостей:

from pylab import *
from mpl_toolkits.mplot3d import Axes3D

fig = figure()
ax = Axes3D(fig)

X = np.arange(-5, 5, 0.5)
Y = np.arange(-5, 5, 0.5)
X, Y = np.meshgrid(X, Y)

Z1 = (X + Y) - 2 ** 3
Z2 = (X + Y) + 3 ** 2

ax.plot_wireframe(X, Y, Z1)
ax.plot_wireframe(X, Y, Z2)
ax.plot_surface(X, Y, Z1, color='green')
ax.plot_surface(X, Y, Z2, color='orange')

show()
