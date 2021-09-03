# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import defaultdict

hex1 = list(input('Введите шестнадцатеричное число: ').upper())
hex2 = list(input('Введите шестнадцатеричное число: ').upper())

hexadecimals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
decimals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
hex_dec = defaultdict(int)
for i in range(len(hexadecimals)):
    hex_dec[hexadecimals[i]] = decimals[i]

def hex_converter(n):
    return sum(16 ** key * int(hex_dec[val]) for key, val in enumerate(n[::-1]))

def dec_converter(n):
    x, remainder = n % 16, n // 16
    if remainder == 0:
        return hexadecimals[x]
    return dec_converter(remainder) + hexadecimals[x]

def add_hex(a, b):
    a, b = hex_converter(a), hex_converter(b)
    return f'Сумма = {list(dec_converter(a + b))}'

def multiply_hex(a, b):
    a, b = hex_converter(a), hex_converter(b)
    return f'Произведение = {list(dec_converter(a * b))}'

print(add_hex(hex1, hex2))
print(multiply_hex(hex1, hex2))