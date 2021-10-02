#  Тема "Вычисления с помощью Numpy"


#  Задание 1

# Импортируйте библиотеку Numpy и дайте ей псевдоним np.
# Создайте массив Numpy под названием a размером 5x2, то есть состоящий из 5 строк и 2 столбцов.
# Первый столбец должен содержать числа 1, 2, 3, 3, 1, а второй - числа 6, 8, 11, 10, 7.
# Будем считать, что каждый столбец - это признак, а строка - наблюдение.
# Затем найдите среднее значение по каждому признаку, используя метод mean массива Numpy.
# Результат запишите в массив mean_a, в нем должно быть 2 элемента.

import numpy as np

a = np.array([[1, 6],
              [2, 8],
              [3, 11],
              [3, 10],
              [1, 7]])

mean_a = np.array([[np.mean(a[0:, 0]), np.mean(a[0:, 1])]])
print(f'\n{mean_a}')


#  Задание 2

# Вычислите массив a_centered, отняв от значений массива “а” средние значения соответствующих признаков,
# содержащиеся в массиве mean_a. Вычисление должно производиться в одно действие. Получившийся массив должен иметь размер 5x2.

a_centered = a - mean_a
print(f'\n{a_centered}')


#  Задание 3

# Найдите скалярное произведение столбцов массива a_centered. В результате должна
# получиться величина a_centered_sp. Затем поделите a_centered_sp на N-1, где N - число наблюдений.

a_centered_sp = sum([a_centered[0:, 0][i] * a_centered[0:, 1][i] for i in range(len(a_centered[0:, 0]))])
print(f'\n{a_centered_sp}')

denominator = len(a_centered[0:, 0]) - 1
print(f'\n{denominator}')

covariance = a_centered_sp / denominator
print(f'\n{covariance}')


#  Задание 4

# В этом задании проверьте получившееся число, вычислив ковариацию еще одним способом
# - с помощью функции np.cov. В качестве аргумента m функция np.cov должна принимать транспонированный массив "a".

a_t = np.transpose(a)
print(f'\n{a_t}')

cov_check = np.cov(a_t[0, 0:], a_t[1, 0:])
print(f'\n{cov_check}')

# cov_check_2 = np.cov(a_centered[0:, 0], a_centered[0:, 1])
# print(cov_check_2)


#  Задание 5

# Необходимо реализовать метод сортировки целых (int) элементов.
# Метод должен быть реализован без использования “готовых” методов ( sorted, np.sort() ).

def sort_int(arr):
    for i in range(len(arr)):
        swap = i + np.argmin(arr[i:])
        arr[i], arr[swap] = arr[swap], arr[i]
    return arr

print(f'\n{sort_int(a[0:, 0])}')

