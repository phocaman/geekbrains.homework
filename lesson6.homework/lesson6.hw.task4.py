# № 4
#
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
# свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Автомобиль {self.name} (цвет: {self.color}) начал движение.")

    def stop(self):
        print(f"Автомобиль {self.name} (цвет: {self.color}) остановился.")

    def turn_right(self):
        print(f"Автомобиль {self.name} (цвет: {self.color}) повернул направо.")

    def turn_left(self):
        print(f"Автомобиль {self.name} (цвет: {self.color}) повернул налево.")

    def show_speed(self):
        print(f"Автомобиль {self.name} (цвет: {self.color}) движется со скоростью {self.speed} км/ч.")


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Автомобиль {self.name} (цвет: {self.color}) движется со скоростью {self.speed} км/ч.")
        if self.speed > 60:
            print(f"Скорость автомобиля {self.name} (цвет: {self.color}) превышает установленную скорость движения.")
        else:
            print(f"Автомобиль {self.name} (цвет: {self.color}) движется с допустимой скоростью.")


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Автомобиль {self.name} (цвет: {self.color}) движется со скоростью {self.speed} км/ч.")
        if self.speed > 40:
            print(f"Скорость автомобиля {self.name} (цвет: {self.color}) превышает установленную скорость движения.")
        else:
            print(f"Автомобиль {self.name} (цвет: {self.color}) движется с допустимой скоростью.")


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def cops(self):
        if self.is_police:
            print(f"Автомобиль {self.name} (цвет: {self.color}) зарегистрирован на управление внутренних дел.")
        else:
            raise ValueError('Ошибка: неверный класс.')


my_new_town_car = TownCar(80, 'баклажан', 'Lada', False)
print(my_new_town_car.speed)
print(my_new_town_car.color)
print(my_new_town_car.name)
print(my_new_town_car.is_police)
my_new_town_car.go()
my_new_town_car.turn_right()
my_new_town_car.turn_left()
my_new_town_car.show_speed()
my_new_town_car.stop()

my_new_sport_car = SportCar(150, 'красный', 'Maserati', False)
print(my_new_sport_car.speed)
print(my_new_sport_car.color)
print(my_new_sport_car.name)
print(my_new_sport_car.is_police)
my_new_sport_car.go()
my_new_sport_car.turn_right()
my_new_sport_car.turn_left()
my_new_sport_car.show_speed()
my_new_sport_car.stop()

my_new_work_car = WorkCar(40, 'серый', 'Газель', False)
print(my_new_work_car.speed)
print(my_new_work_car.color)
print(my_new_work_car.name)
print(my_new_work_car.is_police)
my_new_work_car.go()
my_new_work_car.turn_right()
my_new_work_car.turn_left()
my_new_work_car.show_speed()
my_new_work_car.stop()

their_new_police_car = PoliceCar(60, 'белый', 'Ford', True)
print(their_new_police_car.speed)
print(their_new_police_car.color)
print(their_new_police_car.name)
print(their_new_police_car.is_police)
their_new_police_car.go()
their_new_police_car.turn_right()
their_new_police_car.turn_left()
their_new_police_car.show_speed()
their_new_police_car.cops()
their_new_police_car.stop()