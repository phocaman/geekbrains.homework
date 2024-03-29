# № 5

# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить
# результат вычисления произведения всех элементов списка.

# Подсказка: использовать функцию reduce().

from functools import reduce


numbers = [number for number in range(100, 1001) if number % 2 == 0]
numbers_product = reduce((lambda x, y: x * y), numbers)
print(numbers)
print(numbers_product)