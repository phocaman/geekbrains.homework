# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random as rd

n = 20
array = [0] * n
for i in range(n):
    array[i] = rd.randint(1, 100)
    print('%3d' % array[i], end = ' ')
print()

min_index = 0
max_index = 0
for i in range(1, n):
    if array[i] < array[min_index]:
        min_index = i
    elif array[i] > array[max_index]:
        max_index = i
print(f'Значение мин. элемента: {array[min_index]}\nЗначение макс. элемента: {array[max_index]}')

if min_index > max_index:
    min_index, max_index = max_index, min_index

sum_between = 0
for i in range(min_index + 1, max_index):
    sum_between += array[i]
print(f'Сумма элементов между мин. и макс. элементами: {sum_between}')