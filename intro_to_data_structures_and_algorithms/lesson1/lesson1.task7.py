# 7. По длинам трех отрезков, введенных пользователем, определить возможность
# существования треугольника, составленного из этих отрезков. Если такой треугольник
# существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.

a = int(input('Введите длину первого отрезка: '))
b = int(input('Введите длину второго отрезка: '))
c = int(input('Введите длину третьего отрезка: '))

if (a + b) > c and (b + c) > a and (c + a) > b:
    if a == b == c:
        print('Треугольник равносторонний.')
    elif a == b or b == c or c == a:
        print('Треугольник равнобедренный.')
    else:
        print('Треугольник разносторонний.')