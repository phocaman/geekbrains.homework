# № 4
#
# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
# параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры, уникальные
# для каждого типа оргтехники.


""" Проект "Склад оргтехники" (I) """


class Warehouse:
    ...


class Equipment:
    def __init__(self, eqpt_type, name, amount, price):
        self.eqpt_type = eqpt_type
        self.name = name
        self.amount = amount
        self.price = price


class Printer(Equipment):
    def __init__(self, eqpt_type, name, amount, price, printer_type, print_speed):
        super().__init__(eqpt_type, name, amount, price)

        """ Тип принтера: лазерный, струйный, матричный """
        self.printer_type = printer_type

        """ Скорость печати (стр./мин.) """
        self.print_speed = print_speed

    def __str__(self):
        return f"\nТип оборудования: {self.eqpt_type} \nНаименование: {self.name}" \
            f"\nКоличество: {self.amount} шт. \nЦена: {self.price} руб." \
            f"\nТип принтера: {self.printer_type} \nСкорость печати: {self.print_speed} стр./мин"


class Scanner(Equipment):
    def __init__(self, eqpt_type, name, amount, price, resolution):
        super().__init__(eqpt_type, name, amount, price)

        """ Разрешение (ppi) """
        self.resolution = resolution

    def __str__(self):
        return f"\nТип оборудования: {self.eqpt_type} \nНаименование: {self.name}" \
            f"\nКоличество: {self.amount} шт. \nЦена: {self.price} руб." \
            f"\nРазрешение: {self.resolution} пикселей на дюйм (ppi)"


class Photocopier(Equipment):
    def __init__(self, eqpt_type, name, amount, price, is_monochrome):
        super().__init__(eqpt_type, name, amount, price)

        """ Чёрно-белый или цветной """
        self.is_monochrome = is_monochrome

    def monochrome_color(self):
        if self.is_monochrome:
            return 'чёрно-белая'
        else:
            return 'цветная'

    def __str__(self):
        return f"\nТип оборудования: {self.eqpt_type} \nНаименование: {self.name}" \
            f"\nКоличество: {self.amount} шт. \nЦена: {self.price} руб." \
            f"\nТип печати: {self.monochrome_color()}"


printer = Printer('Принтер', 'Samsung', 1, 8000, 'лазерный', 30)
print(printer)
scanner = Scanner('Сканер', 'Epson', 1, 6000, 500)
print(scanner)
xerox = Photocopier('Копировальный аппарат', 'Xerox', 1, 15000, False)
print(xerox)