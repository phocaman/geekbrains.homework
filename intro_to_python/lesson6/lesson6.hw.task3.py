# № 3
#
# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным
# и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы
# получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
        print(f"\nИмя, фамилия сотрудника: {name} {surname} \nДолжность: {position}"
              f"\nОклад: {wage} руб. \nПремия: {bonus} руб.")

    def get_full_name(self):
        get_full_name = self.name + ' ' + self.surname
        print(f"\nИмя, фамилия сотрудника: {get_full_name} ")

    def get_total_income(self):
        get_total_income = self._income.get('wage') + self._income.get('bonus')
        print(f"\nОбщий доход сотрудника: {get_total_income} руб.")


new_worker = Position('Иван', 'Петров', 'ведущий специалист', 120000, 30000)

print(f"\nИмя: {new_worker.name}")
print(f"Фамилия: {new_worker.surname}")
print(f"Должность: {new_worker.position}")
print(f"Доход: оклад - {new_worker._income.get('wage')} руб.,"
      f" премия - {new_worker._income.get('bonus')} руб.")

new_worker.get_full_name()
new_worker.get_total_income()

another_new_worker = Position('Пётр', 'Иванов', 'старший специалист', 100000, 20000)

print(f"\nИмя: {another_new_worker.name}")
print(f"Фамилия: {another_new_worker.surname}")
print(f"Должность: {another_new_worker.position}")
print(f"Доход: оклад - {another_new_worker._income.get('wage')} руб.,"
      f" премия - {another_new_worker._income.get('bonus')} руб.")

another_new_worker.get_full_name()
another_new_worker.get_total_income()