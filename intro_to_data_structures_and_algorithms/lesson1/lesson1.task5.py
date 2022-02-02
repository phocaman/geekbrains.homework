# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят
# и сколько между ними находится букв.

import string

letter1 = input('Введите любую букву английского алфавита (a-z, A-Z): ')
letter2 = input('Введите любую букву английского алфавита (a-z, A-Z): ')

def get_pos(letter):
    letter = letter.lower()
    return list(string.ascii_lowercase).index(letter) + 1

print(f'Позиция первой введённой буквы: {get_pos(letter1)}')
print(f'Позиция второй введённой буквы: {get_pos(letter2)}')

if letter1 == letter2:
    print(f'Количество букв между введёнными буквами: {get_pos(letter2) - get_pos(letter1)}')
else:
    print(f'Количество букв между введёнными буквами: {get_pos(letter2) - get_pos(letter1) - 1}')