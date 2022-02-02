# № 2
#
# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать
# защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
#
# Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
        print(f"\nПостроить дорогу длиной {_length} м, шириной {_width} м.")

    def total_cover_mass(self, sqm_cover_mass, thickness):
        self.sqm_cover_mass = sqm_cover_mass
        self.thickness = thickness
        total_cover_mass = int((self._length * self._width * sqm_cover_mass * thickness) / 1000)
        print(f"\nДля покрытия дорожного полотна необходимо {total_cover_mass} т асфальта.")


my_new_road = Road(20000, 10)
my_new_road.total_cover_mass(25, 0.05)