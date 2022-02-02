# № 5

# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить
# ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
# чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится
# специальный символ, выполнение программы завершается. Если специальный символ
# введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.


total = 0
while True:
    initial_data = input("Пожалуйста, введите несколько чисел через пробел"
                              " (или введите 'q' для выхода из программы): ")
    numbers = initial_data.split(' ')
    for number in numbers:
        try:
            item = int(number)
            total += item
        except:
            if number == 'q':
                print(f"Сумма введённых Вами чисел = {total}. Программа завершена.")
                exit(0)
            else:
                print(f"Сумма введённых Вами чисел = {total}. Введён неверный символ. Программа завершена.")
                exit(0)