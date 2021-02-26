# № 5
#
# Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники
# на склад и передачу в определённое подразделение компании. Для хранения данных о наименовании и
# количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру
# (например, словарь).
#
# № 6
#
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый
# тип данных.


""" Проект "Склад оргтехники" (II) """


class Warehouse:

    def __init__(self):
        self.stored_items = []
        self.transferred_items = []

    def receive_items(self, equipment):
        print(f'Принять на склад {equipment.eqpt_type} {equipment.name}.')
        item = dict()
        item['ID'] = equipment.eqpt_id
        item['Тип оборудования'] = equipment.eqpt_type
        item['Наименование'] = equipment.name
        item['Количество'] = equipment.amount
        item['Цена'] = equipment.price
        self.stored_items.append(item)
        print(self.stored_items)
        print('Оборудование принято на склад.')
        print(f'Оборудование на складе: {self.stored_items}')

    def manually_receive_items(self):
        print('Принять оборудование на склад.')
        item = dict()
        item['ID'] = int(input('Введите ID: '))
        item['Тип оборудования'] = input('Введите тип оборудования: ')
        item['Наименование'] = input('Введите наименование: ')
        item['Количество, шт.'] = int(input('Введите количество: '))
        item['Цена, руб.'] = int(input('Введите цену: '))
        self.stored_items.append(item)
        print('Оборудование принято на склад.')
        print(f'Оборудование на складе: {self.stored_items}')

    def transfer_items(self, equipment):
        print('Передать оборудование со склада в офис.')
        equipment.eqpt_id = int(input('Введите ID оборудования: '))
        for i in range(len(self.stored_items)):
            if self.stored_items[i]['ID'] == equipment.eqpt_id:
                self.transferred_items.append(self.stored_items[i])
                del self.stored_items[i]
                break
        print('Оборудование передано со склада в офис.')
        print(f'Оборудование на складе: {self.stored_items}')
        print(f'Оборудование в офисе: {self.transferred_items}')


class Equipment:
    def __init__(self, eqpt_id, eqpt_type, name, amount, price):
        self.eqpt_id = eqpt_id
        self.eqpt_type = eqpt_type
        self.name = name
        self.amount = amount
        self.price = price


class Printer(Equipment):
    def __init__(self, eqpt_id, eqpt_type, name, amount, price, printer_type, print_speed):
        super().__init__(eqpt_id, eqpt_type, name, amount, price)

        """ Тип принтера: лазерный, струйный, матричный """
        self.printer_type = printer_type

        """ Скорость печати (стр./мин.) """
        self.print_speed = print_speed

    def __str__(self):
        return f"\nТип оборудования: {self.eqpt_type} \nНаименование: {self.name}" \
            f"\nКоличество: {self.amount} шт. \nЦена: {self.price} руб." \
            f"\nТип принтера: {self.printer_type} \nСкорость печати: {self.print_speed} стр./мин"


class Scanner(Equipment):
    def __init__(self, eqpt_id, eqpt_type, name, amount, price, resolution):
        super().__init__(eqpt_id, eqpt_type, name, amount, price)

        """ Разрешение (ppi) """
        self.resolution = resolution

    def __str__(self):
        return f"\nТип оборудования: {self.eqpt_type} \nНаименование: {self.name}" \
            f"\nКоличество: {self.amount} шт. \nЦена: {self.price} руб." \
            f"\nРазрешение: {self.resolution} пикселей на дюйм (ppi)"


class Photocopier(Equipment):
    def __init__(self, eqpt_id, eqpt_type, name, amount, price, is_monochrome):
        super().__init__(eqpt_id, eqpt_type, name, amount, price)

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


warehouse = Warehouse()

printer = Printer(1, 'принтер', 'Samsung', 1, 8000, 'лазерный', 30)
printer2 = Printer(2, 'принтер', 'HP', 1, 5000, 'струйный', 20)
scanner = Scanner(3, 'сканер', 'Epson', 1, 6000, 500)
xerox = Photocopier(4, 'копировальный аппарат', 'Xerox', 1, 15000, False)

warehouse.receive_items(printer)
warehouse.receive_items(printer2)
warehouse.receive_items(scanner)
warehouse.receive_items(xerox)
warehouse.manually_receive_items()

warehouse.transfer_items(printer)
warehouse.transfer_items(printer2)
warehouse.transfer_items(scanner)
warehouse.transfer_items(xerox)




