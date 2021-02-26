# № 2
#
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class MyOwnZeroDivErr(Exception):

    def __init__(self, text):
        self.text = text


dividend = float(input('Пожалуйста, введите делимое: '))
while True:
    try:
        divisor = float(input('Пожалуйста, введите делитель: '))
        if divisor == 0:
            raise MyOwnZeroDivErr('Недопустимая операция: деление на нуль.')
    except MyOwnZeroDivErr as e:
        print(e)
    else:
        print(f"Частное = {dividend / divisor}")
        break






