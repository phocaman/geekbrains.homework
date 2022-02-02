# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

def get_reversed(n):
    reversed = 0
    while n > 0:
        remainder = n % 10
        reversed = reversed * 10 + remainder
        n = n // 10
    return f'Число, обратное по порядку цифр: {reversed}'

print(get_reversed(123456789))