# № 6б

# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения. Например, в первом задании
# выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение
# элементов списка будет прекращено.

# Задание Б

from itertools import cycle


c = 0
for i in cycle([3, 5, 8, 13, 21, 34, 55, 89]):    
    if c > 15:
        break
    print(i)
    c += 1