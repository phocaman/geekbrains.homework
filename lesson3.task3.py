# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random as rd

n = 20
array = [0] * n
for i in range(n):
    array[i] = rd.randint(1, 100)
    print(array[i], end = ' ')
print()

minimum = 0
maximum = 0
for i in range(n):
    if array[i] < array[minimum]:
        minimum = i
    elif array[i] > array[maximum]:
        maximum = i
print(f'Мин. число = {array[minimum]}, индекс (1-20) = {minimum + 1}\nМакс. число = {array[maximum]}, индекс (1-20) = {maximum + 1}')
b = array[minimum]
array[minimum] = array[maximum]
array[maximum] = b

for i in range(n):
    print(array[i], end = ' ')
print()