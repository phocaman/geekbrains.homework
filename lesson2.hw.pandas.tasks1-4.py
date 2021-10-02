#  Тема "Работа с данными в Pandas"


#  Задание 1

# Импортируйте библиотеку Pandas и дайте ей псевдоним pd. Создайте датафрейм authors со столбцами author_id и author_name,
# в которых соответственно содержатся данные: [1, 2, 3] и ['Тургенев', 'Чехов', 'Островский'].
# Затем создайте датафрейм book cо столбцами author_id, book_title и price, в которых соответственно содержатся данные:
# [1, 1, 1, 2, 2, 3, 3],
# ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
# [450, 300, 350, 500, 450, 370, 290].

import pandas as pd

authors = pd.DataFrame({'author_id': [1, 2, 3],
                        'author_name': ['Тургенев', 'Чехов', 'Островский']})
print(f'\n{authors}')

book = pd.DataFrame({'author_id': [1, 1, 1, 2, 2, 3, 3],
                    'book_title': ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
                    'price': [450, 300, 350, 500, 450, 370, 290]})
print(f'\n{book}')


#  Задание 2

# Получите датафрейм authors_price, соединив датафреймы authors и books по полю author_id.

authors_price = pd.merge(authors, book, on='author_id')
print(f'\n{authors_price}')


#  Задание 3

# Создайте датафрейм top5, в котором содержатся строки из authors_price с пятью самыми дорогими книгами.

top5 = authors_price.nlargest(5, 'price')
print(f'\n{top5}')


#  Задание 4

# Создайте датафрейм authors_stat на основе информации из authors_price. В датафрейме authors_stat должны быть четыре столбца:
# author_name, min_price, max_price и mean_price,
# в которых должны содержаться соответственно имя автора, минимальная, максимальная и средняя цена на книги этого автора.

groupby = authors_price.groupby('author_name')
min_price = groupby['price'].min()
max_price = groupby['price'].max()
mean_price = groupby['price'].mean()

authors_stat = pd.DataFrame({'min_price': min_price, 'max_price': max_price, 'mean_price': mean_price})
print(f'\n{authors_stat}')