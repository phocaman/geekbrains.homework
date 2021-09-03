# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия. Программа должна определить
# среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import defaultdict

companies = defaultdict()
num_of_companies = int(input('Введите количество предприятий: '))

while num_of_companies:
    name_of_company = input('\nВведите название предприятия: ')
    full_year_profit = input('Введите прибыль предприятия за 4 квартала (поквартально, через запятую): ').split(',')
    companies[name_of_company] = sum(list(map(int, full_year_profit)))
    num_of_companies -= 1

average_profit = sum(companies.values()) / len(companies)

print(f'\nСредняя годовая прибыль предприятий составила {average_profit} рублей.')

for name_of_company, full_year_profit in companies.items():
    if full_year_profit > average_profit:
        print(f'\nПрибыль предприятия {name_of_company} выше среднего значения.')
    elif full_year_profit < average_profit:
        print(f'\nПрибыль предприятия {name_of_company} ниже среднего значения.')