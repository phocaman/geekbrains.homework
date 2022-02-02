# 2. Написать два алгоритма нахождения i-го по счёту простого числа.

# б) с использованием «Решета Эратосфена»

import itertools
import cProfile

def get_primes():
    D = {}
    yield 2
    for q in itertools.count(3, 2):
        p = D.pop(q, None)
        if p is None:
            yield q
            D[q * q] = q
        else:
            x = p + q
            while x in D or x % 2 == 0:
                x += p
            D[x] = p

def get_nth_prime(n):
    for i, p in enumerate(get_primes(), 1):
        if i == n:
            return p

# print(get_nth_prime(1))  #  2
# print(get_nth_prime(50))  #  229
# print(get_nth_prime(75))  #  379
# print(get_nth_prime(125))  #  691
# print(get_nth_prime(255))  #  1613
# print(get_nth_prime(315))  #  2087
# print(get_nth_prime(435))  #  3037
# print(get_nth_prime(500))  #  3571
# print(get_nth_prime(780))  #  5939
# print(get_nth_prime(840))  #  6473
# print(get_nth_prime(960))  #  7561
print(get_nth_prime(1000))  #  7919

#  Полученные результаты сверил с таблицей "The first 1000 prime numbers":
#  https://en.wikipedia.org/wiki/List_of_prime_numbers#The_first_1000_prime_numbers

# Time complexity (get_nth_prime()):
# O(log n)

cProfile.run('get_nth_prime(1000)')

# 4964 function calls in 0.006 seconds

#    Ordered by: standard name

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.006    0.006 <string>:1(<module>)
#         1    0.000    0.000    0.006    0.006 lesson4.task2b.py:22(get_nth_prime)
#      1001    0.005    0.000    0.006    0.000 lesson4.task2b.py:8(get_primes)
#         1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      3959    0.001    0.000    0.001    0.000 {method 'pop' of 'dict' objects}

import big_o
print(big_o.big_o(get_nth_prime, big_o.datagen.n_, n_repeats=20, min_n=2, max_n=25)[0])