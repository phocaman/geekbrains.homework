# № 5

# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделённых пробелами. Программа должна подсчитывать сумму чисел в файле
# и выводить её на экран.

file_name = 'user_nums.txt'

with open(file_name, 'w') as f:
    data = input('\nВведите несколько чисел через пробел: ')
    f.write(data)

with open(file_name) as f:
    data = f.readlines()
    for line in data:
        user_nums = line.split()
        numbers = [int(i) for i in user_nums if i.isdigit()]
        sum_total = sum(numbers)
        print(f"\nСумма введённых чисел = {sum_total}")

# #Результат:
#
# Сумма введённых чисел = 1773
#
# #Содержимое файла user_nums.txt:
#
# 23 456 789 7 65 432 1