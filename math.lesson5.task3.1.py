# 3.
# 1) Дополните код Монте-Карло последовательности независимых испытаний расчетом
# соответствующих вероятностей (через биномиальное распределение) и сравните результаты.

import numpy as np
import math

k, n = 0, 1000  # При n = 10000 Python выдаёт OverflowError на факториалах при расчёте C
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + c + d

for i in range(0, n):
    if x[i] == 2:
        k = k + 1
print(k, n, k / n)

comb_kn = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
print(comb_kn)

prob_nk = comb_kn * ((k / n) ** k) * ((1 - k / n) ** (n - k))
print(prob_nk)
