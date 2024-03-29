# № 2

# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
 
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

import random


randomlist = random.sample(range(1, 100), 20)
numbers = randomlist
new_numbers = [number for number in numbers if number > numbers[numbers.index(number)-1]]
print(numbers)
print(new_numbers)


# Пример:
# [16, 24, 60, 9, 27, 29, 95, 78, 74, 43, 15, 1, 5, 51, 94, 58, 55, 47, 40, 91]
# [24, 60, 27, 29, 95, 5, 51, 94, 91]