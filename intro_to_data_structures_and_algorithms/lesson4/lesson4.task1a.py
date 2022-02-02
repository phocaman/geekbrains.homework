# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

# Задача № 3 из домашнего задания к уроку № 2:

# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

# а) первоначальная реализация

import cProfile

def get_reversed(n):
    reversed = 0
    while n > 0:
        reversed = (reversed * 10) + (n % 10)
        n = n // 10
    return f'Число, обратное по порядку цифр: {reversed}'

print(get_reversed(123456789))

# Time complexity:
# O(n)

cProfile.run('get_reversed(123456789)')

# 4 function calls in 0.000 seconds

#    Ordered by: standard name

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 lesson4.task1a.py:13(get_reversed)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

import big_o
print(big_o.big_o(get_reversed, big_o.datagen.n_, n_repeats=20, min_n=2, max_n=25)[0])