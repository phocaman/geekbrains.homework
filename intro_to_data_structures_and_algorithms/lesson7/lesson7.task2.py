# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
# и отсортированный массивы.

from random import uniform

def merge_sort(array):
    if len(array) < 2:
        return array
    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    sorted_arr = []
    left_ind = right_ind = 0
    while True:
        if left_ind >= len(left):
            sorted_arr.extend(right[right_ind:])
            break
        if right_ind >= len(right):
            sorted_arr.extend(left[left_ind:])
            break
        if left[left_ind] < right[right_ind]:
            sorted_arr.append(left[left_ind])
            left_ind += 1
        else:
            sorted_arr.append(right[right_ind])
            right_ind += 1
    return sorted_arr

array = list(round(uniform(0, 50), 2) for _ in range(0, 20))
print(f'Неотсортированный массив: {array}')
print(f'Массив, отсортированный по возрастанию: {merge_sort(array)}')