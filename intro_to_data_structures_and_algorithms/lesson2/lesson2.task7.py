# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел
# выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

n = int(input('Введите любое натуральное число: '))
def prove_equality(n):
    left_part = 0
    for i in range(1, n + 1):
        left_part += i
        right_part = n * (n + 1) // 2
    print(f'Левая часть равенства = {left_part}')
    print(f'Правая часть равенства = {right_part}')
    if left_part == right_part:
        print(f'{left_part} = {right_part}, что и требовалось доказать.')

prove_equality(n)