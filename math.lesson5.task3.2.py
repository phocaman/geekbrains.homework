# 3.
# 2) Повторите расчеты биномиальных коэффициентов и вероятностей k успехов в последовательности
# из n независимых испытаний, взяв другие значения n и k.


import numpy as np
import math


# Вариант 1

k, n = 0, 100
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + c + d

for i in range(0, n):
    if x[i] == 1:
        k = k + 1
print(k, n, k / n)

comb_kn = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
print(comb_kn)

prob_nk = comb_kn * ((k / n) ** k) * ((1 - k / n) ** (n - k))
print(prob_nk)


# Вариант 2

k, n = 0, 500
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + c + d

for i in range(0, n):
    if x[i] == 3:
        k = k + 1
print(k, n, k / n)

comb_kn = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
print(comb_kn)

prob_nk = comb_kn * ((k / n) ** k) * ((1 - k / n) ** (n - k))
print(prob_nk)

