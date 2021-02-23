# № 1

# Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.

file_name = 'user_input.txt'

with open(file_name, 'w') as f:
    while True:
        line = input('Пожалуйста, введите данные: ')
        if line == ' ':
            print('Ввод окончен.')
            break
        f.write(line + '\n')

with open(file_name, 'r') as f:
    contents = f.read()
    print(f"Содержимое файла: \n{contents}")

# Пример.
#
# Содержимое файла:
# abc 123
# 456 def
# ghi 789
# 000 xyz