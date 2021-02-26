# № 1
#
# Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Date:

    def __init__(self, d_m_y):
        self.d_m_y = str(d_m_y)

    @classmethod
    def get_d_m_y(cls, d_m_y):
        date = []
        for i in d_m_y.split('-'):
            if i.isdigit():
                date.append(i)
        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def is_valid(d, m, y):
        if 1 <= d <= 31 and 1 <= m <= 12 and 2021 >= y >= 0:
            return f'Данные верны.'
        else:
            return f'Неверные данные.'


new_date = Date('23-02-2021')
print(Date.get_d_m_y('23-02-2021'))
print(new_date.get_d_m_y('23-02-2021'))
print(Date.is_valid(23, 2, 2021))
print(new_date.is_valid(23, 2, 2021))



