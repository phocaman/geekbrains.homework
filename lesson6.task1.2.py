# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.

# Задача № 7 домашнего задания к уроку № 3

# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

from numpy.random import randint
from pympler import asizeof

def get_two_smallest(array):
    min1 = sorted(array)[0]
    min2 = sorted(array)[1]
    return f'Первый наименьший элемент: {min1}', f'Второй наименьший элемент: {min2}'

array = randint(0, 10000, 50)
print(f'Массив: {array}')
print(get_two_smallest(array))

print(f'\nВыделено памяти под randint: {asizeof.asizeof(randint)} байт.')
print(f'Выделено памяти под asizeof: {asizeof.asizeof(asizeof)} байт.')
print(f'Выделено памяти под get_two_smallest(array): {asizeof.asizeof(get_two_smallest(array))} байт.')
print(f'Выделено памяти под min1: {asizeof.asizeof(sorted(array)[0])} байт.')
print(f'Выделено памяти под min2: {asizeof.asizeof(sorted(array)[1])} байт.')
print(f'Выделено памяти под array: {asizeof.asizeof(array)} байт.')
print(f'Выделено памяти под print(): {asizeof.asizeof(print())} байт.')
print(f'Выделено памяти под print(): {asizeof.asizeof(print())} байт.')

# Выделено памяти под randint: 0 байт.
# Выделено памяти под asizeof: 0 байт.
# Выделено памяти под get_two_smallest(array): 328 байт.
# Выделено памяти под min1: 48 байт.
# Выделено памяти под min2: 48 байт.
# Выделено памяти под array: 512 байт.
# Выделено памяти под print(): 16 байт.
# Выделено памяти под print(): 16 байт.

# Итого: 968 байт

# Mas OS X Yosemite 10.10.5
# Python 3.9.1 64-bit