# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный
# и отсортированный массивы. Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

from numpy.random import randint

def bubble_sort(array):
    is_swapped = True
    iter_count = 0
    while(is_swapped):
        is_swapped = False
        for i in range(len(array) - iter_count - 1):
            if array[i] < array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                is_swapped = True
        iter_count += 1

array = list(randint(-100, 100, 20))
print(f'Неотсортированный массив: {array}')
bubble_sort(array)
print(f'Массив, отсортированный по убыванию: {array}')