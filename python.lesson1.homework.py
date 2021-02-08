# № 1

# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.

# № 1.1

a = 5
b = 10
x = (a + b)

print(x)
print()

greeting = ('Здравствуй')
punctmark1 = (',')
address1 = ('дорогой')
address2 = ('друг')
punctmark2 = ('!')

print(greeting + punctmark1, address1, address2 + punctmark2)
print()

# № 1.2

number = int(input('Пожалуйста, введите число: '))

print('Вы ввели число: ', number)
print()

name = input('Как Вас зовут? ')
age = int(input('Сколько Вам лет? '))
height = int(input('Какой у Вас рост в сантиметрах? '))
weight = int(input('Какой у Вас вес в килограммах? '))

print(f"Вас зовут {name}, Вам {age}, Ваш рост {height} см, Ваш вес {weight} кг.")
print()

# № 2

# Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

import time

n = int(input('Пожалуйста, введите время в секундах: '))

def convert(seconds):
    return time.strftime('%H:%M:%S', time.gmtime(n))

print(convert(n))
print()

# № 3

# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = int(input('Пожалуйста, введите число: '))
temp = str(n)
a = temp + temp
b = temp + temp + temp
comp = n + int(a) + int(b)

print(n + int(a) + int(b))
print('Итог:', comp)
print()

# № 4

# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('Пожалуйста, введите целое положительное число: '))

largest_num = number % 10
number = number // 10

while number > 0:
    if number % 10 > largest_num:
        largest_num = number % 10
    number = number // 10

print('Самая большая цифра в числе:', largest_num)
print()

# № 5

# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким
# финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток
# — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала
# с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее
# запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

sales = int(input('Пожалуйста, введите сумму выручки фирмы, руб.: '))
cost = int(input('Пожалуйста, введите сумму издержек фирмы, руб.: '))
profit = sales - cost

if sales > cost:
    print(f"Фирма получила прибыль в размере {profit} руб. Рентабельность выручки составила {profit / cost:.2f}.") # sales исправлено на profit
    employees = int(input('Пожалуйста, введите число сотрудников фирмы: '))
    print(f"Прибыль в расчёте на одного сотрудника составила {profit / employees:.2f} руб.")
else:
    print('Фирма получила убыток.')
print()


# № 6

# Спортсмен занимается ежедневными пробежками. В первый день его результат
# составил a километров. Каждый день спортсмен увеличивал результат на 10%
# относительно предыдущего. Требуется определить номер дня, на который результат
# спортсмена составит не менее b километров. Программа должна принимать значения
# параметров a и b и выводить одно натуральное число — номер дня.

a = int(input('Пожалуйста, введите результат первого дня тренировок, км: '))
b = int(input('Пожалуйста, введите желаемый результат, км: '))

days_to_target = 1
current_result = a

while current_result < b:
        a = a + a * 0.1
        days_to_target += 1
        current_result += a

print('Номер дня, когда будет достигнут желаемый результат:', days_to_target)
print()