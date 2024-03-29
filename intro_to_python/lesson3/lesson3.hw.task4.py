# № 4

# Программа принимает действительное положительное число x и целое
# отрицательное число y. Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y). При решении
# задания необходимо обойтись без встроенной функции возведения числа в степень.

# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень
# с помощью оператора **. Второй — более сложная реализация без оператора **,
# предусматривающая использование цикла.

# Решение № 1 (**)


import random
randint1 = random.randint(2, 10)
randint2 = random.randint(-10, -2)


def my_func(x, y):
    z = 1 / x ** abs(y)
    return z


print('Решение № 1:')
print(f"x = {randint1}, y = {randint2}")
print(f"z = {my_func(randint1, randint2)}")


# Решение № 2 (for)


def my_func(x, y):
    z = 1
    for i in range(abs(-y)):
        if y < 0:
            z = z / x
        else:
            z = z * x
    return z


print('Решение № 2:')
print(f"x = {randint1}, y = {randint2}")
print(f"z = {my_func(randint1, randint2)}")