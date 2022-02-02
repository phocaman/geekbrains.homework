# № 4

# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк
# должен записываться в новый текстовый файл.

file_name = 'one_two_three_four.txt'
new_file_name = 'один_два_три_четыре.txt'
numerals_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open(file_name) as f:
    with open(new_file_name, 'w') as new_f:
        data = f.read()
        for key, value in numerals_dict.items():
            data = data.replace(key, value)
        print(data)
        new_f.write(data)

# #Результат:
#
# Один - 1
# Два - 2
# Три - 3
# Четыре - 4
#
# #Содержимое файла один_два_три_четыре.txt:
#
# Один - 1
# Два - 2
# Три - 3
# Четыре - 4