# № 1
#
# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами
# должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера,
# создав экземпляр и вызвав описанный метод.


import time


class TrafficLight:

    __color = ['КРАСНЫЙ', 'ЖЁЛТЫЙ', 'ЗЕЛЁНЫЙ']

    def running(self):
        i = 0
        while i < 3:
            if i == 0:
                print(f"\nСигнал светофора: {TrafficLight.__color[i]}. Движение запрещено.")
                time.sleep(7)
            elif i == 1:
                print(f"\nСигнал светофора: {TrafficLight.__color[i]}. Внимание!")
                time.sleep(2)
            elif i == 2:
                print(f"\nСигнал светофора: {TrafficLight.__color[i]}. Движение разрешено.")
                time.sleep(14)
            i += 1


my_traffic_light = TrafficLight()
my_traffic_light.running()