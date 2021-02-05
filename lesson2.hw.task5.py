# № 5
# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка.
# Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

import random

randomlist = random.sample(range(1, 10), 5)
randomlist.sort(reverse=True)
rating = randomlist
print('Рейтинг:', rating)

user_add = int(input('Пожалуйста, введите целое натуральное число: '))

for i in rating:
    if user_add > rating[0]:
        rating.insert(0, user_add)
        print(rating)
        break
    elif user_add == rating[0]:
        rating.insert(1, user_add)
        print(rating)
        break
    elif user_add <= rating[-1]:
        rating.insert(5, user_add)
        print(rating)
        break
    else:
        ind = int(rating.index(user_add))
        rating.insert(ind, user_add)
        print(rating)
        break