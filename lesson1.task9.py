# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
number3 = int(input('Введите третье число: '))

if number1 != number2 != number3:
    if number1 > number2 > number3 or number1 < number2 < number3:
        print(f'Число {number2} - среднее.')
    elif number2 > number1 > number3 or number2 < number1 < number3:
        print(f'Число {number1} - среднее.')
    elif number1 > number3 > number2 or number1 < number3 < number2:
        print(f'Число {number3} - среднее.')
else:
    print('Введите три РАЗНЫХ числа.')