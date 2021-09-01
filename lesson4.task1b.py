# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

# Задача № 3 из домашнего задания к уроку № 2:

# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

# б) альтернативная реализация

import cProfile

def get_reversed(num):
  return f'Число, обратное по порядку цифр: {int(str(num)[::-1])}'

print(get_reversed(123456789))

# Time complexity:
# O(1)

cProfile.run('get_reversed(123456789)')

# 4 function calls in 0.000 seconds

#    Ordered by: standard name

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 lesson4.task1b.py:13(get_reversed)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}