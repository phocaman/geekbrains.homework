# 2. Написать два алгоритма нахождения i-го по счёту простого числа.

# а) без использования «Решета Эратосфена»

import cProfile

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
            break
    else:
        return True

def get_nth_prime(n):
    x = []
    j = 2
    while len(x) < n:
        if (is_prime(j)) == True:
            x.append(j)
        j = j + 1
    print(x[n - 1])

# get_nth_prime(1)  #  2
# get_nth_prime(50)  #  229
# get_nth_prime(75)  #  379
# get_nth_prime(125)  #  691
# get_nth_prime(255)  #  1613
# get_nth_prime(315)  #  2087
# get_nth_prime(435)  #  3037
# get_nth_prime(500)  #  3571
# get_nth_prime(780)  #  5939
# get_nth_prime(840)  #  6473
# get_nth_prime(960)  #  7561
get_nth_prime(1000)  #  7919

#  Полученные результаты сверил с таблицей "The first 1000 prime numbers":
#  https://en.wikipedia.org/wiki/List_of_prime_numbers#The_first_1000_prime_numbers

# Time complexity (get_nth_prime()):
# O(n)

cProfile.run('get_nth_prime(1000)')

# 16842 function calls in 0.344 seconds

#    Ordered by: standard name

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.344    0.344 <string>:1(<module>)
#         1    0.005    0.005    0.344    0.344 lesson4.task2a.py:17(get_nth_prime)
#      7918    0.338    0.000    0.338    0.000 lesson4.task2a.py:7(is_prime)
#         1    0.000    0.000    0.344    0.344 {built-in method builtins.exec}
#      7919    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#      1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

import big_o
print(big_o.big_o(get_nth_prime, big_o.datagen.n_, n_repeats=20, min_n=2, max_n=25)[0])