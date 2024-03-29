# № 3
#
# Создайте собственный класс-исключение, который должен проверять содержимое списка
# на наличие только чисел. Проверить работу исключения на реальном примере. Запрашивать
# у пользователя данные и заполнять список необходимо только числами. Класс-исключение
# должен контролировать типы данных элементов списка.
#
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока
# пользователь сам не остановит работу скрипта, введя, например, команду «stop». При этом
# скрипт завершается, сформированный список с числами выводится на экран.
#
# Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
# Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента.
# Вносить его в список, только если введено число. Класс-исключение должен не позволить
# пользователю ввести текст (не число) и отобразить соответствующее сообщение. При этом работа
# скрипта не должна завершаться.


class MyOwnValueError(Exception):

    def __init__(self, text):
        self.text = text


num_list = []

while True:
    initial_data = input("Пожалуйста, введите число (или команду 'stop' для выхода из программы): ")
    numbers = initial_data.split(' ')
    for number in numbers:
        try:
            if number == 'stop':
                print('Программа завершена.')
                print(list(map(int, num_list)))
                exit(0)
            elif number.isdigit() is False:
                raise MyOwnValueError('Некорректное значение аргумента. Введите число.')
        except MyOwnValueError as e:
            print(e)
        else:
            if number.isdigit():
                num_list.append(number)