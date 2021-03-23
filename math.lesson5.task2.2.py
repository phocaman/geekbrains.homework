# 2.
# 2) Сгенерируйте десять выборок случайных чисел х0, ..., х9.
# и постройте гистограмму распределения случайной суммы  x0 + ... + х9.


import numpy as np
import matplotlib.pyplot as plt


x0 = np.random.rand(100)
x1 = np.random.rand(100)
x2 = np.random.rand(100)
x3 = np.random.rand(100)
x4 = np.random.rand(100)
x5 = np.random.rand(100)
x6 = np.random.rand(100)
x7 = np.random.rand(100)
x8 = np.random.rand(100)
x9 = np.random.rand(100)
x_total = x0 + x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9
num_bins = 10
n, bins, patches = plt.hist(x_total, num_bins)
plt.xlabel('Сумма x0 + ... + x9')
plt.ylabel('Вероятность')
plt.title('Гистограмма')
plt.show()


