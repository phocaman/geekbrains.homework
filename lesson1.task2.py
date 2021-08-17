# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.

a = 5
b = 6

#  Побитовое И (AND)
print(f'a & b = {a & b}')
#  Ставит 1 на бит результата, для к-рого соответствующие биты операндов равны 1

#  Побитовое ИЛИ (OR)
print(f'a | b = {a | b}')
#  Ставит 1 на бит результата, для к-рого хотя бы один из соответствующих битов операндов равен 1

#  Побитовое НЕ (NOT)
print(f'~ a = {~ a}')
#  Заменяет каждый бит операнда на противоположный

#  Побитовое исключающее ИЛИ (XOR)
print(f'a ^ b = {a ^ b}')
#  Ставит 1 на бит результата, для к-рого только один из соответствующих битов операндов равен 1 (но не оба)

#  Побитовый сдвиг вправо
print(f'a >> 2 = {a >> 2}')
#  Сдвигает двоичное представление a на b битов вправо, отбрасывая сдвигаемые биты
#  В данном случае равен целочисленному делению на 2

#  Побитовый сдвиг влево
print(f'a << 2 = {a << 2}')
# Сдвигает двоичное представление a на b битов влево, добавляя справа нули
# В данном случае равен умножению на 2