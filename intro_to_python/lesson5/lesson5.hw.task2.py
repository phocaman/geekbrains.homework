# № 2

# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.


file_name = '/Users/GeorgeEremin/PycharmProjects/geekbrains.homework/' \
            'lesson5.homework/2_Other files (.txt, .json)/onegin.txt'

num_lines = 0
i = 0
output = ''

with open(file_name) as f:
    for line in f:
        i += 1
        line.split()
        num_lines += 1
        words_in_line = len(line.split())
        output = output + 'Число слов в строке № ' + str(i) + ' = ' + str(words_in_line) + '\n'

print('\nЧисло строк в файле = ' + str(num_lines))
print('\n' + output)


# #Результат:
#
# Число строк в файле = 14
#
# Число слов в строке № 1 = 5
# Число слов в строке № 2 = 5
# Число слов в строке № 3 = 4
# Число слов в строке № 4 = 5
# Число слов в строке № 5 = 4
# Число слов в строке № 6 = 5
# Число слов в строке № 7 = 7
# Число слов в строке № 8 = 5
# Число слов в строке № 9 = 3
# Число слов в строке № 10 = 2
# Число слов в строке № 11 = 3
# Число слов в строке № 12 = 3
# Число слов в строке № 13 = 5
# Число слов в строке № 14 = 5
#
# #Содержимое файла onegin.txt:
#
# «Мой дядя самых честных правил,
# Когда не в шутку занемог,
# Он уважать себя заставил
# И лучше выдумать не мог.
# Его пример другим наука;
# Но, боже мой, какая скука
# С больным сидеть и день и ночь,
# Не отходя ни шагу прочь!
# Какое низкое коварство
# Полуживого забавлять,
# Ему подушки поправлять,
# Печально подносить лекарство,
# Вздыхать и думать про себя:
# Когда же черт возьмет тебя!»