# 1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.

def count_substrings(str):
	substrings = set()
	for i in range(len(str) + 1):
		for j in range(i + 1, len(str) + 1):
			substrings.add(str[i:j])
	return f'\nПодстроки введённой строки: {substrings}\nКоличество подстрок: {len(substrings)}'

user_str = input('Введите строку, состоящую из строчных латинских букв: ')
print(count_substrings(user_str))