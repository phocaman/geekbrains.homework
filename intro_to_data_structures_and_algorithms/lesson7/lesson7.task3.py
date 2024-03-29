# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# то используйте метод сортировки, который не рассматривался на уроках.

from numpy.random import randint
import big_o

def get_median(array):
    if len(array) < 1:
        return(None)
    if len(array) % 2 == 0:
        median = (array[len(array) // 2 - 1: len(array) // 2 + 1])
        return sum(median) / len(median)
    else:
        return(array[len(array) // 2])

m = 20
array = sorted(list(randint(0, 100) for _ in range(2 * m + 1)))
#  здесь вполне можно обойтись без sorted, однако
#  с ним удобнее проверять правильность нахождения медианы

print(f'Массив: {array}')
print(f'Медиана: {get_median(array)}')

positive_int_generator = lambda n: big_o.datagen.integers(n, 0, 10000)
best, others = big_o.big_o(get_median, positive_int_generator, n_repeats=100)
print(best)