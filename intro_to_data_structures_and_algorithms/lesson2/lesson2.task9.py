# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

n = int(input('Введите число или введите 0 для выхода из программы: '))

def get_max(n):
    max_s = 0
    max_m = 0
    while n != 0:
        m = n
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        if s > max_s:
            max_s = s
            max_m = m
        n = int(input('Введите число или введите 0 для выхода из программы: '))
    return f'Число {max_m} - наибольшее по сумме цифр: {max_s}.'

print(get_max(n))