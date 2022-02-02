# № 3

# Реализовать функцию my_func(), которая принимает три позиционных
# аргумента, и возвращает сумму наибольших двух аргументов.


import random
randint1 = random.randint(1, 100)
randint2 = random.randint(1, 100)
randint3 = random.randint(1, 100)


def my_func(a, b, c):
    numbers = [a, b, c]
    total = []
    largest1 = max(numbers)
    total.append(largest1)
    numbers.remove(largest1)
    largest2 = max(numbers)
    total.append(largest2)
    return sum(total)


print(f"a = {randint1}, b = {randint2}, c = {randint3}")
print(f"Сумма наибольших чисел = {my_func(randint1, randint2, randint3)}")