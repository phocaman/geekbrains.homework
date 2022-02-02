# № 5
#
# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Инструмент: {self.title}. Запуск отрисовки.")


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Новый инструмент: {self.title}. Запуск отрисовки авторучкой.")


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Новый инструмент: {self.title}. Запуск отрисовки карандашом.")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Новый инструмент: {self.title}. Запуск отрисовки маркером.")


my_new_writing_tool = Stationery('перо')
my_new_writing_tool.draw()

my_new_pen = Pen('авторучка')
my_new_pen.draw()

my_new_pencil = Pencil('карандаш')
my_new_pencil.draw()

my_new_handle = Handle('маркер')
my_new_handle.draw()