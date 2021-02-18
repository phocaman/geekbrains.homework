# № 3
# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# 3.2
# Решение через dict

month_num = int(input('Пожалуйста, введите порядковый номер месяца (напр., янв - 1, фев - 2 и т. д.): '))

seasons_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}

if month_num in {12, 1, 2}:
    print(seasons_dict.get(1))
elif month_num in {3, 4, 5}:
    print(seasons_dict.get(2))
elif month_num in {6, 7, 8}:
    print(seasons_dict.get(3))
elif month_num in {9, 10, 11}:
    print(seasons_dict.get(4))
else:
    print('Неверный порядковый номер')