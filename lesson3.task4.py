# 4. Определить, какое число в массиве встречается чаще всего.

import random as rd

n = 20
array = [0] * n
for i in range(n):
    array[i] = rd.randint(1, 20)
print(array)

target_num = array[0]
num_frequency = 1
for i in range(n - 1):
    f = 1
    for j in range(i + 1, n):
        if array[i] == array[j]:
            f += 1
    if f > num_frequency:
        num_frequency = f
        target_num = array[i]

if num_frequency > 1:
    print(f'Частота появления числа {target_num} равна {num_frequency}.')
else:
    print('Все числа уникальны.')