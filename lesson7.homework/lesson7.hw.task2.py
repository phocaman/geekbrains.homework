# № 2
#
# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы
# для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class AbstractGarments(ABC):

    @property
    @abstractmethod
    def fabric_consump(self):
        pass

    @property
    @abstractmethod
    def measuring(self):
        pass

    @abstractmethod
    def calc_fabric_consump(self):
        pass


class Garments(AbstractGarments):

    garments = []

    def __init__(self, name, measuring):
        self.name = name
        self._measuring = measuring
        self._fabric_consump = None

        self.garments.append(self)

    def calc_fabric_consump(self):
        raise NotImplemented

    @property
    def fabric_consump(self):
        if not self._fabric_consump:
            self.calc_fabric_consump()

        return self._fabric_consump

    @property
    def measuring(self):
        return self._measuring

    @property
    def total_fabric_consump(self):
        return sum([item.fabric_consump for item in self.garments])


class Coat(Garments):
    def calc_fabric_consump(self):
        self._fabric_consump = round(self.measuring / 6.5 + 0.5, 2)

    @property
    def V(self):
        return self.measuring

    def __str__(self):
        return f"Расход ткани на {self.name} (размер: {self.measuring}) " \
               f"составляет {self.fabric_consump} м."


class Suit(Garments):
    def calc_fabric_consump(self):
        self._fabric_consump = round(2 * self.measuring * 0.01 + 0.3, 2)

    @property
    def H(self):
        return self.measuring

    def __str__(self):
        return f"Расход ткани на {self.name} (рост: {self.measuring}) " \
               f"составляет {self.fabric_consump} м."


my_new_coat = Coat('пальто', 10)
print(my_new_coat)
print(my_new_coat.fabric_consump)
print(my_new_coat.measuring)
print(my_new_coat.V)
print(my_new_coat.total_fabric_consump)

my_new_suit = Suit('костюм', 175)
print(my_new_suit)
print(my_new_suit.fabric_consump)
print(my_new_suit.measuring)
print(my_new_suit.H)
print(my_new_suit.total_fabric_consump)
