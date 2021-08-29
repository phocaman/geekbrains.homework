# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random as rd

n = 20
array = []
for i in range(n):
    array.append(rd.randint(1, 100) - 50)
print(f'Массив: {array}')

i = 0
index = -1
while i < n:
    if array[i] < 0 and index == -1:
        index = i
    elif array[i] < 0 and array[i] > array[index]:
        index = i
    i += 1

print(f'Максимальный отрицательный элемент: {array[index]}. Индекс элемента: {index}.')