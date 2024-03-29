# № 3
#
# Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления
# должно осуществляться округление значения до целого числа.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
# количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как
# произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как
# целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
# количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек
# между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает,
# то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.


class Cell:

    def __init__(self, amount):
        self._amount = amount

    def __add__(self, other):
        return Cell(self._amount + other._amount)

    def __sub__(self, other):
        if self._amount > other._amount:
            return Cell(self._amount - other._amount)
        print(f"{self._amount} - {other._amount}: Недопустимая операция.")

    def __mul__(self, other):
        return Cell(self._amount * other._amount)

    def __truediv__(self, other):
        return Cell(self._amount // other._amount)

    def make_order(self, per_seq):
        sequences, remainder = self._amount // per_seq, self._amount % per_seq
        return '\n'.join(['*' * per_seq] * sequences + (['*' * remainder] if remainder else []))

    def __str__(self):
        return f"Клетка состоит из {self._amount} ячеек."


cell_1 = Cell(25)
print(cell_1)
cell_2 = Cell(15)
print(cell_2)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_2 - cell_1)
print(cell_2 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print((cell_1 * cell_2).make_order(20))