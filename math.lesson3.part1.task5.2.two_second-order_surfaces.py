# 5. Задание (в программе):
#
# 1) Нарисуйте трехмерный график двух параллельных плоскостей.
# 2) Нарисуйте трехмерный график двух любых поверхностей второго порядка.
#
# 2) график двух поверхностей второго порядка:

from pylab import *
from mpl_toolkits.mplot3d import Axes3D

fig = figure()
ax = Axes3D(fig)

X = np.arange(-5, 5, 0.5)
Y = np.arange(-5, 5, 0.5)

X, Y = np.meshgrid(X, Y)

Z1 = np.sqrt(X**2 + Y**2)
Z2 = -np.sqrt(X**2 + Y**2)

ax.plot_wireframe(X, Y, Z1)
ax.plot_wireframe(X, Y, Z2)
ax.plot_surface(X, Y, Z1, color='green')
ax.plot_surface(X, Y, Z2, color='orange')

show()
