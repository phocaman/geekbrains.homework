import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 2 * np.pi, 0.1)
y1 = np.cos(x)
y2 = np.cos(2 * x)


plt.plot(y1)
plt.plot(y2)
plt.show()
