# № 2

# Для списка реализовать обмен значений соседних элементов,
# т. е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

user_list = input('Пожалуйста, введите элементы списка через пробел: ').split()

if len(user_list) % 2 == 0:
    i = 0
    while i < len(user_list):
        user_list[i], user_list[i + 1] = user_list[i + 1], user_list[i]
        i += 2
else:
    i = 0
    while i < len(user_list) - 1:
        user_list[i], user_list[i + 1] = user_list[i + 1], user_list[i]
        i += 2

print(user_list)