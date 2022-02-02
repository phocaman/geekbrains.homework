# № 7
#
# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json


file_name = 'companies_list.txt'

num_companies = 0

with open(file_name) as f:
    contents = f.readlines()
    companies_profit_loss = {}
    average_profit = {}
    companies_data = [companies_profit_loss, average_profit]
    for line in contents:
        line.rstrip()
        data = line.split()
        num_companies += 1
        revenue, cost = [int(i) for i in data if i.isdigit()]
        companies_profit_loss[data[0][:7]] = int(revenue - cost)
        profit_loss_total = 0
        for value in companies_profit_loss.values():
            if value > 0:
                profit_loss_total += value
        average_profit['Средняя прибыль'] = int(profit_loss_total / num_companies)


print(f"Прибыли и убытки компаний (словарь): {companies_profit_loss}")
print(f"Средняя прибыль (словарь): {average_profit}")
print(f"Список словарей: {companies_data}")


with open('companies_data.json', 'w', encoding='utf-8') as f:
    json.dump(companies_data, f)

with open ('companies_data.json', 'r', encoding='utf-8') as f:
    result = json.load(f)
print(f"Выгрузка из json-файла (список словарей): {result}")

# #Результат:
#
# Прибыли и убытки компаний (словарь): {'Альфа': 30000, 'Бета': 40000, 'Гамма': -5000,
#                                       'Дельта': -20000, 'Эпсилон': 60000}
# Средняя прибыль (словарь): {'Средняя прибыль': 26000}
# Список словарей: [{'Альфа': 30000, 'Бета': 40000, 'Гамма': -5000,
#                    'Дельта': -20000, 'Эпсилон': 60000}, {'Средняя прибыль': 26000}]
# Выгрузка из json-файла (список словарей): [{'Альфа': 30000, 'Бета': 40000, 'Гамма': -5000,
#                                             'Дельта': -20000, 'Эпсилон': 60000}, {'Средняя прибыль': 26000}]

# #Содержимое файла companies_list.txt:
#
# Альфа ООО 100000 70000
# Бета ООО 90000 50000
# Гамма ЗАО 80000 85000
# Дельта ЗАО 70000 90000
# Эпсилон ОАО 200000 140000