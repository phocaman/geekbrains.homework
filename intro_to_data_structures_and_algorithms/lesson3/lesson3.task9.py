# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random as rd

m = 5
n = 4
a = []
for i in range(n):
    b = []
    for j in range(m):
        num = rd.randint(1, 99)
        b.append(num)
        print('%4d' % num, end = '')
    a.append(b)
    print()

largest = -1
for j in range(m):
    smallest = 100
    for i in range(n):
        if a[i][j] < smallest:
            smallest = a[i][j]
    if smallest > largest:
        largest = smallest
print(f'Максимальный элемент среди минимальных: {largest}')