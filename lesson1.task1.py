# 1. Найти сумму и произведение цифр трёхзначного числа, которое вводит пользователь.

number = int(input('Введите трёхзначное число: '))

a = number % 10
number = number // 10
b = number % 10
number = number // 10

print(f'Сумма цифр числа = {number + a + b}')
print(f'Произведение цифр числа = {number * a * b}')