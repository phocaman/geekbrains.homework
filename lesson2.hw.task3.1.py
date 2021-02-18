# № 3
# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# 3.1
# Решение через list

month_num = int(input('Пожалуйста, введите порядковый номер месяца (напр., янв - 1, фев - 2 и т. д.): '))

def get_season(month_num):
    months_list = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
    if month_num in months_list[0]:
        print('Зима')
    elif month_num in months_list[1]:
        print('Весна')
    elif month_num in months_list[2]:
        print('Лето')
    elif month_num in months_list[3]:
        print('Осень')
    else:
        print('Неверный порядковый номер')

get_season(month_num)
print()